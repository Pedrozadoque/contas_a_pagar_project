import csv
from datetime import datetime

class Conta:
    def __init__(self, descricao, valor, data_vencimento, paga=False):
        self.descricao = descricao
        self.valor = valor
        self.data_vencimento = datetime.strptime(data_vencimento, '%Y-%m-%d')
        self.paga = paga

    def marcar_como_paga(self):
        self.paga = True

    def __str__(self):
        status = "Paga" if self.paga else "Pendente"
        return f"Conta: {self.descricao}, Valor: R${self.valor}, Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}, Status: {status}"
    
class ContasAPagar:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, descricao, valor, data_vencimento):
        nova_conta = Conta(descricao, valor, data_vencimento)
        self.contas.append(nova_conta)
        print(f"Conta '{descricao}' adicionada com sucesso.")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta encontrada.")
        for conta in self.contas:
            print(conta)

    def listar_contas_pendentes(self):
        print("Contas Pendentes:")
        for conta in self.contas:
            if not conta.paga:
                print(conta)

    def listar_contas_pagas(self):
        print("Contas Pagas:")
        for conta in self.contas:
            if conta.paga:
                print(conta)

    def marcar_conta_como_paga(self, descricao):
        for conta in self.contas:
            if conta.descricao == descricao:
                conta.marcar_como_paga()
                print(f"Conta '{descricao}' marcada como paga.")
                return
        print(f"Conta '{descricao}' não encontrada.")

    def gerar_relatorio(self):
        print("Relatório de Contas:")
        self.listar_contas_pagas()
        self.listar_contas_pendentes()


# Exemplo de uso:
contas = ContasAPagar()

# Adicionando contas
contas.adicionar_conta("Luz", 200, "2024-09-10")
contas.adicionar_conta("Água", 150, "2024-09-15")
contas.adicionar_conta("Internet", 120, "2024-09-20")

# Listando todas as Contas
contas.listar_contas()

# Marcando uma conta comm paga
contas.marcar_conta_como_paga("Luz")

# Listando contas pendentes()

# Gerando relatório
contas.gerar_relatorio()