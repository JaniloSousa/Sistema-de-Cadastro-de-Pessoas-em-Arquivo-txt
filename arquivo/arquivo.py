from interface.interface import cabecalho

# função que verifica se o arquivo txt existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()

    except (FileNotFoundError):
        return False

    else:
        return True


# função responsável por criar o arquivo txt caso ele não exista
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()

    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[m \U0001F615')

    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m \U0000263A')


# função que ler o arquivo txt
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('\033[31mHouve um ERRO na leitura do arquivo!\033[m \U0001F615')

    else:
        cabecalho('PESSOAS CADASTRADAS')
        # loop for que mostrar os dados de cada pessoa de uma maneira mais "bonitinha" na tela
        print('  indice     nome     idade      sexo   ')
        for ind, linha in enumerate(a):
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '') # tirando a quebra de linha do último elemento
            print(f'{ind:^10}{dado[0]:^10}{dado[1]:^10}{dado[2]:^10}')

    finally:
        a.close()


# função que escreve ALGO A MAIS no arquivo txt
def cadastrar(arq, nome='desconhecido', idade=0, sexo = 'Não informado'):
    try:
        a = open(arq, 'at') # a -> append

    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m \U0001F615')

    else:
        try:
            a.write(f'{nome};{idade};{sexo}\n')

        except:
            print('\033[31mHouve um ERRO na hora de cadastrar os dados!\033[m \U0001F615')

        else:
            print(f'\033[32mNovo registro de \033[m{nome}\033[32m adicionado com sucesso!\033[m \U0000263A')
            a.close()

def excluirPessoa(arq, ind):
    try:
        arquivo = open(arq, 'r')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m \U0001F615')
    else:
        try:
            conteudo = arquivo.readlines()
        except:
            print('\033[31mHouve um ERRO na leitura do arquivo!\033[m \U0001F615')
        else:
            arquivo.close()

    # PREPARANDO OS DADOS ATUALIZADOS SEM O ITEM EXCLUÍDO
    pessoa_excluida = conteudo[ind].split(';')[0] # pegando a pessoa excluida
    conteudo.pop(ind)
    novo_conteudo = ''
    for linha in conteudo:
        novo_conteudo = novo_conteudo + linha

    try:
        arquivo = open(arq, 'w')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo!\033[m \U0001F615')
    else:
        try:
            arquivo.write(novo_conteudo)
        except:
            print('\033[31mHouve um ERRO ao atualizar os dados sem o item excluído\033[m \U0001F615')
        else:
            print(f'{pessoa_excluida} \033[32mexcluído(a) com sucesso!\033[m \U0000263A')
            arquivo.close()