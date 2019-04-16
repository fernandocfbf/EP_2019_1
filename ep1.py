import random
def carregar_cenarios():
    cenarios = {
        "dia anterior": {
            'titulo': 'Dia do descanso',
            'descricao' : 'Você está na sua casa',
            'opcoes': {
                'cozinha': 'comer alguma porcaria',    
                'sala de estar': 'Assistir TV',
                'quarto': 'dormir'
            }
        },
        "manhã do novo dia":{
            'titulo':  'A jornada',
            'descricao' : 'Você acordou, já se arrumou e está na rua iniciando sua jornada até o Insper',
            'opcoes': {
                'chamar um uber': 'pegar o celular',
                'tentar o busao': 'continuar ir até o ponto'
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
        inventário = []
        
        cenario_atual = cenarios[nome_cenario_atual]
        opcoes = cenario_atual['opcoes']
        descricao = cenario_atual['descricao']
        titulo = cenario_atual['titulo'] 
        print()
        print(titulo)
        print(descricao)
        
        print('Suas opções são: "Ir para a sala", "Ir para a cozinha" ou "Ir para o quarto".')    
        pergunta1 = input('Dessa opções, digite o que você deseja fazer: ')
        
        while pergunta1 != 'Ir para a sala' and pergunta1 != 'Ir para a cozinha' and pergunta1 != 'Ir para o quarto':
            pergunta1 = input('Resposta inválida, digite algo dentro das opções citadas: ')
            
        if pergunta1 == 'Ir para a sala':
            pergunta1_1 = input('Você está na sala de estar, o que deseja fazer: enrolar e assistir TV ou fazer o EP? ' )
            
            while pergunta1_1 != 'enrolar e assistir TV' and pergunta1_1 != 'fazer o EP':
                pergunta1_1 = input('Resposta inválida, digite algo dentro das opções citadas: ')
  
        elif pergunta1 == 'Ir para a cozinha':
            pergunta1_2 = input('Você está na cozinha, o que deseja fazer: comer alguma porcaria ou fazer o EP?')
        
            while pergunta1_2!= 'comer alguma porcaria' and pergunta1_2 != 'fazer o EP':
                pergunta1_2 = input ('Resposta inválida, digite algo dentro das opções citadas')
        
        elif pergunta1 == 'Ir para o quarto':
            pergunta1_3 = input('Você está no quarto, o que deseja fazer: dormir ou fazer o EP?')
            
            while pergunta1_3 != 'dormir' and pergunta1_3 != 'fazer o EP':
                pergunta1_3 = input('Resposta inválida, digite algo dentro das opções:')
        
        print ('Suas opções são:"chamar um uber" ou "tentar o busao"')
        pergunta2 = input('Dessas opções, digite o que você deseja fazer:')
        
        while pergunta2 != 'chamar um uber' and pergunta2 != 'tentar o busao':
            pergunta2 = input('Resposta inválida, digite algo dentro das opções citadas:')
        
        if pergunta2 == 'tentar o busao':
            pergunta2_1 = input('Você está indo para o ponto, o que deseja fazer: continuar ir até o ponto ou tentar ir apé até o Insper')
        
            while pergunta2_1 != 'continuar ir até o ponto' and pergunta2_1 != 'tentar ir apé até o Insper':
                pergunta2_1 = input('Resposta inválida, digite algo dentro das opções citadas:')
        
        if pergunta2 == 'chamar um uber':
            pergunta2_2 = input('Você vai chamar o uber, o que você deseja: pegar o celular ou tentar ir apé até o Insper:')
            
            while pergunta2_2 != 'pegar o celular' and pergunta2_2 != 'tentar ir apé até o Insper':
                pergunta2_2 = input('Resposta inválida, digite algo dentro das opções:')
                
        
        
        
        
        
        
        
        
        
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
    
