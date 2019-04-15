import random
def carregar_cenarios():
    cenarios = {
        "dia anterior": {
            'titulo': 'Dia do descanso',
            'descricao' : 'Você está na sua casa',
            'opcoes': {
                'sala de estar': 'Assistir TV',
                'quarto': 'ir até o seu quarto'
            }
        },
                
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "dia anterior"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        Vida_P1 = 500
        
        cenario_atual = cenarios[nome_cenario_atual]
        opcoes = cenario_atual['opcoes']
        descricao = cenario_atual['descricao']
        titulo = cenario_atual['titulo'] 
        print(titulo)
        print('-----------------')
        print(descricao)
        print(opcoes)
        pergunta1 = input('Dessa opções o que você deseja fazer?')
        
        if pergunta1 == 'Assistir TV':
            print('Você está no sofá assistindo TV e encontrou o "BOSS DO SONO". Você deve enfrenta-lo para não cair no sono e deixar de fazer o EP')
            print('Seu HP: 500')
            print('BOSS DO SONO HP: 100')
            Vida_BOSS_DO_SONO = 100
            ataqueBOOS_DO_SONO = 251
            ataque_P1 = random.randint(0,1)
            print('Encare o desafio! É sua vez, você atingiu seu oponente com', ataque_P1, 'ponto de ataque')
            Vida_BOSS_DO_SONO -= ataque_P1
            print('BOSS DO SONO HP:', Vida_BOSS_DO_SONO) 
            print('Sofra as consequências! Você foi ferido por', ataqueBOOS_DO_SONO, 'pontos de ataque')
            if ataqueBOOS_DO_SONO > 250:
                print('Você não resistiu e caiu no sono')
            
            
          
            
            
        
        
        
        
        
        
        
        
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
    
