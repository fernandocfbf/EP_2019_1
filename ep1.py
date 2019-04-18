# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fernando Fincatti, fernandocfbf@al.insper.edu.br
# - aluno B: Pedro Celia, pedrodc1@al.insper.edu.br
import random
import json

with open('Dicionario.json', 'r', encoding="utf8") as arquivo:
    dicionario = json.load(arquivo)
    
def carregar_cenarios():
    cenarios = dicionario 
    nome_cenario_atual = "dia anterior"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou enrolar, assistir Netflix,"
        " embaçar em geral. Amanhã eu falo com o professor sobre o EP.")
    print()
    print("Sua missão será enfrentar o professor e conseguir adiar o EP (boa sorte)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual['titulo'])
        print(len(cenario_atual['titulo'])*'-')
        print(cenario_atual['descricao'])
        
        vidaP1 = 100
        lista_ataque_P1 = ['Chutes mortais'] 
        inventario = []
        
        def define_valor_ataque(escolha):
            if escolha == 'Chutes mortais':
                ataqueP1 = random.randint(20,35)
            elif escolha == 'Mordidas sangrentas':
                ataqueP1 = random.randint(25,60)
            elif escolha == 'Socos em chamas':
                ataqueP1 = random.randint(50,100)
            
            return ataqueP1
        
        
        def define_valor_alimentos(escolha):
            if escolha == 'Big MC':
                soma = 60
            elif escolha == 'gaytorade':
                soma = 400
            elif escolha == 'energético':
                soma = 20
            return soma
            
        
        if nome_cenario_atual == 'Ir para a cozinha':
            inventario = ['Big MC']
        elif nome_cenario_atual == 'fugir':
            inventario[1] = 'energético'
        elif nome_cenario_atual == 'Lutar' or nome_cenario_atual == 'Fugir':
            inventario[2] = 'gaytorade'
            
            
            
            
        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
            
        else:

            print('suas opções:')
            for e,i in opcoes.items():
                print('{0}:{1}'.format(e,i))
            escolha = input("Digite a sua escolha: ")

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
    
# combate do SleepMonster
                
        if nome_cenario_atual == 'lutar':
            ataque_SleepMonster = 51
            vida_SleepMonster = 100
            print()
            print('COMBATE')
            print()
            while vidaP1 > 50 and vida_SleepMonster > 0:
                while len(inventario) > 0: 
                    print('SEU TURNO')
                    print()
                    comer = input('Antes de atacar, digite "sim" se '
                                  'você deseja comer alguma coisa ou "não" para continuar: ')
                    if comer == 'sim':
                        print('Você pode comer:')
                        for e in inventario:
                            print(e)
                            comendo = input('Digite o que deseja comer: ')
                        del inventario[comendo]
                        if comendo == 'energético':
                            ataque_SleepMonster = random.randint(0,10)
                                
                        somaVida = define_valor_alimentos(comendo)
                        vidaP1 += somaVida
                    elif comer == 'não':
                        print()
                        break
                break
                
            while vidaP1 > 50 and vida_SleepMonster > 0: 
                print('---SEU TURNO---')
                print('Seu HP:', vidaP1)
                print('Adversário HP:', vida_SleepMonster)
                print('Seu ataques disponíveis são:')
                for e in lista_ataque_P1:
                    print(e)
                    ataques = input('Digite o ataque que deseja usar: ')
                    ataqueP1 = define_valor_ataque(ataques)
                    print('Você o atingiu com {0} pontos '
                    'de dano'.format(ataqueP1))
                    print('---TURNO DO ADVERSÁRIO---')
                    vida_SleepMonster -= ataqueP1
                    print('Seu HP:', vidaP1)
                    print('Adversário HP:', vida_SleepMonster)
                    print('Você foi atingido com {0} pontos '
                    'de dano '.format(ataque_SleepMonster))
                    vidaP1 -= ataque_SleepMonster
                    print()
            
            if vidaP1 <= 50:
                print('Você foi gravemente ferido e caiu em um sono cheio de pesadelos!'
                ' Sua manhã será terrível')
            else:
                print('Você venceu a batalha e teve um ótimo sono! Pela manhã'
                ' você acordará perfeitamente descansado!')
                vidaP1 += 15
                
# combate final
                
        elif nome_cenario_atual == 'lutar contra o professor':
            ataque_Professor = random.randint(20,30)
            vida_Professor = 150
            print()
            print('COMBATE')
            print()
            while vidaP1 > 50 and vida_Professor > 0:
                while len(inventario) > 0: 
                    print('SEU TURNO')
                    print()
                    comer = input('Antes de atacar, digite "sim" se '
                                  'você deseja comer alguma coisa ou "não" para continuar: ')
                    if comer == 'sim':
                        print('Você pode comer:')
                        for e in inventario:
                            print('inventario[0]:(x1)')
                            comendo = input('Digite o que deseja comer: ')
                        del inventario[comendo]
                                
                        somaVida = define_valor_alimentos(comendo)
                        vidaP1 += somaVida
                    elif comer == 'não':
                        print()
                        break
                break
                
            while vidaP1 > 0 and vida_SleepMonster > 0: 
                print('---SEU TURNO---')
                print('Seu HP:', vidaP1)
                print('Adversário HP:', vida_Professor)
                print('Seu ataques disponíveis são:')
                for e in lista_ataque_P1:
                    print(e)
                    ataques = input('Digite o ataque que deseja usar: ')
                    ataqueP1 = define_valor_ataque(ataques)
                    print('Você o atingiu com {0} pontos '
                    'de dano'.format(ataqueP1))
                    print('---TURNO DO ADVERSÁRIO---')
                    vida_Professor -= ataqueP1
                    print('Seu HP:', vidaP1)
                    print('Adversário HP:', vida_Professor)
                    print('Você foi atingido com {0} pontos '
                    'de dano '.format(ataque_Professor))
                    vidaP1 -= ataque_Professor
                    print()
            
            if vidaP1 <= 0:
                print('GAME OVER')
            elif vida_Professor <= 0:
                print('Você conseguiu!!!!!!!! \n'
                'o EP será adiado para sempre')
            break
                                    
        

    print("Você morreu!")


    # Programa principal.
if __name__ == "__main__":
    main()
    
    
    
    
