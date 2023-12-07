import heapq
import pygame
import sys
import random
import networkx as nx
from Pared import Pared
from Objetivo import ghost,Cereza,Pastilla
from Punto import PuntoAmarillo


class Mapa:
    def __init__(self):
        self.vec_paredes = []
        self.vec_obj = []
        self.G=None
        self.scale=30
        self.node_10 = None
        self.node_20 = None
        self.ruta_corta =None
        
        
    def selec_mapa(self,tipo,can_fantasmas,can_cerezas,can_pastas):
        if tipo==1:
            map = [
                [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  # 1
                [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],  # 2
                [7, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 1, 7],  # 3
                [7, 1, 15, 1, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15, 1, 15, 1, 7],  # 4
                [7, 1, 15, 1, 15, 15, 15, 15, 15, 1, 15, 1, 15, 15, 15, 15, 15, 1, 15, 1, 7],  # 5
                [7, 1, 15, 1, 1, 1, 1, 1, 15, 1, 15, 1, 15, 1, 1, 1, 1, 1, 15, 1, 7],  # 6
                [7, 1, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 15, 15, 15, 1, 7],  # 7
                [7, 1, 1, 1, 15, 1, 1, 1, 1, 1, 15, 1, 1, 1, 1, 1, 15, 1, 1, 1, 7],  # 8
                [7, 1, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 15, 15, 15, 1, 7],  # 9
                [7, 1, 15, 1, 15, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 15, 1, 15, 1, 7],  # 10
                [7, 10, 15, 1, 15, 15, 15, 1, 15, 1, 15, 1, 15, 1, 15, 15, 15, 1, 15, 20, 7],  # 11
                [7, 1, 15, 1, 15, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 15, 1, 15, 1, 7],  # 12
                [7, 1, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 15, 15, 15, 1, 7],  # 13
                [7, 1, 1, 1, 15, 1, 1, 1, 1, 1, 15, 1, 1, 1, 1, 1, 15, 1, 1, 1, 7],  # 14
                [7, 1, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 15, 15, 15, 1, 7],  # 15
                [7, 1, 15, 1, 1, 1, 1, 1, 15, 1, 15, 1, 15, 1, 1, 1, 1, 1, 15, 1, 7],  # 16
                [7, 1, 15, 1, 15, 15, 15, 15, 15, 1, 15, 1, 15, 15, 15, 15, 15, 1, 15, 1, 7],  # 17
                [7, 1, 15, 1, 15, 1, 1, 1, 1, 1, 1, 1, 15, 1, 1, 1, 15, 1, 1, 1, 7],  # 18
                [7, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 1, 7],  # 19
                [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],  # 20
                [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  # 21
            ]
        else:
            map = [
                #1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20   21
                [7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7], #1
                [7 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 7], #2
                [7 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 7], #3
                [7 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 7], #4
                [7 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 7], #5
                [7 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 7], #6
                [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #7
                [7 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 7], #8
                [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #9
                [7 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 7], #10
                [7 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 7], #11
                [7 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 7], #12
                [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #13 
                [7 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 7], #14
                [7 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 7], #15
                [7 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 7], #16
                [7 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 7], #17
                [7 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 1 , 7], #18
                [7 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 7], #19
                [7 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 7], #20
                [7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7], #21
            ]
        #agregar objetivos
        
        cont=0
        while cont<can_fantasmas:
            j= random.randint(2,18)
            k= random.randint(2,18)
            if map[j][k]==15:
                map[j][k]=100
                cont+=1
            
        
        cont2=0
        while cont2<=can_cerezas:
            j= random.randint(2,18)
            k= random.randint(2,18)
            if map[j][k]==15:
                map[j][k]=0
                cont2+=1
        
        cont3=0
        while cont3<=can_pastas:
            j= random.randint(2,18)
            k= random.randint(2,18)
            if map[j][k]==15:
                map[j][k]=8
                cont3+=1
        
        self.codificar_mapa(map)
        
    

    def codificar_mapa(self, mapa):
        for row_index, row in enumerate(mapa):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    pared = Pared(col_index * 30, row_index * 30, 30, 30)
                    self.vec_paredes.append(pared)

                if cell == 15:
                    Punto = PuntoAmarillo(col_index * 30, row_index * 30)
                    self.vec_obj.append(Punto)

                if cell == 100:
                    ghost1 = ghost(col_index * 30, row_index * 30, 26, 26)
                    self.vec_obj.append(ghost1)
                    # Agrega un nodo extra para el fantasma
                    
                if cell == 0:
                    cerezas = Cereza(col_index * 30, row_index * 30, 27, 28)
                    self.vec_obj.append(cerezas)
                    # Agrega un nodo extra para la cereza
                    

                if cell == 8:
                    pasta = Pastilla(col_index * 30, row_index * 30, 30, 30)
                    self.vec_obj.append(pasta)
                    # Agrega un nodo extra para la pastilla
                    
                

        self.construir_grafo(mapa)

    def construir_grafo(self, map):
        self.G = nx.Graph()
        for i, row in enumerate(map):
            for j, tile in enumerate(row):
                if tile not in [1, 7]:
                    self.G.add_node((i, j))
        
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] not in [1, 7]:
                    # Conectar con nodos adyacentes
                    if i > 0 and map[i - 1][j] not in [1, 7]:
                        self.G.add_edge((i, j), (i - 1, j), weight=map[i][j])
                    if i < len(map) - 1 and map[i + 1][j] not in [1, 7]:
                        self.G.add_edge((i, j), (i + 1, j), weight=map[i][j])
                    if j > 0 and map[i][j - 1] not in [1, 7]:
                        self.G.add_edge((i, j), (i, j - 1), weight=map[i][j])
                    if j < len(map[0]) - 1 and map[i][j + 1] not in [1, 7]:
                        self.G.add_edge((i, j), (i, j + 1), weight=map[i][j])
        
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 10:
                    self.node_10 = (i, j)
                elif map[i][j] == 20:
                    self.node_20 = (i, j)
        
        if self.node_10 and self.node_20:
            self.ruta_corta = self.dijkstra(self.G, self.node_10, self.node_20)

    def dijkstra(self, G, start, end):
        dist = {node: float("inf") for node in G.nodes}
        prev = {node: None for node in G.nodes}

        dist[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > dist[current_node]:
                continue

            for neighbor, edge_data in G[current_node].items():
                weight = edge_data.get('weight', 1)
                distance = current_distance + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Reconstruir la ruta
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = prev[current]

        return path
    

    def draw(self):
            pygame.init()
            ventana = pygame.display.set_mode((630, 630))
            pygame.display.set_caption("Nueva Ventana")

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                ventana.fill((0, 0, 0))  # Limpia la pantalla en cada frame

                for pared in self.vec_paredes:
                    pared.draw(ventana)

                for objetivo in self.vec_obj:
                    objetivo.draw(ventana)

                for edge in self.G.edges:
                    pygame.draw.line(ventana, (10, 230, 20), (edge[0][1] * 30 + 15, edge[0][0] * 30 + 15),
                                    (edge[1][1] * 30 + 15, edge[1][0] * 30 + 15), 2)
                if self.ruta_corta:
                    for i in range(len(self.ruta_corta) - 1):
                        pygame.draw.line(ventana, (240, 0, 0), (self.ruta_corta[i][1] * 30 + 15, self.ruta_corta[i][0] * 30 + 15),
                                        (self.ruta_corta[i + 1][1] * 30 + 15, self.ruta_corta[i + 1][0] * 30 + 15), 2)
                pygame.display.flip()

            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    mapa = Mapa()
    mapa.selec_mapa(1, 3, 5, 2)

    inicio = (1, 10)  # Coordenadas del inicio
    fin = (19, 10)  # Coordenadas del fin

    mapa.draw()