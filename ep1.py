import random
def carregar_cenarios():
    cenarios = {
        "dia anterior": {
            'titulo': 'Dia do descanso',
            'descricao' : 'Você está na sua casa',
            'opcoes': {
                'Ir para a cozinha': 'abrir a geladeira, lavar a louça ou fazer o EP',    
                'Ir sala de estar': 'enrolar e assistir TV ou fazer o EP',
                'Ir quarto': 'dormir ou fazer o EP'
            }
        },
        "manhã do novo dia":{
            'titulo':  'A jornada',
            'descricao' : 'Você acordou, já se arrumou e está na rua iniciando sua jornada até o Insper',
            'opcoes': {
                'chamar um uber': 'pegar o celular ou tentar ir apé até o insper',
                'tentar o busao': 'continuar e ir até o ponto ou tentar ir apé até o Insper'
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
        
        Vida_Sleep_Monster = 100
        Ataque_Sleep_Monster = 251
        
        print('Suas opções são: "Ir para a sala", "Ir para a cozinha" ou "Ir para o quarto"')   
        pergunta1 = input('Dessa opções, digite o que você deseja fazer: ')
        
        while pergunta1 != 'Ir para a sala' and pergunta1 != 'Ir para a cozinha' and pergunta1 != 'Ir para o quarto':
            pergunta1 = input('Resposta inválida, digite algo dentro das opções citadas: ')
            
        if pergunta1 == 'Ir para a sala':
            pergunta1_1 = input('Você está na sala de estar, o que deseja fazer: enrolar e assistir TV ou fazer o EP? ' )
            
            while pergunta1_1 != 'enrolar e assistir TV' and pergunta1_1 != 'fazer o EP':
                pergunta1_1 = input('Resposta inválida, digite algo dentro das opções citadas: ')
                
            if pergunta1_1 == 'enrolar e assistir TV':
                print('Você está no sofá assistindo TV e encontrou o "Sleep Monster". Você deve enfrenta-lo para não cair no sono e deixar de fazer o EP')
                print('----------COMBATE----------')
                print('Seu HP: 500')
                print('Sleep Monster HP: 100')
                perguntaCombate1 = input('Você deseja "atacar" ou "fugir"? ')
                    
                while perguntaCombate1 != 'atacar' and perguntaCombate1 != 'fugir':
                    perguntaCombate1 = input('Resposta inválida, digite algo dentro das opções citadas: ')
                    
                if perguntaCombate1 == 'atacar':
                    print('--------Seu turno--------')
                    ataque_P1 = random.randint(0,20)
                    Vida_Sleep_Monster -= ataque_P1
                    print('Você o atingiu com um soco esmagador!')
                    print('HIT:',ataque_P1)
                    print('Sleep monster HP:', Vida_Sleep_Monster)
                    print('Seu HP:', Vida_P1)
                    print('--------Turno do adversário--------')
                    print('Você foi gravemente ferido!')
                    print('HIT:', Ataque_Sleep_Monster)
                    print('Você não resistiu e caiu em um sono profundo, sofra as consequências!')
                    
                else: 
                    print('Você tentou fugir, mas não deu tempo... sofra as consequências!')
                
            elif pergunta1_1 == 'fazer o EP':
                print('Você está determinado a fazer o EP, a introdução está feita,'
                'falta o desenvolvimento e a conclusão, mas está passando master chef na TV e '
                'o EP terá de ficar para outra hora...')
                       
        elif pergunta1 == 'Ir para a cozinha':
            pergunta1_2 = input('Você está na cozinha, o que deseja fazer: "abrir a geladeira", "lavar a louça" ou "fazer o EP?"')
        
            while pergunta1_2!= 'abrir a geladeira' and pergunta1_2!= 'fazer o EP' and pergunta1_2!= 'lavar a louça':
                pergunta1_2 = input ('Resposta inválida, digite algo dentro das opções citadas')
                
            if pergunta1_2 == 'abrir a geladeira':
                print('UAU!! Você encontrou um Mc lanche feliz, é melhor guarda-lo para depois.')
                inventário.append('Mc lanche feliz')
                pergunta1_2 = input('E agora o que deseja fazer: lavar a louça ou fazer o EP? ')
                if pergunta1_2 == 'lavar a louça':                
        
                    print('Você lavou a louça mas ficou muito cansado!'
                          'na sua frente surge um enorme monstro, é o Sleep Monster!')
                
                    perguntaCombate2 = input('Você deseja "atacar" ou "fugir"? ')
                    while perguntaCombate2 != 'atacar' and perguntaCombate2 != 'fugir':
                        perguntaCombate2 = input('Resposta inválida, digite algo dentro das opções citadas')
                        
                    if perguntaCombate2 == 'atacar':
                        ataque_P1 = random.randint(0,20)
                        Vida_Sleep_Monster -= ataque_P1
                        print('Você o atingiu com um soco esmagador!')
                        print('HIT:',ataque_P1)
                        print('Sleep monster HP:', Vida_Sleep_Monster)
                        print('Seu HP:', Vida_P1)
                        print('--------Turno do adversário--------')
                        print('Você foi gravemente ferido!')
                        print('HIT:', Ataque_Sleep_Monster)
                        print('Você não resistiu e caiu em um sono profundo, sofra as consequências!')
                            
                    else: 
                        print('Você tentou fugir, mas não deu tempo... sofra as consequências!')
                
            elif pergunta1_2 == 'lavar a louça':                
        
                print('Você lavou a louça mas ficou muito cansado!'
                'na sua frente surge um enorme monstro, é o Sleep Monster!')
                
                perguntaCombate2 = input('Você deseja "atacar" ou "fugir"? ')
                while perguntaCombate2 != 'atacar' and perguntaCombate2 != 'fugir':
                    perguntaCombate2 = input('Resposta inválida, digite algo dentro das opções citadas')
                
                if perguntaCombate2 == 'atacar':
                    ataque_P1 = random.randint(0,20)
                    Vida_Sleep_Monster -= ataque_P1
                    print('Você o atingiu com um soco esmagador!')
                    print('HIT:',ataque_P1)
                    print('Sleep monster HP:', Vida_Sleep_Monster)
                    print('Seu HP:', Vida_P1)
                    print('--------Turno do adversário--------')
                    print('Você foi gravemente ferido!')
                    print('HIT:', Ataque_Sleep_Monster)
                    print('Você não resistiu e caiu em um sono profundo, sofra as consequências!')
                
                else: 
                    print('Você tentou fugir, mas não deu tempo... sofra as consequências!')
            
            elif pergunta1_2 == 'fazer o EP':
                print('Você está determinado a fazer o EP, a introdução está feita,'
                'falta o desenvolvimento e a conclusão, mas está passando master chef na TV e '
                'o EP terá de ficar para outra hora...')
                inventário.append('introdução')
        
        elif pergunta1 == 'Ir para o quarto':
            pergunta1_4 = input('Você está no quarto, o que deseja fazer: dormir ou fazer o EP?')
            
            while pergunta1_4 != 'dormir' and pergunta1_4 != 'fazer o EP':
                pergunta1_4 = input('Resposta inválida, digite algo dentro das opções:')
            
            if pergunta1_4 == 'dormir':
                print('Você dormiu muito bem')
            else: 
                print('Você está determinado a fazer o EP, a introdução está feita,'
                'falta o desenvolvimento e a conclusão, mas está passando master chef na TV e '
                'o EP terá de ficar para outra hora...')
                inventário.append('introdução')
                
            
                
                
        cenario_atual = cenarios['manhã do novo dia']
        opcoes = cenario_atual['opcoes']
        descricao = cenario_atual['descricao']
        titulo = cenario_atual['titulo'] 
        print()
        print(titulo)
        print(descricao)
    
    
                
        
        
        
        
        
        
        
        
        
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
    
