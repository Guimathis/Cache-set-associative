# Arquivo .py que contém todas as funções que manipulam arquivos

# Função para abrir um arquivo e ler os dados sobre a cache e a memória príncipal,
# Cria um dicionário e separa por nome as informações lidas do arquivo.
# Para acessar um dado use dados_cache_mp['nome do campo']
# fecha o arquivo e retorna um dicionário
def ler_arquivo_infos_cc_mp(nome_arq):
    try:
        f = open(nome_arq, 'r')
        infos = f.read().split('\n')
        dados_mp_cache = {'tamMemoria': int(infos[1].split(', ')[0]), 'palpBloco': int(infos[1].split(', ')[1]),
                          'tamCache': int(infos[3].split(', ')[0]), 'linpConjunto': int(infos[3].split(', ')[1])}
        f.close()

        return dados_mp_cache
    except FileNotFoundError:
        print('Arquivo não encontrado, tente novamente: \n')
        return None
    except TypeError:
        print('Arquivo não encontrado, tente novamente: \n')
        return None


# Recebe o nome do arquivo do usuário, testa se possui a extensão .txt
# e retorna o nome com extensão .txt
def ler_nome_arquivo():
    arquivo = input('Insira nome do arquivo:')
    if len(arquivo) == 0:
        return None
    # Verifica se o nome do arquivo fornecido possui a extensão ".txt"
    if not arquivo.endswith('.txt'):
        # Adiciona a extensão ".txt" ao nome do arquivo
        arquivo += '.txt'
    # print('Arquivo lido com sucesso!\n')
    return arquivo


# Ao executar o programa esta função recebe o nome do arquivo de informações
# antes de entrar no loop de execuções
def abrir_arquivo_execucao():
    arquivo = ler_nome_arquivo()
    if arquivo is not None and arquivo.find('.txt') != -1:
        return arquivo
    else:
        print('Entrada inválida, tente novamente.\n')
        return None

#  Abre um arquivo com endereços da memória, acessa e aloca os blocos dos respectivos endereços na memória
def ler_arquivo_endereços(nomeArquivo, memoria_principal, cache):
    try:
        with open(nomeArquivo, 'r') as f:
            enderecos = f.readlines()
            for endereco in enderecos:
                endereco_bin = endereco.strip()
                # Verificar se o endereço binário tem o comprimento correto
                if len(endereco_bin) == memoria_principal.tamanho_do_endereco:
                    print(
                        '------------------------------------------------------------------------------------------------------------------------')
                    print(f'Acessando o endereço de memória {endereco_bin}:')
                    cache.acessar_endereço(endereco_bin, memoria_principal)
                else:
                    print(f'Endereço inválido: {endereco_bin}\n')
            print(
                '------------------------------------------------------------------------------------------------------------------------')
    except FileNotFoundError:
        print(f'Erro: Arquivo {nomeArquivo} não encontrado.\n')
    except TypeError:
        print('Erro ao ler arquivo, tente Novamente:\n')