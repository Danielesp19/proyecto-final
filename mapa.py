import heapq
import pygame
import sys
import random
import heapq
import networkx as nx
from Pared import Pared
from Objetivo import Pacman, ghost,Cereza,Pastilla
from Punto import PuntoAmarillo


class Mapa:
    def __init__(self):
        self.vec_paredes = []
        self.vec_obj = []
        self.G=None
        self.scale=30
        Inicial = None
        Final = None
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
                [7, 1, 15, 1, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 15, 1, 15, 1, 7],  # 18
                [7, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 1, 7],  # 19
                [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],  # 20
                [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],  # 21
            ]
        if tipo==2:
            map = [
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
            [7, 1, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 15, 15, 15, 1, 7],
            [7, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 7],
            [7, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 1, 7],
            [7, 1, 1, 1, 15, 1, 1, 1, 1, 1, 15, 1, 1, 1, 1, 1, 15, 1, 1, 1, 7],
            [7, 1, 15, 15, 15, 15, 15, 15, 15, 1, 15, 1, 15, 15, 15, 15, 15, 15, 15, 1, 7],
            [7, 1, 15, 1, 1, 1, 1, 1, 15, 1, 15, 1, 15, 1, 1, 1, 1, 1, 15, 1, 7],
            [7, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 7],
            [7, 1, 15, 1, 1, 1, 1, 1, 1, 1, 15, 1, 1, 1, 1, 1, 1, 1, 15, 1, 7],
            [7, 10, 15, 15, 15, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 15, 15, 20, 7],
            [7, 1, 15, 1, 1, 1, 1, 1, 1, 1, 15, 1, 1, 1, 1, 1, 1, 1, 15, 1, 7],
            [7, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 7],
            [7, 1, 15, 1, 1, 1, 1, 1, 15, 1, 15, 1, 15, 1, 1, 1, 1, 1, 15, 1, 7],
            [7, 1, 15, 1, 15, 15, 15, 15, 15, 1, 15, 1, 15, 15, 15, 15, 15, 1, 15, 1, 7],
            [7, 1, 15, 1, 15, 1, 1, 1, 1, 1, 15, 1, 1, 1, 1, 1, 15, 1, 15, 1, 7],
            [7, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 1, 15, 15, 15, 15, 15, 1, 7],
            [7, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 1, 1, 15, 1, 7],
            [7, 1, 15, 15, 15, 1, 15, 15, 15, 15, 15, 15, 15, 15, 15, 1, 15, 15, 15, 1, 7],
            [7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
        ]
    

            
        #agregar objetivos
        if can_cerezas != 0 and can_fantasmas != 0 and can_pastas != 0:
            cont=0
            while cont<can_fantasmas:
                j= random.randint(2,18)
                k= random.randint(2,18)
                if map[j][k]==15:
                    map[j][k]=300
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

                if cell == 300:
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

                if cell == 10:
                    pasta = Pacman(col_index * 30, row_index * 30, 30, 30)
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
                    Inicial = (i, j)
                elif map[i][j] == 20:
                    Final = (i, j)
        
        if Inicial and Final:
            self.encontrar_y_dibujar_caminos(Inicial, Final)
            self.ruta_corta = self.dijkstra(self.G, Inicial, Final)

    def dijkstra(self, G, start, end):
        dist = {node: float("inf") for node in G.nodes}
        prev = {node: None for node in G.nodes}

        dist[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

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
    
    def find_all_paths(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            self.all_paths.append(path.copy())
        if start not in graph:
            return
        for node in graph[start]:
            if node not in path:
                self.find_all_paths(graph, node, end, path)

    def encontrar_y_dibujar_caminos(self, start, end):
        self.all_paths = []
        self.find_all_paths(self.G, start, end)
        
    

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
                
                for path in self.all_paths:
                    for i in range(len(path) - 1):
                        pygame.draw.line(ventana, (0, 0, 240), (path[i][1] * 30 + 15, path[i][0] * 30 + 15),
                                        (path[i + 1][1] * 30 + 15, path[i + 1][0] * 30 + 15), 2)
                        
                if self.ruta_corta:
                    for i in range(len(self.ruta_corta) - 1):
                        pygame.draw.line(ventana, (240, 0, 0), (self.ruta_corta[i][1] * 30 + 15, self.ruta_corta[i][0] * 30 + 15),
                                        (self.ruta_corta[i + 1][1] * 30 + 15, self.ruta_corta[i + 1][0] * 30 + 15), 2) 
                
                pygame.display.flip()

            pygame.quit()
            sys.exit()


