import pandas as pd
from math import sqrt
import streamlit as st
import random

# 1 relevante 0=irrelevante, None=nao avaliado
userReviews = {
   'anna': {
       'Red Dead Redemption': 0, 
       'Silent Hill 2': 1, 'Heavy Rain': 1, 'Max Payne 3': 0, 
       'Cyberpunk 2077': 1, 'Forza Horizon 4': 0, 'Forza Motorsport': 0, 
        'Monster Hunter: World': 0, 'Monster Hunter: Rise': 0, 
        'Dark Souls III': 1, 'Elden Ring': 1, 'Resident Evil 3': 1, 
      'Call of Duty: 4': 0, 
       'Dying Light': 1,  
    } ,
   'jose': {
       'Red Dead Redemption': 1, 
       'Red Dead Redemption 2': 1, 
     'Max Payne 3': 1, 
       'Cyberpunk 2077': 1, 'Forza Horizon 4': 1, 'Forza Motorsport': 1, 
       'Assetto Corsa': 1, 'Need For Speed':0,   
       'Dark Souls III': 1,  
         'Call of Duty: 4': 1, 
        'Dying Light': 1,  
    },
    'felipe': {
       'Red Dead Redemption': 1, 
       'Red Dead Redemption 2': 1, 
        'Max Payne 3': 1, 
       'Cyberpunk 2077': 1, 'Forza Horizon 4': 1, 'Forza Motorsport': 1, 
       'Assetto Corsa': 1, 'Need For Speed':0,  
       'Dark Souls III': 1, 
        'Call of Duty: 4': 1,  
        'Dota 2': 1
    },
} 

