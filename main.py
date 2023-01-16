# PROGRAMA PRINCIPAL
# fazendo as importações necessárias
# MEUS MÓDULOS
from interface.interface import *
from arquivo.arquivo import *

# módulo externo
from time import sleep

# verificando se o arquivo existe, se não, criando ele
arq = 'pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

# loop principal do meu programa
while True:
    resposta = menu(['Listar Pessoas Cadastradas', 'Cadastrar Uma Nova Pessoa', 'Excluir Uma Pessoa','Sair do Sistema'])

    # opção para listar todas as pessoas cadastradas
    if resposta == 1:
        lerArquivo(arq)

    # opção para cadastrar uma nova pessoa
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        sexo = str(input('Sexo [M/F]: '))
        cadastrar(arq, nome, idade, sexo)

    # opção de excluir uma pessoa
    elif resposta == 3:
        cabecalho('EXCLUINDO PESSOA')
        ind = int(input('Informe o índice da pessoa: '))
        excluirPessoa(arq, ind)
        sleep(2)

    # opção de encerrar o programa
    elif resposta == 4:
        cabecalho('Saindo do sistema... ')
        sleep(2)
        break

    # caso o usuário escolha um número de opção que não exista
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m \U0001F615')
        
    sleep(2)

print('Programa encerrado.')