# Biblioteca para lidar com vetores e numeros aleatórios, **NECESSITA pip install NumPy**
import numpy as np

import main
from main import *

# Códigos de cores para alterar cores no terminal
RESET = "\033[0m"
BLUE = "\033[34m"

# Classe cache com atributos para guardar as informações da cache em um objeto.
class Cache:
    def __init__(self, tamanhoCache, linhasPorConjunto, quantidadeConjuntos, quantidadeLinhas, d, tag):
        self.tamanhoCache = tamanhoCache
        self.linhasPorConjunto = linhasPorConjunto
        self.quantidadeConjuntos = quantidadeConjuntos
        self.quantidadeLinhas = quantidadeLinhas
        self.d = d
        self.tag = tag
        self.falha = 0
        self.acerto = 0
        self.cache = [[{'tag': None, 'bloco': None, 'cont': 0} for _ in range(self.linhasPorConjunto)] for _ in range(self.quantidadeConjuntos)]

    # Imprime a cache por completo, separada pelo número dos conjuntos
    def imprimir_cache(self):
        print(f'{BLUE}Conjuntos da Cache:{RESET}')
        for set_index, set_lines in enumerate(self.cache):
            print(f"Conjunto {set_index}: {set_lines}")

    def __str__(self):
        return ("\nInformações da cache: "
                f"{BLUE}\nTamanho da Cache(kb): {RESET}{self.tamanhoCache} "
                f"{BLUE}\nLinhas por Conjunto: {RESET}{self.linhasPorConjunto} "
                f"{BLUE}\nQuantidade de Conjuntos: {RESET}{self.quantidadeConjuntos} "
                f"{BLUE}\nQuantidade de linhas da cache: {RESET}{self.quantidadeLinhas} "
                f"{BLUE}\nBits para d: {RESET}{self.d} "
                f"{BLUE}\nBits para tag: {RESET}{self.tag}\n")


    # Imprime na tela o conjunto acessado, junto com o anterior e o posterior, se existir
    def imprimir_conjuntos(self, indice_cache):
        if indice_cache == 0:
            print(f'Acessando o 1° conjunto da cache:  {self.cache[indice_cache]}')
            print(f'Conjunto posterior:  {self.cache[indice_cache + 1]}')
        elif indice_cache == self.quantidadeConjuntos - 1:
            print(f'Conjunto anterior:  {self.cache[indice_cache - 1]}')
            print(f'Acessando o ultimo conjunto da cache:  {self.cache[indice_cache]}')
        else:
            print(f'Conjunto anterior:  {self.cache[indice_cache - 1]}')
            print(f'{indice_cache + 1}° conjunto acessado:  {self.cache[indice_cache]}')
            print(f'Conjunto posterior:  {self.cache[indice_cache + 1]}')

    #  obtem o índice do conjunto que o endereço inserido será mapeado
    def get_indice(self, bloco_mp):
        return bloco_mp % self.quantidadeConjuntos

    # Esta função cria uma lista chamada status onde são armazenados na posição [0]
    #  o resultado da busca do endereço na cache, e na posição [1] a linha em que o endereço será mapeado em caso de
    # linha vazia ou se o endereço já está na cache
    # Também imprime na tela o conjunto acessado, conjunto anterior e posterior, se existir
    def acessar_cache(self, endereco):
        status_pos = list()
        indice_cache = self.get_indice(endereco['s'])
        self.imprimir_conjuntos(indice_cache)
        for i, conjunto in enumerate(self.cache[indice_cache]):
            if conjunto['tag'] is None:
                status_pos.append(0)
                status_pos.append(int(i))
                return status_pos
            elif conjunto['tag'] == endereco['tag']:
                status_pos.append(1)
                status_pos.append(i)
                return status_pos
            elif conjunto['tag'] != endereco['tag']:
                pass
        status_pos.append(2)
        return status_pos

    # Função para colocar o bloco do endereço de entrada na memória cache
    # divide o 's' pela quantidade de palavras por bloco para encontrar o indice da primeira palavra do respectivo bloco
    # para que não seja preciso percorrer toda a memória até encontrar o bloco
    def buscar_na_memoria(self, memoria, endereço, linha):
        indices = endereço['s'] * memoria.palavras_por_bloco
        bloco = memoria.memoriaPrincipal[indices:indices + memoria.palavras_por_bloco]
        self.cache[endereço['d']][linha]['bloco'] = list(bloco)
        self.cache[endereço['d']][linha]['tag'] = endereço['tag']
        self.cache[endereço['d']][linha]['cont'] += 1

    # Função que recebe o endereço binário, processa e guarda num dicionário a linha da memória, tag, s, d e w
    # usa a função acessar_cache() para saber se o ocorreu falha ou acerto e se é necessário fazer substituição
    # analisa o retorno da função acessar_cache() e faz atribuições, alterações e incrementos se necessário,
    # também chama o LFU se o conjunto estiver cheio
    def acessar_endereço(self, endereço_bin, memoria_principal):
        endereço = main.processa_endereco(endereço_bin, memoria_principal, self)
        status_pos = self.acessar_cache(endereço)

        # se status_pos[0] = 0 significa que existe linha vazia na cache,
        # chama a função para buscar o bloco na memória e alocalo na posição vazia do conjunto salva em status_pos[1],
        # falha++
        if status_pos[0] == 0:
            self.falha += 1
            print(f'\nO endereço acessado não está na cache.\n')
            print(f'Alocando o bloco do endereço {endereço_bin} na cache:')
            self.buscar_na_memoria(memoria_principal, endereço, status_pos[1])
            print(f'Cache resultante:')
            self.imprimir_conjuntos(self.get_indice(endereço['s']))

        # se status_pos[0] = 1 significa que o endereço está na cache, acerto++
        elif status_pos[0] == 1:
            self.acerto += 1
            s = endereço['s']
            self.cache[self.get_indice(s)][status_pos[1]]['cont'] += 1
            print('\nO endereço acessado já está na cache.\n')
            print(f'Cache resultante: ')
            self.imprimir_conjuntos(self.get_indice(endereço['s']))

        # se status_pos[0] = 2 significa que o endereço não está na cache e que o conjunto está cheio,
        # chama o algoritmo lfu para fazer a substituição
        elif status_pos[0] == 2:
            print('Endereço não encontrado.\nCache cheia, chamando LFU')
            self.lfu(memoria_principal, endereço)

    # Função que implementa o algoritmo de subtituição por FLU(Least Frequently Used)
    def lfu(self, memoria_principal, endereco):
        indice_cache = self.get_indice(endereco['s'])
        lfu_index = 0
        cont_min = float('inf')

        for i, conjunto in enumerate(self.cache[indice_cache]):
            if conjunto['cont'] < cont_min:
                cont_min = conjunto['cont']
                lfu_index = i

        print(f'Substituindo a linha {lfu_index} do conjunto {indice_cache} (usada {cont_min} vezes)')
        # Busca o bloco na memória e substitui na cache
        self.buscar_na_memoria(memoria_principal, endereco, lfu_index)
        self.cache[endereco['d']][lfu_index]['cont'] = 1
        # Imprimi a cache após substituição com a chamada da função imprimir_conjuntos()
        print(f'\nCache após substituição:')
        self.imprimir_conjuntos(indice_cache)
