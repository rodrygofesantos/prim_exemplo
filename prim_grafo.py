import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph, start):
    mst = []  # Árvore Geradora Mínima
    visited = set()
    min_heap = []

    heapq.heappush(min_heap, (0, start, None))  # (peso, atual, pai)

    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)

        if current in visited:
            continue
        visited.add(current)

        if parent is not None:
            mst.append((parent, current, weight))

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))
    return mst

# Grafo original
grafo = {
    's': [('a', 2), ('b', 6), ('d', 7)],
    'a': [('s', 2), ('b', 6), ('d', 8)],
    'b': [('s', 6), ('a', 6), ('c', 5), ('d', 4)],
    'c': [('b', 5), ('d', 9)],
    'd': [('s', 7), ('a', 8), ('b', 4), ('c', 9)]
}

# Executa Prim
resultado = prim(grafo, 's')

# Cria o grafo original no NetworkX
G = nx.Graph()
for u in grafo:
    for v, peso in grafo[u]:
        G.add_edge(u, v, weight=peso)

# Cria o grafo da AGM
MST = nx.Graph()
for u, v, peso in resultado:
    MST.add_edge(u, v, weight=peso)

# Layout do grafo
pos = nx.spring_layout(G, seed=42)

# Desenha o grafo original com pesos
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=12)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo Original")

# Desenha a AGM
plt.subplot(1, 2, 2)
nx.draw(MST, pos, with_labels=True, node_color='lightgreen', edge_color='red', node_size=1000, font_size=12)
labels_mst = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels_mst)
plt.title("Árvore Geradora Mínima (Prim)")

plt.tight_layout()
plt.show()

# Imprime o resultado
print("Árvore Geradora Mínima (Prim):")
custo_total = 0
for u, v, peso in resultado:
    print(f"{u} - {v} (peso {peso})")
    custo_total += peso

print(f"Custo total: {custo_total}")
