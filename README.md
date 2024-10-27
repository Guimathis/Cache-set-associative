# Trabalho de Arquitetura e Organização de Computadores

Projeto, desenvolvido em Python, visa simular uma memória cache set-associative e uma memória principal,
com o objetivo de compreender suas interações e funcionamento.

**Alunos: Guilherme Mathias Silva Gomes, Thiago Henrique Aparecido Ferreira**

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e diretórios:


- `loop_de_execuções.py`: Loop de execução, integra as funcionalidades da cache e da memória principal.
- `service.py`: Funções que lidam com cálculos sobre os dados da cache e memória principal.
- `cache.py`: Implementação da memória cache.
- `memoria_principal.py`: Implementação da memória principal.
- `processar_arquivos.py`: Implementação de funções que lidam com arquivos de dados sobre a memória cache e MP.
- `leitura_decimais.py`: Implementação de funções que lidam com a leitura de numeros decimais e conversões para binário.
- `infos.txt`: Arquivo com as informações sobre memória principal e memória cache. 
   Possui as informações necessárias para a instanciação da mp e cache(siga as instruções dentro do arquivo).
- `enderecos.txt`: Arquivo para se preenchido com endereços, para simular uma cache cheia e colocar o algoritmo
    lfu em prática. 

## Como Executar

Para executar o projeto, siga os passos abaixo:


 - Configure um interpretador Python compatível com o projeto (recomenda-se usar uma versão recente do Python 3).
 - Execute a partir na main em `loop_de_execuções.py` para iniciar a simulação.

## Observações

  - Necessita da instalação da biblioteca NumPy(pip install numpy).
  - Arquivo infos e enderecos ja estão preenchidos valores para execução e teste do simulador, 
    mas podem ser alterados para quaisquer valores dentro dos limites de tamanho



