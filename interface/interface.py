# função que lê um dado e verifica se ele é um número iteiro
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m \U0001F615')
            continue

        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar nada.\033[m \U0001F615')
            return 0

        else:
            return n


# função que imprimi uma linha na tela com um tamanho informado
def linha(tam = 42):
    return '-' * tam


# função que imprimi um cabeçalho na tela
def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


# função resposável por apresentar um menu na tela
def menu(lista):
    cabecalho('MENU PRINCIPAL \U0001F4CB')

    c = 1
    for item in lista:
        print(f'\033[31m{c}\033[m -> \033[33m{item}\033[m')
        c += 1

    print(linha())
    
    opc = leiaInt('\033[34mSua Opção: \033[m')
    return opc