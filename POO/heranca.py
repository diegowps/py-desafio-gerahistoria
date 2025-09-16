class Animal:
    """ Classe Pai com um comportamento genérico. """
    def __init__(self, nome: str):
        self.nome = nome

    def falar(self):
        # Comportamento padrão para um animal genérico
        return "Este animal faz um som."

class Cachorro(Animal):
    """ Classe Filha que herda de Animal. """
    def falar(self):
        # Sobrescreve o método 'falar' para um comportamento específico
        return "Au au!"

class Gato(Animal):
    """ Outra Classe Filha que também herda de Animal. """
    def falar(self):
        return "Miau!"

# --- Uso ---
animal_generico = Animal("Criatura")
rex = Cachorro("Rex")
felix = Gato("Félix")

# Cada objeto chama o mesmo método ('falar'), mas obtém uma resposta diferente
print(f"{animal_generico.nome}: {animal_generico.falar()}")
print(f"{rex.nome}: {rex.falar()}")
print(f"{felix.nome}: {felix.falar()}")

