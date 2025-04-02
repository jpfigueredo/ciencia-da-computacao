class BrowserNavigation:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def visit_page(self, page):
        if self.current_page:
            self.back_stack.append(self.current_page)
        self.current_page = page
        self.forward_stack.clear()
        print(f"Visitou: {page}")

    def go_back(self):
        if not self.back_stack:
            print("Não há páginas para voltar.")
            return
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Voltou para: {self.current_page}")

    def go_forward(self):
        if not self.forward_stack:
            print("Não há páginas para avançar.")
            return
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Avançou para: {self.current_page}")

    def current(self):
        if self.current_page:
            print(f"Página atual: {self.current_page}")
        else:
            print("Nenhuma página carregada no momento.")

browser = BrowserNavigation()

browser.visit_page("https://www.google.com")
browser.visit_page("https://www.github.com")
browser.visit_page("https://www.stackoverflow.com")
browser.go_back()
browser.go_back()
browser.go_forward()
browser.current()
