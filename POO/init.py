
O que exatamente são __init__ e self? Eles aparecem em todo lugar!
Resposta: Esses são dois dos conceitos mais fundamentais e 
importantes da POO em Python.

__init__(self, ...) (O Construtor):
Pense na classe como uma planta de uma casa. O __init__ é o 
conjunto de instruções iniciais que você executa toda vez que 
constrói uma nova casa a partir daquela planta. Ele "inicializa" o 
objeto.

O que ele faz? Sua principal função é receber os dados iniciais 
(como nome, vida e nivel) e atribuí-los como atributos ao objeto 
que está sendo criado.

Por que os dois underlines __? Em Python, isso indica que é um 
"método mágico" ou "método especial", que tem um comportamento 
pré-definido pela linguagem. O __init__ é chamado automaticamente 
no momento em 
que você cria um objeto (ex: heroi = Heroi(...)).

self (A Referência ao Próprio Objeto):
A palavra self é como o objeto se refere a si mesmo.

Analogia: Quando você pensa "Eu preciso beber água", o "Eu" é 
o self. Dentro de um método, o objeto precisa de uma forma de 
acessar seus próprios atributos e métodos.

#__init__ ponte
#self.ponte = ponte

Na prática: Quando escrevemos self.nome = nome dentro do __init__, 
estamos dizendo: "Para este objeto específico que estou criando "
"(self), defina o seu atributo nome com o valor da variável nome "
"que foi passada como parâmetro."

Todo método de uma classe deve ter self como seu primeiro parâmetro 
para que ele possa "saber" a qual objeto ele pertence e, assim, 
manipular os atributos corretos.

