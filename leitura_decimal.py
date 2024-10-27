from service import *

# Recebe um numero decimal, que é convetido para binário e em seguida
# separa o endereço recebido em tag, s, d e w
# através da função strip, divide o endereço em 1 caractere por posição,
# onde o [valor_inicial:valor_final] define as posições que serão atribuidas as respesctivas váriaveis do dicionário
# e o int(valor, base) converte os valores de binário para decimal
def processa_decimal(endereco_decimal, mp, tamanho_endereco, cache):
    endereco_bin = decimal_para_binario(endereco_decimal, tamanho_endereco)
    infos_endereço = {
        'linha_mp': int(endereco_bin, 2),
        'tag': endereco_bin.strip()[:cache.tag],
        's': int(endereco_bin.strip()[:mp.s], 2),
        'd': int(endereco_bin.strip()[cache.tag:mp.s], 2),
        'w': int(endereco_bin.strip()[mp.s:], 2),
    }
    return infos_endereço


# Convertendo para binário com zero à esquerda para completar o tamanho do endereço
def decimal_para_binario(numero_decimal, num_bits):
    formato = '{:0' + str(num_bits) + 'b}'
    numero_binario = formato.format(numero_decimal)
    return numero_binario

# Le um numero decimal do usuário, faz verificações sobre ele
def input_decimal(quantidade_de_linhas):
    try:
        endereco_decimal = int(input(f'Digite um endereço decimal até {quantidade_de_linhas - 1}: '))
        # Verificar se está dentro dos limites
        if 0 <= endereco_decimal < quantidade_de_linhas:
            return endereco_decimal
        else:
            print(f'\nEndereço fora dos limites, tente novamente.\n')
            return None
    except ValueError:
        print('\nEntrada inválida. Por favor, insira um número inteiro.\n')
        return None

