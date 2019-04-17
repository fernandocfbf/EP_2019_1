# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Fernando Fincatti, fernandocfbf@al.insper.edu.br
# - aluno B: Pedro Celia, pedrodc1@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "dia anterior": {
            'titulo': 'Dia do descanso',
            'descricao' : 'Você está na sua casa',
            'opcoes': {
                'Ir para a cozinha': 'abrir a geladeira',    
                'Ir sala de estar': 'enrolar e assistir TV ',
                
            }
        },
        "Ir para a cozinha":{
            'titulo':  'Pico da alegria ',
            'descricao' : 'Você encontrou um Big Mc, isso está no seu inventário agora',
            'opcoes': {
                'dormir': 'ir para a cama dormir',
                'Ir sala de estar': 'voltar para a sala de estar'
            }
         },
        "Ir sala de estar":{
            'titulo':  'Pico do sossego',
            'descricao' : 'Você encontrou o Sleep Monster',
            'opcoes': {
                'lutar': 'combate',
                'fugir': 'ir para a cama dormir'
            }
        },
    
        "lutar": {
            "titulo": "A jornada",
            "descricao": "Você foi derrotado e caiu em um sono profundo. Agora acordou \n"
            "e está chegando no insper sem ter feito o EP",
            "opcoes": {
                "biblioteca": "pegar um livro",
                "quarto andar": "pegar uma mala",
                "andar professor": "ir para o andar do professor"
            }
        },
        "fugir": {
            "titulo": "Tiro de 100 metros",
            "descricao": "Você correu mas o ele te pegou e agora você caiu \n"
            'em um sono profundo. Agora acordou \n'
            "e está chegando no insper sem ter feito o EP",
            "opcoes": {
                "biblioteca": "pegar um livro",
                "quarto andar": "pegar uma mala",
                "andar professor": "ir para o andar do professor"
                
            }
        },
        "biblioteca": {
            "titulo": "Pico da leitura",
            "descricao": 'Você está na biblioteca e encontrou o "Magias pythonianas" \n'
            'isso lhe deu um ataque mais poderoso!',
            "opcoes": {
                "andar professor": "ir para o andar do professor",
                "quarto andar": "pegar uma mala"
            }
        },
        "quarto andar": {
            "titulo": "Pico de quem sabe",
            "descricao": 'Você está no quarto andar e econtrou uma mala, dentro dela \n'
            'havia um cheetos, agora isso está no seu iventário',
            "opcoes": {
                "andar professor": "ir para o andar do professor"
            }
        },
        "andar professor": {
            "titulo": "O conflito começa",
            "descricao": "Voce chegou ao andar da sala do seu professor, TAN TAN TAN...",
            "opcoes": {
                "lutar contra o professor": "enfrentar o professor",
                "encher linguiça": "pedir com jeitinho"
            }
        },
        "encher linguiça": {
            "titulo": "A discussão",
            "descricao": "Você negociou, tentou, mas falhou, a luta agora é inevitável",
            "opcoes": {
                "lutar contra o professor": "enfrentar o professor",
            }
        },
        "lutar contra o professor": {
            "titulo": "A batalha final",
            "descricao": "A porradaria começa",
            "opcoes": {
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

    print("Você morreu!")


    # Programa principal.
if __name__ == "__main__":
    main()
    
    
    
    
