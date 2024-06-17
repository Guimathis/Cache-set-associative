from service import *

# Importação do arquivo que contem as funções de manipulação de arquivos
from processamento_arquivos import *

# Códigos de cores para alterar cores no terminal
RESET = "\033[0m"
BLUE = "\033[34m"


# Loop de execução, primeiramente recebe o nome de um arquivo de informações
#   previamente preenchido com as informações sobre a mp e cache,
#   se o arquivo não for nulo chama função para ler os dados do arquivo de entrada e declarar a memória principal e a cache
#   se o nome do arquivo não for inserido, inicia-se o loop, mas para usar qualquer opção
#   é preciso ler um arquivo de informações.

# Inicia o loop de execuções para apresentar as opções
def loop_opções_execução(arq_infos=None):
    if arq_infos is not None:
        infos_mp_cache = ler_arquivo_infos_cc_mp(arq_infos)
        if infos_mp_cache is not None:
            dados_mp_cache = declarar_mp_cache(infos_mp_cache)
            memoria_principal = dados_mp_cache['memoriaPrincipal']
            cache = dados_mp_cache['cache']
            print('Arquivo lido com sucesso!')
            print(cache.__str__())
            print(memoria_principal.__str__())
    sair_loop = False
    while not sair_loop:
        print('Opções:')
        operação = ler_str \
            (f'{BLUE}R{RESET}: Ler novo arquivo de informações    | {BLUE}W{RESET}: Imprimir Informações\
             \n{BLUE}E{RESET}: Informar endereço de memória       | {BLUE}A{RESET}: Ler arquivo de endereços\
              \n{BLUE}T{RESET}: Imprimir taxa de falha/acerto      |<{BLUE}ENTER{RESET}>: Encerrar \nOpção')
        if operação is None:
            print('\nLeitura encerrada.')
            break
        match operação:

            # A opção 'R' tem a função de ler outro arquivo de informações sobre a mp e cache durante a execução
            #   usar esta opção durante a execução irá criar uma nova memória e resetar a cache
            case 'R' | 'r':
                arq_infos = ler_nome_arquivo()

                infos_mp_cache = ler_arquivo_infos_cc_mp(arq_infos)
                if infos_mp_cache is not None:
                    dados_mp_cache = declarar_mp_cache(infos_mp_cache)
                    memoria_principal = dados_mp_cache['memoriaPrincipal']
                    cache = dados_mp_cache['cache']
                    print('Arquivo lido com sucesso!')
                    print(cache.__str__())
                    print(memoria_principal.__str__())
                else: arq_infos = None

            # Opção 'W' imprime as informações da mp e cache como tag e tamanho do endereço,
            #   e imprime por completo a mp e cache própriamente.
            case 'W' | 'w':
                if arq_infos is not None:
                    print(str(cache))
                    print(str(memoria_principal))
                    cache.imprimir_cache()
                    memoria_principal.imprimir_memoria()
                else:
                    print('\nLeia um arquivo de informações para poder imprimir.\n')

            # Opção 'E' permite a leitura de um endereço de memória válido para acesso à mp
            #  o endereço é lido e passado para o método acessar_endereço que faz o processo de acesso a cache
            case 'E' | 'e':
                if arq_infos is None:
                    print('\nLeia um arquivo de informações para poder acessar um endereço.\n')
                else:
                    endereço_bin = input(f'   Digite um endereço binário de {memoria_principal.tamanho_do_endereco} bits: ')
                    if len(endereço_bin) != memoria_principal.tamanho_do_endereco or not endereço_bin.isdigit():
                        print('Endereço inválido, tente novamente:\n')
                    else:
                        print('------------------------------------------------------------------------------------------------------------------------------')
                        print(f'Acessando o endereço de memória {endereço_bin}:')
                        cache.acessar_endereço(endereço_bin, memoria_principal)
                        print('------------------------------------------------------------------------------------------------------------------------------')
            # Opção 'A' permite a leitura de um arquivo de endereços da memória principal
            case 'A' | 'a':
                arq_endereços = ler_nome_arquivo()
                if arq_infos is None:
                    print('\nLeia um arquivo de informações para poder acessar um endereço.\n')
                else:
                    ler_arquivo_endereços(arq_endereços, memoria_principal, cache)

            # Opção 'T' Permite imprimir a taxa de falha/acerto na cache
            case 'T' | 't':
                if arq_infos is None:
                    print('\nLeia um arquivo de informações para apresentar a taxa de falha/acerto.\n')
                else:
                    taxa_acertos_e_erros(cache.acerto, cache.falha)

            case _:
                print('\nOpção inválida, tente novamente:\n')


if __name__ == '__main__':
    loop_opções_execução(abrir_arquivo_execucao())
    # loop_opções_execução()
