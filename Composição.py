class Processador:
    def __init__(self, modelo: str, velocidade_ghz: float):
        self.modelo = modelo
        self.velocidade_ghz = velocidade_ghz

    def get_modelo(self):
        return self.modelo

    def get_velocidade_ghz(self):
        return self.velocidade_ghz

    def __str__(self):
        return f"Processador: {self.modelo}, {self.velocidade_ghz}GHz"
#== ==================================================================
class MemoriaRAM:
    def __init__(self, capacidade_gb: int, tipo: str):
        self.capacidade_gb = capacidade_gb
        self.tipo = tipo

    def get_capacidade_gb(self):
        return self.capacidade_gb

    def get_tipo(self):
        return self.tipo

    def __str__(self):
        return f"Memória RAM: {self.capacidade_gb}GB {self.tipo}"
#== ==================================================================
class Armazenamento:
    def __init__(self, tipo: str, capacidade_gb: int):
        self.tipo = tipo
        self.capacidade_gb = capacidade_gb

    def get_tipo(self):
        return self.tipo

    def get_capacidade_gb(self):
        return self.capacidade_gb

    def __str__(self):
        return f"Armazenamento: {self.tipo} {self.capacidade_gb}GB"
#== ==================================================================
class Computador:
    def __init__(self, marca: str, modelo: str, processador: Processador, memoria_ram: MemoriaRAM, armazenamento: Armazenamento):
        self.marca = marca
        self.modelo = modelo
        self.processador = processador
        self.memoria_ram = memoria_ram
        self.armazenamento = armazenamento

    # Getters
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_processador(self):
        return self.processador

    def get_memoria_ram(self):
        return self.memoria_ram

    def get_armazenamento(self):
        return self.armazenamento
#== ==================================================================
    def ligar(self):
        print(f"Ligando o {self.get_marca()} {self.get_modelo()}...")
        print("Especificações:")
        print(f"\n - {self.get_processador()}")
        print(f"\n - {self.get_memoria_ram()}")
        print(f"\n - {self.get_armazenamento()}")
        return self
    
    def __str__(self):
        return (f"Computador: {self.marca} {self.modelo}\n"
                f"  {self.processador}\n"
                f"  {self.memoria_ram}\n"
                f"  {self.armazenamento}")


#== ==================================================================
if __name__ == "__main__":
    cpu = Processador("Intel Core i7-12700F", 4.9)
    ram = MemoriaRAM(16, "DDR4")
    ssd = Armazenamento("SSD", 512)

    pc = Computador("Asus", "ROG Strix G15", cpu, ram, ssd)

    print(pc)
    pc.ligar()