# 2 jogos avaliados
# 0 pouco relevante
# 1 muito relevante
games = {
    'Red Dead Redemption': { 
        "Open World" : 1,  
        "Story Rich": 1,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 1, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 1, 
        "Narration": 0, 
        "Shooter": 1, 
        "Classic": 1, 
        "Gore": 0.4,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.25, 
        "Sports": 0, 
        "First-Person": 0.15,
        "Replay Value": 0.75, 
        "Indie": 0,
        "Horror": 0
    },
    'Red Dead Redemption 2': {
        "Open World" : 1,  
        "Story Rich": 1,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 1, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 1, 
        "Narration": 0, 
        "Shooter": 1, 
        "Classic": 1, 
        "Gore": 0.4,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.25, 
        "Sports": 0, 
        "First-Person": 0.15,
        "Replay Value": 0.75, 
        "Indie": 0,
        "Horror": 0
    },
    'Silent Hill 2': {
        "Open World" : 0.25,  
        "Story Rich": 1,
        "Singleplayer": 1, 
        "Action": 0.15, 
        "Zombies": 0.65, 
        "Atmospheric": 1, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 1, 
        "Narration": 0.65, 
        "Shooter": 0.45, 
        "Classic": 1, 
        "Gore": 0.84,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 0, 
        "VR": 0, 
        "Realistic": 0.35, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.65, 
        "Indie": 0,
        "Horror": 0.95
    },
    'Heavy Rain': {
        "Open World" : 0,  
        "Story Rich": 1,
        "Singleplayer": 1, 
        "Action": 0.25, 
        "Zombies": 0, 
        "Atmospheric": 1, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 1, 
        "Narration": 0.85, 
        "Shooter": 0.25, 
        "Classic": 0, 
        "Gore": 0.24,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 0, 
        "VR": 0, 
        "Realistic": 0.65, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.25, 
        "Indie": 0,
        "Horror": 0.35
    },
    'Max Payne 3': {
        "Open World" : 0,  
        "Story Rich": 0.85,
        "Singleplayer": 1, 
        "Action": 0.95, 
        "Zombies": 0, 
        "Atmospheric": 1, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.75, 
        "Narration": 0.75, 
        "Shooter": 0.75, 
        "Classic": 0, 
        "Gore": 0.64,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.75, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.05, 
        "Indie": 0,
        "Horror": 0
    },
    'Cyberpunk 2077': {
        "Open World" : 1,  
        "Story Rich": 0.85,
        "Singleplayer": 1, 
        "Action": 0.95, 
        "Zombies": 0, 
        "Atmospheric": 1, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.75, 
        "Narration": 0.75, 
        "Shooter": 0.75, 
        "Classic": 0, 
        "Gore": 0.04,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 0, 
        "VR": 0, 
        "Realistic": 0.55, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.25, 
        "Indie": 0,
        "Horror": 0
    },
    'Forza Horizon 4': {
        "Open World" : 1,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 0, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.255, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0,
        "Racing": 1, 
        "Automobile Sim": 1, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.85, 
        "Sports": 0, 
        "First-Person": 1,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Forza Motorsport': {
        "Open World" : 0,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 0, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.255, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0,
        "Racing": 1, 
        "Automobile Sim": 1, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.85, 
        "Sports": 0, 
        "First-Person": 1,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Assetto Corsa':{
        "Open World" : 0,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 0, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.125, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0,
        "Racing": 1, 
        "Automobile Sim": 1, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 1, 
        "Sports": 1, 
        "First-Person": 1,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Need For Speed': {
        "Open World" : 1,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 0, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.255, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0,
        "Racing": 1, 
        "Automobile Sim": 1, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.85, 
        "Sports": 0, 
        "First-Person": 1,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Monster Hunter: World':{
        "Open World" : 0.65,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.455, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0.04,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.45, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Monster Hunter: Rise': {
        "Open World" : 0.75,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.455, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0.04,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.45, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Dark Souls III': {
        "Open World" : 1,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.755, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0.04,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.55, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Elden Ring': {
        "Open World" : 1,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 0, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.755, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0.04,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.55, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 0
    },
    'Resident Evil 3':{
        "Open World" : 0,  
        "Story Rich": 0.75,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 1, 
        "Atmospheric": 0.75, 
        "3D": 1, 
        "Third Person": 1, 
        "Great Soundtrack": 0.655, 
        "Narration": 0.00, 
        "Shooter": 1, 
        "Classic": 1, 
        "Gore": 0.74,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 0.5, 
        "VR": 0, 
        "Realistic": 0.75, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.95, 
        "Indie": 0,
        "Horror": 1
    },
    'Call of Duty: Modern Warfare': {
        "Open World" : 0,  
        "Story Rich": 0.75,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0.75, 
        "Atmospheric": 0.65, 
        "3D": 1, 
        "Third Person": 0, 
        "Great Soundtrack": 0.455, 
        "Narration": 0.00, 
        "Shooter": 1, 
        "Classic": 1, 
        "Gore": 0.44,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.75, 
        "Sports": 0, 
        "First-Person": 1,
        "Replay Value": 0.05, 
        "Indie": 0,
        "Horror": 0
    },
    'Call of Duty: 4': {
        "Open World" : 0,  
        "Story Rich": 0.75,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0.75, 
        "Atmospheric": 0.65, 
        "3D": 1, 
        "Third Person": 0, 
        "Great Soundtrack": 0.455, 
        "Narration": 0.00, 
        "Shooter": 1, 
        "Classic": 1, 
        "Gore": 0.44,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.75, 
        "Sports": 0, 
        "First-Person": 1,
        "Replay Value": 0.05, 
        "Indie": 0,
        "Horror": 0
    },
    'Dota 2':{
        "Open World" : 0,  
        "Story Rich": 0.00,
        "Singleplayer": 0, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 0.25, 
        "3D": 1, 
        "Third Person": 0, 
        "Great Soundtrack": 0.55, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0.14,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.25, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.00, 
        "Indie": 0,
        "Horror": 0
    },
    'Dying Light': {
        "Open World" : 1,  
        "Story Rich": 0.75,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0.95, 
        "Atmospheric": 0.85, 
        "3D": 1, 
        "Third Person": 0, 
        "Great Soundtrack": 0.455, 
        "Narration": 0.00, 
        "Shooter": 1, 
        "Classic": 0, 
        "Gore": 0.84,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.75, 
        "Sports": 0, 
        "First-Person": 1,
        "Replay Value": 0.45, 
        "Indie": 0,
        "Horror": 0.75
    },
    'Civilization 5': {
        "Open World" : 0,  
        "Story Rich": 0,
        "Singleplayer": 0.75, 
        "Action": 0, 
        "Zombies": 0, 
        "Atmospheric": 0.65, 
        "3D": 1, 
        "Third Person": 0, 
        "Great Soundtrack": 0.755, 
        "Narration": 0.00, 
        "Shooter": 0, 
        "Classic": 0, 
        "Gore": 0.84,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 1, 
        "VR": 0, 
        "Realistic": 0.25, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.65, 
        "Indie": 0,
        "Horror": 0
    },
    'Dead Space': {
        "Open World" : 0,  
        "Story Rich": 0,
        "Singleplayer": 1, 
        "Action": 1, 
        "Zombies": 0, 
        "Atmospheric": 0.95, 
        "3D": 1, 
        "Third Person": 0, 
        "Great Soundtrack": 0.755, 
        "Narration": 0.00, 
        "Shooter": 0.8, 
        "Classic": 0, 
        "Gore": 0.94,
        "Racing": 0, 
        "Automobile Sim": 0, 
        "Multiplayer": 0, 
        "VR": 0, 
        "Realistic": 0.55, 
        "Sports": 0, 
        "First-Person": 0,
        "Replay Value": 0.55, 
        "Indie": 0,
        "Horror": 1
    }
}

 

