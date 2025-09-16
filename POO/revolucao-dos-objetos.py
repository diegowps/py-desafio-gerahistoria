Aula 1: A Revolução dos Objetos - Pensando Diferente (9:00 - 10:50)
Objetivo: Mudar o paradigma do código procedural para o orientado a objetos. Foco em classe, objeto, __init__ e self.

(15 min) Quebra-Gelo e Abertura:

Pergunta-Chave: "Se vocês tivessem que descrever um carro para um computador que não sabe o que é um carro, como fariam?" (Guiar a discussão para "características" e "ações").

Introdução da analogia: Classe = Planta da Casa, Objeto = A Casa Construída.

(40 min) Teoria e Live Coding 1: Criando a Primeira Classe

Explicação de classe como um molde.

Introdução do __init__ como o "construtor" e self como a forma do objeto "se enxergar".

Live Coding: Criar a classe Jogador com atributos nome e vida.

Python

class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.vida = 100 # Todo jogador começa com 100 de vida

    def exibir_status(self):
        print(f"Jogador: {self.nome}, Vida: {self.vida}")
Criar dois objetos jogador1 e jogador2 para provar que são independentes.

(40 min) Desafio Prático 1: O Inimigo Aparece!

Missão: "Agora é com vocês! Em duplas, criem a classe Monstro. Ela deve ter os atributos tipo (ex: "Zumbi") e forca. Crie um método chamado atacar() que simplesmente imprime na tela: O [tipo] ataca com [forca] de força!."

Circular pela sala, tirar dúvidas e ajudar.

(15 min) Revisão e Dúvidas:

Mostrar uma solução possível para o desafio.

Recapitular os conceitos: Classe, Objeto, __init__, self, Atributo, Método.