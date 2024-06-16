# Biblioteca para lidar com vetores e numeros aleatórios, **NECESSITA pip install NumPy**
import numpy as np


from cache import *
from memoriaPrincipal import *

# Váriavel global para guardar o tamanho da palavra, que é especificado no trabalho ser 4
tam_palavra = 4

# Códigos de cores para alterar cores no terminal
RESET = "\033[0m"
RED = "\033[31m"


# Função que recebe o dicionário com as informações sobre a memória e a cache,
# faz alguns cálculos e atribuições e cria os objetos memória principal e cache
def declarar_mp_cache(infos_mp_cache):
    global tam_palavra
    # DADOS MEMÓRIA PRINCIPAL
    numero_de_linhas_mp = int((infos_mp_cache['tamMemoria'] * 1024) / tam_palavra)
    numero_de_blocos_mp = int(numero_de_linhas_mp / infos_mp_cache['palpBloco'])
    w = int(np.log2(infos_mp_cache['palpBloco']))
    s = int(np.log2(numero_de_blocos_mp))
    tamanho_endereço_mp = s + w
    # Criação do objeto memória com todos os seus atributos e a memória própriamente
    memoria_principal = MemoriaPrincipal(infos_mp_cache['tamMemoria'], infos_mp_cache['palpBloco'], numero_de_linhas_mp,
                                         numero_de_blocos_mp, w, s, tamanho_endereço_mp)

    # DADOS CACHE
    tamanho_linha_cache = int(tam_palavra * infos_mp_cache['palpBloco'])
    quantidade_linhas_cache = int((infos_mp_cache['tamCache'] * 1024) / tamanho_linha_cache)
    quantidade_conjuntos_cache = int(quantidade_linhas_cache / infos_mp_cache['linpConjunto'])
    d = int(np.log2(quantidade_conjuntos_cache))
    tag = s - d
    # Criação do objeto cache com todos os seus atributos e a cache própriamente
    cache = Cache(infos_mp_cache['tamCache'], infos_mp_cache['linpConjunto'], quantidade_conjuntos_cache,
                  quantidade_linhas_cache, d, tag)

    # guarda os objetos em um dicionário
    informações_mp_cache = {
        'memoriaPrincipal': memoria_principal,
        'cache': cache
    }
    # retorna o dicionário com a mp e a cache
    return informações_mp_cache


# Função para separar o endereço recebido em tag, s, d e w
# através da função strip, divide o endereço em 1 caractere por posição,
# onde o [valor_inicial:valor_final] define as posições que serão atribuidas as respesctivas váriaveis do dicionário
# e o int(valor, base) converte os valores de binário para decimal
def processa_endereco(endereco_bin, mp, cache):
    infos_endereço = {
        'linha_mp': int(endereco_bin, 2),
        'tag': endereco_bin.strip()[:cache.tag],
        's': int(endereco_bin.strip()[:mp.s], 2),
        'd': int(endereco_bin.strip()[cache.tag:mp.s], 2),
        'w': int(endereco_bin.strip()[mp.s:], 2),
    }
    return infos_endereço


def taxa_acertos_e_erros(acerto, falha):
    #Se if == verdadeiro imprimi que não houve acessos à cache.
    if acerto + falha == 0:
        print('\nSem acessos à Cache.\n')
        return
    #calcula as taxas para acerto e erro
    taxa_acerto = (acerto / (acerto + falha)) * 100
    taxa_erro = (falha / (acerto + falha)) * 100

    print(f'Taxa de acerto: {taxa_acerto:.2f}%')
    print(f'Taxa de erro: {taxa_erro:.2f}%\n')


# Lê a opção do menu de opções
def ler_str(dado):
    try:
        string = input(dado + ': ')
        if len(string) == 0: return None
        if len(string) > 0: return string
    except IOError:
        print('\nErro na leitura do dado: ' + dado)
    except KeyboardInterrupt:
        print("\nEntrada do usuário interrompida. O programa será encerrado.")
    return None