def cosseno(a, b):
    xy = 0
    sum_x2 = 0
    sum_y2 = 0
    for key in a:
        if key in b:
            sum_x2 += pow(a[key], 2)
            sum_y2 += pow(b[key], 2)
            xy += a[key] * b[key]
    
    print(f'xy {xy}')
    print(f'sum_x2 {sum_x2}')
    print(f'sum_y2 {sum_y2}')
    if xy ==0:
        return 0
    else:
        return (xy / (sqrt(sum_x2) * sqrt(sum_y2) ))


 
 

# Recomendação por itens
def recommend(gameName: str):
    # distancia entre itens
    distances = []
    for gameKey in games:
        if gameKey != gameName:
            distances.append( [cosseno(games[gameName], games[gameKey]), gameKey])
    
    distances.sort(reverse=True)

    print("FIM")
    print(distances[0:5])

    # usuarios que gostarem desse jogo
    filteredReviewers = [user for user in userReviews if gameName in userReviews[user].keys()]

    print(f"Aqui deve haver somente usuarios com este jogo na lista")
    print(filteredReviewers)
    # item mais similar por filtragem de conteudo
    mostSimilar = distances[0][1]

    knnGames = userReviews[filteredReviewers[0]].keys()

    otherRecommendations = []
    for game in distances:
        if game[1] != mostSimilar and game[1] in knnGames:
            if(len(otherRecommendations) < 4):
                otherRecommendations.append(game[1])
 
    print("otherRecommendations")
    print(otherRecommendations)

    print("most similar")
    print(mostSimilar)
    
    recommendations = [mostSimilar] + otherRecommendations
    print(f"recoomendations, {recommendations}")
    return distances

 

