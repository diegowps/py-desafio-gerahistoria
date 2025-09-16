class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.vida = 100 # Todo jogador começa com 100 de vida

    def exibir_status(self):
        print(f"Jogador: {self.nome}, Vida: {self.vida}")    

# O Inimigo Aparece!
# Missão: "Agora é com vocês! Em duplas, criem a classe Monstro. 
# Ela deve ter os atributos tipo (ex: "Monstro") e forca. 
# Crie um método chamado atacar() 
# que simplesmente imprime na tela: 
# O [tipo] ataca com [forca] de força!."
# Circular pela sala, tirar dúvidas e ajudar.

#definição da classe (molde)
class Monstro:
    """Representar um monstro generico.
    A classe encapsula os atributos e ações de um monstro."""""

    def __init___(self, tipo: str, forca: int):
        """
        O construtor da classe. É chamado automaticamente quando um novo objeto monstro é criado.
        Sua função é definir os atributos iniciais do objeto."""
        self.tipo = tipo
        self.forca = forca
        print(f"Um novo monstro do tipo '{self.tipo}' apareceu!")

    def atacar(self):
        """ Metodo (ação) que o monstro pode realizar,
        Ele usa os atributos do próprio objeto ("self")
        para descrever o ataque.""" 
        print(f"O {self.tipo} ataca com {self.forca} de força!")
# --- Demonstração de uso ---
# # aqui, estamos criando um objeto monstro
# 
print("--- Criando um Monstro ---")
#Criando primeiro objeto (instância) da classe monstro
zumbi = Monstro(tipo="Zumbi", forca=15)

# # Criando o segundo objeto, independente do primeiro

ogro = Monstro(tipo="Ogro", forca=30)
print("\n--- Status dos Monstros ---")
#chamando o metodo atacar() de cada objeto
# # Cada monstro usa seus proprios atributos para o ataque.
zumbi.atacar()
ogro.atacar()

"No nosso jogo, teremos Zumbis, Esqueletos e Aranhas. 
Eles têm coisas em comum (vida, força) e coisas diferentes (Zumbi 
morde, Esqueleto atira flecha). Como evitamos copiar

e colar código?"

Introdução da analogia: Herança = Genética 
(Filhos herdam características dos pais).