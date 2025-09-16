class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.vida = 100 # Todo jogador começa com 100 de vida

    def exibir_status(self):
        print(f"Jogador: {self.nome}, Vida: {self.vida}")