def recommend_app():
    options = []
    selected = ""
    all_options = games.keys()
    sample = []
    avaliados = []
    posRecomendacao = []

    st.title("Sistema de Recomendação Hibrido de Jogos")

     

    step = 1
    
    if 'step' not in st.session_state:
        print(f"nao há  ")
        st.session_state['step'] = step

    if 'step' in st.session_state:
        print(f"há {st.session_state['step']}")
        step = st.session_state['step']



    if step == 1:
        if 'sample' not in st.session_state:
            st.session_state['sample'] = random.sample(sorted(all_options), 10)
        
        if 'sample' in st.session_state:
            sample = st.session_state['sample']  
        
 
        # sample = random.sample(sorted(all_options), 10)
        print("sample")
        print(sample)
        avaliados = []
        for jogo in sample:
            adicionado = {}
            # avaliacao: True significa relevante
            adicionado[jogo] = { 'avaliacao': False}
            avaliados.append(adicionado)
        
        print("LISTA PARA AVALIAR")
        print(avaliados)
        st.write("### Passo 1:")
        st.write("#### Selecione os jogos relevantes para você, itens não marcados serão considerados relevantes")
        for avaliacao in avaliados:
            chave = list(avaliacao.keys())
            subChave = list(avaliacao[chave[0]])[0]
            avaliacao[chave[0]][subChave] = st.checkbox(chave[0])
            # avaliacao[chave[0]].avaliacao = st.checkbox(chave[0])
            # print(avaliacao[avaliacao.keys()[0]])


        if st.button("Seguir para o próximo passo"):
            st.session_state['avaliados'] = []
            st.session_state['avaliados'] = avaliados
            step =2 
            st.session_state['step'] = step
            print("passando para o passo 2")
            print(st.session_state['avaliados'])
    
    if step == 2:
        if 'posRecomendacao' in st.session_state:
            posRecomendacao =  st.session_state['posRecomendacao']
        title = st.text_input("Digite o titulo do jogo")
        if title:
            options = [x for x in all_options if title.lower() in x.lower() ]
            print('OPCOES ')
            print(options)
        

        if len(options):
            selected = st.selectbox("Selecione", options)

        if st.button("Obter recomendações") and len(selected) or len(posRecomendacao):
            st.write("# Recomendação por jogos similares")
            recommended = recommend(selected)
            
            if 'posRecomendacao' not in st.session_state:
                
                for recommendation in recommended[1:6]:
                    item = {}
                    item[recommendation[1]] = { 'avaliacao': False}
                    posRecomendacao.append(item)
                st.session_state['posRecomendacao'] = posRecomendacao

         


            if len(recommended):
                st.write(f"## Jogo mais similar: {recommended[0][1]}")
                st.write("### Você pode gostar também de: ")
                st.write("#### Marque as recomendações que concorda ")

                for game in posRecomendacao:
                    print(game)
                    key = list(game.keys())[0]
                    subKey = list(game[key].keys())[0]
                    print(f"key {key}, subkey {subKey}")
                    game[key][subKey] = st.checkbox(key)
                    # st.write(f">Pos - {game}")

                if st.button("Próximo passo"):
                    print()
                    st.session_state['posRecomendacao'] = posRecomendacao
                    step = 3
                    st.session_state['step'] = step
        

    if step == 3:
        st.write("## Desempenho do Sistema")

        if 'posRecomendacao' in st.session_state:
            posRecomendacao = st.session_state['posRecomendacao']
        if 'avaliados' in st.session_state:
            avaliados = st.session_state['avaliados']
        

        total_relevantes_recomendados = [ ]
        total_recomendados = len(posRecomendacao)
 

        total_relevantes = []

        for recomendacao in posRecomendacao:
            key = list(recomendacao.keys())[0]
            subKey = list(recomendacao[key].keys())[0]
            value = recomendacao[key][subKey]
            if value:
                total_relevantes_recomendados.append(recomendacao)
           

        for recomendacao in avaliados:
            key = list(recomendacao.keys())[0]
            subKey = list(recomendacao[key].keys())[0]
            value = recomendacao[key][subKey]
            if value:
                total_relevantes.append(recomendacao)

        if st.button("Obter métricas"):
            precisao = (len(total_relevantes_recomendados) / total_recomendados)  
            revocacao = (len(total_relevantes_recomendados) / len(total_relevantes))  
            f1Score = 2 * ( (precisao * revocacao ) / (precisao + revocacao)) 
            st.write(f"### Precisão: {precisao  * 100 } %")
            st.write(f"### Revocação: {revocacao * 100 } %")
            st.write(f"### F1 Score: {f1Score}  ")


             
            print("antes")
            print(avaliados)

            print("pos")
            print(posRecomendacao)

            print("total_relevantes_recomendados")
            print(total_relevantes_recomendados)
            print("total_relevantes")
            print(total_relevantes)



def main():
    recommend_app()

if __name__ == "__main__":
    main()