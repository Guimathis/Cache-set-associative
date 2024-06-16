# Biblioteca para lidar com vetores e numeros aleatórios, **NECESSITA pip install NumPy**
import numpy as np

# Códigos de cores para alterar cores no terminal
RESET = "\033[0m"
BLUE = "\033[34m"


# Classe para definir a mp e guardar todos os seus atributos em um objeto
# usa a biblioteca numPy para declarar um vetor com o tamanho da memória e
# preenche-lo com numeros inteiros aleatórios
class MemoriaPrincipal:
    def __init__(self, tamanho, palavras_por_bloco, quantidade_linhas, quantidade_blocos, w, s, tamanho_endereco):
        self.tamanho = tamanho
        self.palavras_por_bloco = palavras_por_bloco
        self.quantidade_de_linhas = quantidade_linhas
        self.quantidade_de_blocos = quantidade_blocos
        self.w = w
        self.s = s
        self.tamanho_do_endereco = tamanho_endereco
        self.memoriaPrincipal = np.random.randint(100, 99999 + 1, self.quantidade_de_linhas)

    def __str__(self):
        return (f"Informações da Memoria Principal: "
                f"{BLUE}\nTamanho da memória(kb): {RESET}{self.tamanho} "
                f"{BLUE}\nPalavras por bloco: {RESET}{self.palavras_por_bloco} "
                f"{BLUE}\nQuantidade de linhas: {RESET}{self.quantidade_de_linhas} "
                f"{BLUE}\nQuantidade de blocos: {RESET}{self.quantidade_de_blocos} "
                f"{BLUE}\nBits para word: {RESET}{self.w} "
                f"{BLUE}\nBits para s: {RESET}{self.s} "
                f"{BLUE}\nTamanho do endereço: {RESET}{self.tamanho_do_endereco} \n")

    # imprime a memória principal na tela
    def imprimir_memoria(self):
        print(f'{BLUE}Memória Principal:{RESET}')
        for i in range(self.quantidade_de_blocos):
            blocoInicio = i * self.palavras_por_bloco
            blocoFim = blocoInicio + self.palavras_por_bloco
            bloco = self.memoriaPrincipal[blocoInicio:blocoFim]
            print(f"Bloco {i}: {bloco}")