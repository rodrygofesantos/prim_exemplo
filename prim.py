import heapq

def prim(graph, start):
    # Inicialização
    mst = []  # Árvore Geradora Mínima
    visited = set()
    min_heap = []

    # Começa pelo vértice raiz com custo 0
    heapq.heappush(min_heap, (0, start, None))  # (peso, atual, pai)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue
        visited.add(current)

        # Se não for a raiz, adiciona à árvore
        if parent is not None:
            mst.append((parent, current, weight))

        # Percorre os vizinhos
        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))
    return mst

# Grafo do exercício
grafo = {
    's': [('a', 2), ('b', 6), ('d', 7)],
    'a': [('s', 2), ('b', 6), ('d', 8)],
    'b': [('s', 6), ('a', 6), ('c', 5), ('d', 4)],
    'c': [('b', 5), ('d', 9)],
    'd': [('s', 7), ('a', 8), ('b', 4), ('c', 9)]
}

# Executando o algoritmo a partir do vértice 's'
resultado = prim(grafo, 's')

# Imprimindo o resultado
print("Árvore Geradora Mínima (Prim):")
custo_total = 0
for u, v, peso in resultado:
    print(f"{u} - {v} (peso {peso})")
    custo_total += peso

print(f"Custo total: {custo_total}")