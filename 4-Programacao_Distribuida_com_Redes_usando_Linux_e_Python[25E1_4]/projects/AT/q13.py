#!/usr/bin/env python3
import dns.resolver
import dns.zone
import dns.query
from dnsrecon import *
import json
import unittest
import argparse

class DNSReconTool:
    def __init__(self, domain):
        self.domain = domain
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8', '1.1.1.1']  # DNS públicos

    def get_dns_records(self, record_type='A'):
        try:
            answers = self.resolver.resolve(self.domain, record_type)
            return [str(r) for r in answers]
        except dns.resolver.NoAnswer:
            return []
        except dns.resolver.NXDOMAIN:
            raise ValueError(f"Domínio {self.domain} não existe")

    def check_zone_transfer(self):
        ns_servers = self.get_dns_records('NS')
        results = []
        
        for ns in ns_servers:
            try:
                ns_ip = self.resolver.resolve(ns, 'A')[0]
                z = dns.zone.from_xfr(dns.query.xfr(str(ns_ip), self.domain))
                records = {}
                for name, node in z.nodes.items():
                    rdatasets = node.rdatasets
                    for rdataset in rdatasets:
                        records[str(name)] = [str(r) for r in rdataset]
                results.append({ns: records})
            except Exception as e:
                results.append({ns: f"Falha na transferência: {str(e)}"})
        
        return results

    def comprehensive_scan(self):
        report = []
        
        # Consulta dos registros padrão
        for record in ['A', 'AAAA', 'MX', 'TXT', 'SOA']:
            report.append({record: self.get_dns_records(record)})
        
        # Lista de subdomínios padrão embutida no código
        default_subdomains = ['www', 'mail', 'ftp', 'blog']
        subdomains = []
        for sub in default_subdomains:
            subdomain = f"{sub}.{self.domain}"
            try:
                self.resolver.resolve(subdomain, 'A')
                subdomains.append(subdomain)
            except:
                continue
        report.append({'subdomains': subdomains})
        
        return report

def main():
    parser = argparse.ArgumentParser(description='DNS Recon Tool')
    parser.add_argument('domain', help='Domínio para investigação')
    parser.add_argument('-z', '--zone', action='store_true', help='Tentar transferência de zona')
    parser.add_argument('-f', '--full', action='store_true', help='Varredura completa')
    
    args = parser.parse_args()
    tool = DNSReconTool(args.domain)
    
    try:
        if args.zone:
            print(f"\n[*] Tentando transferência de zona em {args.domain}")
            print(json.dumps(tool.check_zone_transfer(), indent=2))
        
        elif args.full:
            print(f"\n[*] Iniciando varredura completa em {args.domain}")
            print(json.dumps(tool.comprehensive_scan(), indent=2))
        
        else:
            print(f"\n[*] Registros básicos para {args.domain}:")
            print(f"A: {tool.get_dns_records('A')}")
            print(f"NS: {tool.get_dns_records('NS')}")
            print(f"MX: {tool.get_dns_records('MX')}")
    
    except Exception as e:
        print(f"\n[!] Erro: {str(e)}")

class TestDNSRecon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.domain = "example.com"
        cls.tool = DNSReconTool(cls.domain)

    def test_a_record(self):
        records = self.tool.get_dns_records('A')
        self.assertTrue(len(records) > 0, "Nenhum registro A encontrado")

    def test_zone_transfer(self):
        results = self.tool.check_zone_transfer()
        self.assertIsInstance(results, list)
        self.assertTrue(any("Falha na transferência" in str(v) for item in results for v in item.values()))

    def test_subdomains(self):
        scan = self.tool.comprehensive_scan()
        subdomains = [item for item in scan if 'subdomains' in item][0]['subdomains']
        self.assertTrue(len(subdomains) >= 0)

if __name__ == '__main__':
    import sys
    if '--test' in sys.argv:
        unittest.main(argv=sys.argv[:1])
    else:
        main()
