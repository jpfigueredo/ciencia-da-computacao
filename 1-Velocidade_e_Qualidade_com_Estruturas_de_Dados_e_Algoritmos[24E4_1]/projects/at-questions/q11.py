class CustomerSupportQueue:
    def __init__(self):
        self.queue = []

    def add_ticket(self, ticket):
        self.queue.append(ticket)
        print(f"Chamado '{ticket}' adicionado à fila.")

    def process_ticket(self):
        if not self.queue:
            print("Nenhum chamado para processar.")
            return
        ticket = self.queue.pop(0)
        print(f"Processando chamado: '{ticket}'")

    def show_queue(self):
        if not self.queue:
            print("A fila está vazia.")
        else:
            print(f"Fila atual: {list(self.queue)}")

support_queue = CustomerSupportQueue()

support_queue.add_ticket("Chamado #1 - Problema no login")
support_queue.add_ticket("Chamado #2 - Erro no pagamento")
support_queue.add_ticket("Chamado #3 - Dúvida sobre o serviço")

support_queue.show_queue()

support_queue.process_ticket()
support_queue.process_ticket()
support_queue.show_queue()

support_queue.add_ticket("Chamado #4 - Atualização de dados")
support_queue.process_ticket()
support_queue.show_queue()
