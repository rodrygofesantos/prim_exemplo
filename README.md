# Algoritmo de Prim em Python com Visualização Gráfica

Este projeto implementa o Algoritmo de Prim para construção de Árvores Geradoras Mínimas (AGM) em grafos ponderados e não direcionados, utilizando a linguagem Python. A aplicação inclui visualização do grafo original e da árvore geradora resultante com o apoio das bibliotecas NetworkX e Matplotlib.

## Autor

**Prof. Rodrigo Fernandes dos Santos**  
Professor do curso de Ciência da Computação  
Desenvolvido com fins didáticos para apoio ao ensino de Estrutura de Dados e Teoria dos Grafos.

## Objetivo

Demonstrar, de forma prática e visual, o funcionamento do algoritmo guloso de Prim na construção de árvores geradoras de custo mínimo. O projeto visa auxiliar na compreensão dos conceitos fundamentais de grafos por meio de programação aplicada.

## Requisitos

- Python 3.8 ou superior
- networkx >= 3.0
- matplotlib >= 3.5


Instale as dependências com:

```bash
pip install -r requirements.txt
```
## Estrutura do Código

- **`prim.py`**: script principal com a implementação do algoritmo e geração dos gráficos.
- **`requirements.txt`**: arquivo que lista as dependências necessárias para execução do projeto.

O grafo utilizado no algoritmo é representado por um **dicionário de adjacência**, no qual cada **chave** corresponde a um **vértice**, e o **valor associado** é uma **lista de tuplas**. Cada tupla representa um vértice vizinho e o peso da aresta que conecta os dois vértices.


