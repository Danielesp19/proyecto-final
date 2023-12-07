import pygame
import sys
import networkx as nx

# Crear el grafo y agregar nodos desde la matriz
G = nx.Graph()

mapa_lab = [
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  #1
    [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],  #2
    [7, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 7],  #3
    [7, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 7],  #4
    [7, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 3, 1, 0, 1, 7],  #5
    [7, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 7],  #6
    [7, 1, 0, 0, 0, 1, 0, 0, 0, 2, 3, 0, 0, 0, 0, 1, 2, 0, 4, 1, 7],  #7
    [7, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 7],  #8
    [7, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 7],  #9
    [7, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 7],  #10
    [7, 10, 0, 1, 0, 3, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 20, 7],  #11
    [7, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 7],  #12
    [7, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 7],  #13
    [7, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 7],  #14
    [7, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 4, 1, 7],  #15
    [7, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 7],  #16
    [7, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 7],  #17
    [7, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 7],  #18
    [7, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 7],  #19
    [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],  #20
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  #21
]

# Agregar nodos al grafo
for i in range(len(mapa_lab)):
    for j in range(len(mapa_lab[0])):
        if mapa_lab[i][j] not in [1, 7]:
            G.add_node((i, j))

# Conectar nodos adyacentes en el grafo
for i in range(len(mapa_lab)):
    for j in range(len(mapa_lab[0])):
        if mapa_lab[i][j] not in [1, 7]:
            # Conectar con nodos adyacentes
            if i > 0 and mapa_lab[i - 1][j] not in [1, 7]:
                G.add_edge((i, j), (i - 1, j), weight=mapa_lab[i][j])
            if i < len(mapa_lab) - 1 and mapa_lab[i + 1][j] not in [1, 7]:
                G.add_edge((i, j), (i + 1, j), weight=mapa_lab[i][j])
            if j > 0 and mapa_lab[i][j - 1] not in [1, 7]:
                G.add_edge((i, j), (i, j - 1), weight=mapa_lab[i][j])
            if j < len(mapa_lab[0]) - 1 and mapa_lab[i][j + 1] not in [1, 7]:
                G.add_edge((i, j), (i, j + 1), weight=mapa_lab[i][j])

    
# Find the nodes for 10 and 20
node_10 = None
node_20 = None
for i in range(len(mapa_lab)):
    for j in range(len(mapa_lab[0])):
        if mapa_lab[i][j] == 10:
            node_10 = (i, j)
        elif mapa_lab[i][j] == 20:
            node_20 = (i, j)

# Encontrar la ruta más corta desde 10 hasta 20
if node_10 and node_20:
    ruta_corta = nx.shortest_path(G, source=node_10, target=node_20)
else:
    print("No nodes for 10 and/or 20 found in the graph.")

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana
window_size = (630, 630)
ventana = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grafo en Pygame")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    ventana.fill((255, 255, 255))

    # Dibujar nodos
    for i in range(len(mapa_lab)):
        for j in range(len(mapa_lab[0])):
            if mapa_lab[i][j] not in [1, 7]:
                pygame.draw.circle(ventana, (255, 0, 0), (j * 30 + 15, i * 30 + 15), 10)

    # Dibujar las aristas del grafo
    for edge in G.edges:
        pygame.draw.line(ventana, (0, 0, 0), (edge[0][1] * 30 + 15, edge[0][0] * 30 + 15),
                         (edge[1][1] * 30 + 15, edge[1][0] * 30 + 15), 2)
    if ruta_corta:
        for i in range(len(ruta_corta) - 1):
            pygame.draw.line(ventana, (0, 255, 0), (ruta_corta[i][1] * 30 + 15, ruta_corta[i][0] * 30 + 15),
                             (ruta_corta[i + 1][1] * 30 + 15, ruta_corta[i + 1][0] * 30 + 15), 2)
    pygame.display.flip()
