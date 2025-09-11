import random


#-- Banco de ideias para histórias --
# Cada lista vai armazenar um elemento da nossa hitória

livro_de_hisorias = {
    "fantasia":{ }

},
"aventura":{

},
"amor_nao_correspondido":{

},
"comedia":{}

personagens = ['Um astronauta', 'Um Alien', 'Um menino', 'Uma meninina', 'Um dragão']
lugares = ['um castelo', 'uma estação espacial', 'um brechó', 'uma floresta']
acoes = ['encontrou', 'lutou contra', 'viajou para', 'descobriu uma passagem secreta', 'ganhou um concurso de dança']
objetos = ['um mapa do tesouro', 'uma espada magica', 'um capacete de brigadeiro', 'uma folha de papel']
desfechos = ['e viveram felizes para sempre', 'e salvaram o mundo', 'e virou rei', 'morreu mas passa bem', 'era mentira, mas era verdade']

personagem_sorted = random.choice(personagens)
lugar_sorted = random.choice(lugares)
acao_sorted = random.choice(acoes)
objeto_sorted = random.choice(objetos)
desfecho_sorted = random.choice(desfechos)

#-- Gerador de histórias --
# Vamos usar uma f-string (a letra 'f' antes
#  das aspas) para montar a frase final

historia = f"Era uma vez {personagem_sorted} que, em {lugar_sorted}, {acao_sorted} com a ajuda de {objeto_sorted}. No final, {desfecho_sorted}."

print("Aqui está a sua história:")
print(historia)

#-- Fim do gerador de histórias --