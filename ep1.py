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

def define_valor_ataque(escolha):
            if escolha == 'Chutes mortais':
                ataqueP1 = random.randint(25,45)
            elif escolha == 'Mordidas radioativas':
                ataqueP1 = random.randint(40,60)
            elif escolha == 'Socos em chamas':
                ataqueP1 = random.randint(50,90)
            
            return ataqueP1

def define_valor_alimentos(escolha):
            if escolha == 'Big MC':
                soma = 60
            elif escolha == 'gaytorade':
                soma = 400
            elif escolha == 'energético':
                soma = 20
            return soma

def deleta_inventário(resposta):
    for e in range(len(inventario)-1):
        if inventario[e] == resposta:
            del inventario[e]
    return inventario
        


lista_ataque_P1 = ['Chutes mortais']       
inventario = [] 
inventario1 = []   
        


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
                
                
# código para o inventário
                
        if nome_cenario_atual == 'Ir para a cozinha':
             inventario.append('Big MC')
             
            
        elif nome_cenario_atual == 'fugir':
            inventario.append('energético')
            inventario1.append('chave')
            
            
        elif nome_cenario_atual == 'Lutar':
            inventario.append('gaytorade')
            
    
# combate do SleepMonster
                
        elif nome_cenario_atual == 'lutar':
            vidaP1 = 500
            ataque_SleepMonster = 251
            vida_SleepMonster = 100
            print()
            print('COMBATE')
            print()
            if len(inventario) > 0: 
                print('SEU TURNO')
                print()
                comer = input('Antes de atacar, digite "sim" se '
                              'você deseja comer alguma coisa ou "não" para continuar: ')
                if comer == 'sim':
                    print('Você pode comer:')
                    for e in inventario:
                        print(e)
                    comendo = input('Digite o que deseja comer: ')
                    a = deleta_inventário(comendo)
                    if comendo == 'energético':
                        ataque_SleepMonster = random.randint(0,10)
                        
                    somaVida = define_valor_alimentos(comendo)
                    vidaP1 += somaVida

                      
            while vidaP1 > 250 and vida_SleepMonster > 0:
                    
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
            
            if vidaP1 <= 250:
                print('Você foi gravemente ferido e caiu em um sono cheio de pesadelos!'
                ' Sua manhã será terrível')
            else:
                print('Você venceu a batalha e teve um ótimo sono! Pela manhã'
                ' você acordará perfeitamente descansado! (HP + 15)')
                vidaP1 += 15
                
# combate tiazinha da biblioteca
        
        elif nome_cenario_atual == 'enfrenta-lá':
            ataque_tiazinha = random.randint(20,50)
            vida_tiazinha = 100
            print()
            print('COMBATE')
            print()
            if len(inventario) > 0: 
                print('SEU TURNO')
                print()
                comer = input('Antes de atacar, digite "sim" se '
                              'você deseja comer alguma coisa ou "não" para continuar: ')
                if comer == 'sim':
                    print('Você pode comer:')
                    for e in inventario:
                        print(e)
                        comendo = input('Digite o que deseja comer: ')
                        a = deleta_inventário(comendo)
                            
                    somaVida = define_valor_alimentos(comendo)
                    vidaP1 += somaVida

                      
            while vidaP1 > 0 and vida_tiazinha > 0:
                    
                print('---SEU TURNO---')
                print('Seu HP:', vidaP1)
                print('Adversário HP:', vida_tiazinha)
                print('Seu ataques disponíveis são:')
                for e in lista_ataque_P1:
                    print(e)
                    ataques = input('Digite o ataque que deseja usar: ')
                    ataqueP1 = define_valor_ataque(ataques)
                    print('Você o atingiu com {0} pontos '
                    'de dano'.format(ataqueP1))
                    print('---TURNO DO ADVERSÁRIO---')
                    vida_tiazinha -= ataqueP1
                    print('Seu HP:', vidaP1)
                    print('Adversário HP:', vida_tiazinha)
                    print('Você foi atingido com {0} pontos '
                    'de dano '.format(ataque_tiazinha))
                    vidaP1 -= ataque_tiazinha
                    print()
            
            if vidaP1 <= 0:
                print('GAME OVER')
            else:
                print('Você venceu a batalha! Você tem os ataques Socos em chamas'
                      'e Mordidas radioativas')
                lista_ataque_P1.append('Mordidas radioativas')
                lista_ataque_P1.append('Socos em chamas')
                
        
# easteregg da armadura
                    
        elif nome_cenario_atual == 'quarto andar':
            if 'chave' in inventário1:
                print('UAU!! Você foi até seu armário e econtrou uma armadura!')
                vidaP1 *= 2
  
#combate com o professor.
                    
        elif nome_cenario_atual == 'lutar contra o professor':
            ataque_Professor = random.randint(80,150)
            vida_Professor = 1000
            print()
            print('COMBATE')
            print()
            if len(inventario) > 0: 
                print('SEU TURNO')
                print()
                comer = input('Antes de atacar, digite "sim" se '
                              'você deseja comer alguma coisa ou "não" para continuar: ')
                if comer == 'sim':
                    print('Você pode comer:')
                    for e in inventario:
                        print(e)
                        comendo = input('Digite o que deseja comer: ')
                        a = deleta_inventário(comendo)
                            
                    somaVida = define_valor_alimentos(comendo)
                    vidaP1 += somaVida

                      
            while vidaP1 > 0 and vida_Professor > 0:
                    
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
            else:
                print('Você conseguiu!!!! \n'
                'o EP será adiado para sempre')

#combate com a protetora do gaytorade.
            
        elif nome_cenario_atual == 'Lutar':
            ataque_da_protetora = random.randint(30,50)
            vida_da_protetora = 100
            print()
            print('COMBATE')
            print()
            if len(inventario) > 0: 
                print('SEU TURNO')
                print()
                comer = input('Antes de atacar, digite "sim" se '
                              'você deseja comer alguma coisa ou "não" para continuar: ')
                if comer == 'sim':
                    print('Você pode comer:')
                    for e in inventario:
                        print(e)
                        comendo = input('Digite o que deseja comer: ')
                        a = deleta_inventário(comendo)
                            
                    somaVida = define_valor_alimentos(comendo)
                    vidaP1 += somaVida

                      
            while vidaP1 > 0 and vida_da_protetora > 0:
                    
                print('---SEU TURNO---')
                print('Seu HP:', vidaP1)
                print('Adversário HP:', vida_da_protetora)
                print('Seu ataques disponíveis são:')
                for e in lista_ataque_P1:
                    print(e)
                    ataques = input('Digite o ataque que deseja usar: ')
                    ataqueP1 = define_valor_ataque(ataques)
                    print('Você o atingiu com {0} pontos '
                    'de dano'.format(ataqueP1))
                    print('---TURNO DO ADVERSÁRIO---')
                    vida_da_protetora -= ataqueP1
                    print('Seu HP:', vidaP1)
                    print('Adversário HP:', vida_da_protetora)
                    print('Você foi atingido com {0} pontos '
                    'de dano '.format(ataque_da_protetora))
                    vidaP1 -= ataque_da_protetora
                    print()
            
            if vidaP1 <= 0:
                print('GAME OVER')
            else:
                print('Você venceu a batalha!')
    
            break
                                    
        

    print("Você morreu!")


    # Programa principal.
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
