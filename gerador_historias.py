import random

#-- Banco de ideias para histórias --
# Cada lista vai armazenar um elemento da nossa hitória

livro_de_hisorias = {
    "fantasia":{ "personagens": ["papai noel felix", "fenixssara", "mbappe e a princesa encantada", "um elfo da floresta", "um dragão" ],
                "lugares": ["uma floresta encantada", "um castelo", "uma caverna secreta", "um reino distante", "uma montanha mágica" ],
                "acoes": ["encontrou um mapa do tesouro", "lutou contra umo vilão", "viajou para o espaço", "descobriu uma passagem"],
                          "objetos": ["uma espada mágica", "um amuleto poderoso", "um livro de feitiços", "uma poção misteriosa", "um escudo invencível"],
                          "desfechos": ["e viveram felizes para sempre", "e salvaram o mundo", "e virou rei", "morreu mas passa bem", "era mentira, mas era verdade"]
    },                          
    "aventura":{ "personagens": ["galã feio", "uma menina corajosa", "um pirata", "um explorador", "um cientista maluco"],
"lugares": ["Luanda", "uma ilha deserta", "uma cidade futurista", "um deserto escaldante", "uma selva perigosa"],
"acoes": ["encontrou um mapa do tesouro", "lutou contra um monstro", "viajou para o centro da terra", "descobriu uma civilização perdida", "sobreviveu a uma tempestade"],
"objetos": ["um artefato antigo", "uma bússola mágica", "um veículo incrível", "uma arma futurista", "um traje especial"],
"desfechos": ["e viveram felizes para sempre", "e salvaram o mundo", "e virou rei", "morreu mas passa bem", "era mentira, mas era verdade"]
    },
"amor_nao_correspondido":{ "personagens": ["um poeta", "uma garota tímida", "um músico de rua", "um artista de circo", "um cientista apaixonado"],
"lugares": ["uma cidade chuvosa", "um café aconchegante", "uma livraria antiga", "um parque florido", "uma praia deserta"],
"acoes": ["escreveu uma carta de amor", "cantou uma serenata", "pintou um retrato", "fez uma escultura", "inventou uma máquina do amor"],
"objetos": ["uma rosa vermelha", "um colar de coração", "um diário secreto", "um bilhete de cinema", "um ursinho de pelúcia"],
"desfechos": ["e viveram felizes para sempre", "e salvaram o mundo", "e virou rei", "morreu mas passa bem", "era mentira, mas era verdade"]
    },
"comedia":{
"personagens": ["um palhaço desastrado", "um cachorro falante", "um super-herói atrapalhado", "um robô confuso", "um mágico trapalhão"],
"lugares": ["um circo maluco", "uma cidade caótica", "uma escola bagunçada", "um parque de diversões", "uma nave espacial"],
"acoes": ["tentou salvar o dia", "se meteu em confusões", "fez uma invenção maluca", "participou de um concurso bizarro", "viajou no tempo por engano"],
"objetos": ["um nariz de palhaço", "uma capa de super-herói", "um chapéu mágico", "um controle remoto universal", "uma varinha de condão"],
"desfechos": ["e viveram felizes para sempre", "e salvaram o mundo", "e virou rei", "morreu mas passa bem", "era mentira, mas era verdade"]
}
}


# personagens = ['Um astronauta', 'Um Alien', 'Um menino', 'Uma meninina', 'Um dragão']
# lugares = ['um castelo', 'uma estação espacial', 'um brechó', 'uma floresta']
# acoes = ['encontrou', 'lutou contra', 'viajou para', 'descobriu uma passagem secreta', 'ganhou um concurso de dança']
# objetos = ['um mapa do tesouro', 'uma espada magica', 'um capacete de brigadeiro', 'uma folha de papel']
# desfechos = ['e viveram felizes para sempre', 'e salvaram o mundo', 'e virou rei', 'morreu mas passa bem', 'era mentira, mas era verdade']

# personagem_sorted = random.choice(personagens)
# lugar_sorted = random.choice(lugares)
# acao_sorted = random.choice(acoes)
# objeto_sorted = random.choice(objetos)
# desfecho_sorted = random.choice(desfechos)

#-- Gerador de histórias --
# Vamos usar uma f-string (a letra 'f' antes
#  das aspas) para montar a frase final

#historia = f"Era uma vez {personagem_sorted} que, em {lugar_sorted}, {acao_sorted} com a ajuda de {objeto_sorted}. No final, {desfecho_sorted}."


#Interação com o usuário
print("Bem-vindo ao gerador de histórias!")

tema_escolhido = input("Escolha um tema para a sua história (fantasia, aventura, amor não correspondido, comédia): ").strip().lower()

# print("Aqui está a sua história:")
# print(historia)


#Validação e sorteio

if tema_escolhido in livro_de_hisorias:
    # Seleciona o conjunto de listas com base na escolha do usuário

    listas_de_tema = livro_de_hisorias[tema_escolhido]
    # Sorteio (usando apenas as kistas do tema escolhido)
    personagem_sorted = random.choice(listas_de_tema["personagens"])
    lugar_sorted = random.choice(listas_de_tema["lugares"])
    acao_sorted = random.choice(listas_de_tema["acoes"])
    objeto_sorted = random.choice(listas_de_tema["objetos"])
    desfecho_sorted = random.choice(listas_de_tema["desfechos"])

    #Montagem da história
    historia = f"Era uma vez {personagem_sorted} que, em {lugar_sorted}, {acao_sorted} com a ajuda de {objeto_sorted}. No final, {desfecho_sorted}."

    print("Aqui está a sua história:")
    print(historia)
else:
    print("Desculpe, esse tema não está disponível. Por favor, escolha entre: fantasia, aventura, amor não correspondido, comédia.")
    
#-- Fim do gerador de histórias --