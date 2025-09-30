class Ram:
    def __init__(self, nome):
        self.nome = nome

class Processador:
    def __init__(self, nome):
        self.nome = nome

class Armazenamento:
    def __init__(self, nome):
        self.nome = nome

class Computador:
    def __init__(self, endereco):
        self.endereco = endereco
        self.memorias = []
        self.processadores = []
        self.armazenamentos = []

    def adicionar_ram(self, nome):
        ram = Ram (nome)
        self.memorias.append(ram)

    def adicionar_processador(self, nome):
        processador = Processador (nome)
        self.processadores.append(processador)

    def adicionar_armazenamento(self, nome):
        armazenamento = Armazenamento (nome)
        self.armazenamentos.append(armazenamento)

# Uso
computador = Computador("Asus, ROG Strix G15")
computador.adicionar_ram("16GB - HyperX")
computador.adicionar_processador("Intel Core i5-13400F - 4.6GHz")
computador.adicionar_armazenamento("SSD 480GB - Kingston A400")

print("RAM:", [c.nome for c in computador.memorias])
print("Processadores:", [c.nome for c in computador.processadores])
print("Armazenamentos:", [c.nome for c in computador.armazenamentos])