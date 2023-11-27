import pygame
import sys
import random
from Pared import Pared
from Objetivo import ghost
from Punto import PuntoAmarillo

class Mapa:
    def __init__(self):
        self.vec_paredes = []
        self.vec_puntos = []
        self.vec_obj = []

    def selec_mapa(self,tipo,can_fantasmas,can_cerezas,can_pastas):
        
        if tipo==1:
            mapa_lab = [
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
        else:
            mapa_lab = [
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
            if mapa_lab[j][k]==0:
                mapa_lab[j][k]=3
                cont+=1
            
        """
        cont2=0
        while cont2<=can_cerezas:
            j= random.randint(2,18)
            k= random.randint(2,18)
            if mapa_lab[j][k]==0:
                mapa_lab[j][k]=4
                cont2+=1
        
        cont3=0
        while cont3<=can_pastas:
            j= random.randint(2,18)
            k= random.randint(2,18)
            if mapa_lab[j][k]==0:
                mapa_lab[j][k]=5
                cont3+=1
        """
        self.codificar_mapa(mapa_lab)

    #crea los objetos
    def codificar_mapa(self, mapa):
        
        for row_index, row in enumerate(mapa):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    pared = Pared(col_index * 30, row_index * 30, 30, 30)
                    self.vec_paredes.append(pared)
                
                if cell==0:
                    Punto=PuntoAmarillo(col_index * 30, row_index * 30)
                    self.vec_puntos.append(Punto)

                if cell == 3:
                    ghosts = ghost(col_index * 30, row_index * 30, 30, 30)
                    self.vec_obj.append(ghosts)
                """"
                if cell == 4:
                    cerezas = ghost(col_index * 30, row_index * 30, 30, 30)
                    self.vec_paredes.append(cerezas)

                if cell == 5:
                    ghosts = ghost(col_index * 30, row_index * 30, 30, 30)
                    self.vec_paredes.append(ghosts)
                """


    def draw(self):
        pygame.init()
        ventana = pygame.display.set_mode((630, 630))
        pygame.display.set_caption("Nueva Ventana")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for pared in self.vec_paredes:
                pared.draw(ventana)
            for puntos in self.vec_obj:
                puntos.draw(ventana)
            for ghost in self.vec_obj:
                ghost.draw(ventana)
            pygame.display.flip()
