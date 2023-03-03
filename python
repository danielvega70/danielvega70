pyhton
from turtle import *
import time
import queue
import random
def crear_Matriz(n , m):##Creo matriz
    matrix2=[]
    for i in range(n):
        matrix2.append([])
        for j in range(m):
            matrix2[i].append(0)
    return matrix2

class Agente:
    def __init__(self):
        self.env = Enviroment(5,5,0.12)
        agent_pos = True
        self.init_posX = random.randint(0, 4)  ## verificar que no haya ninguna pared
        self.init_posY = random.randint(0, 4)
        while(agent_pos):
            if(self.env.is_coalicion(self.init_posY,self.init_posX)):
                self.init_posX = random.randint(0, 4)  ## verificar que no haya ninguna pared
                self.init_posY = random.randint(0, 4)
            else:
                self.env.e[self.init_posY][self.init_posX] = "A" ## Y modifica la altura y X movimiento horizontal
                break
        self.env.print_Matriz()
        self.think()
    def get_posX(self):
        return self.init_posX
    def get_posY(self):
        return self.init_posY
    def changePos(self):
        self.init_posX = random.randint(0,4)
        self.init_posY = random.randint(0,4)
    def heuristica(self,goal , nuevo_nodo):
        return (goal[0]-nuevo_nodo[0]) + (goal[1] - nuevo_nodo[1])

    def pintarVecinos(self,vecinos,recorrido):
        for i in range(len(vecinos)):
            if not vecinos[i] in recorrido:
                (x,y) = vecinos[i]
                self.env.e[x][y] = "V"
        self.env.print_Matriz()
    def think(self):
        fronteras = queue.PriorityQueue()
        fronteras.put((self.get_posY(),self.get_posX()),0)
        recorrido = {}
        recorrido[(self.init_posY,self.init_posX)] = True
        costo = {}
        costo[(self.init_posY,self.init_posX)] = 0
        print("el nodo ganador esta en ",self.env.getGoal())

        while not fronteras.empty() :
            current = fronteras.get()
            goal = self.env.getGoal()

            if(current[0] == goal[0] and current[1] == goal[1]):
                break
            vecinos=[]
            vecinos = self.env.devolver_vecinos(current[1],current[0])
            print("Cantidad de vecinos ",len(vecinos))
            self.pintarVecinos(vecinos,recorrido)
            for i in range (len(vecinos)):
                nuevo_costo = costo[current] + 1
                if vecinos[i] not in recorrido or nuevo_costo < costo[vecinos[i]] :
                    costo[vecinos[i]] = nuevo_costo
                    prioridad = nuevo_costo + self.heuristica(self.env.getGoal(),vecinos[i])
                    fronteras.put(vecinos[i],prioridad)
                    recorrido[vecinos[i]] = True




class Enviroment:
    def __init__(self,n,m,rate):
        self.e = crear_Matriz(n,m)
        self.n = n
        self.m = m
        self.goal_x = 0
        self.goal_y = 0
        self.llenar_matriz(rate*n*m)
    def is_coalicion(self,x,y):
        if(self.e[x][y] == 1 ):
            return True
    def devolver_vecinos(self,x,y):
        vecinos=[]
        if(x + 1 <= self.m - 1 and  self.e[y][x+1] != 1):
            vecinos.append((y,x+1))
        if(x - 1 >= 0 and self.e[y][x-1] != 1):
            vecinos.append((y,x-1))
        if(y + 1 <= self.n -1 and self.e[y+1][x] != 1):
            vecinos.append((y+1,x))
        if(y -1 >= 0 and self.e[y-1][x] != 1 ):
            vecinos.append((y-1,x))
        return vecinos
    def llenar_matriz(self,rate):
        count = 0
        while(count < rate):## Lleno de obstaculos
            x = random.randint(0 , self.m -1 )
            y = random.randint(0 , self.n -1 )
            if(self.e[y][x] != 1 ):
                self.e[y][x] = 1
                count+=1
            else :
                continue
        meta = True
        while(meta):
            x = random.randint(0, self.m - 1)
            y = random.randint(0, self.n - 1)
            if(self.e[y][x] != 1):
                self.e[y][x] = "X"
                self.goal_y = y
                self.goal_x = x
                meta = False

    def print_Matriz(self):
        print("----------------------------------------------")
        print("----------------------------------------------")
        for i in range(self.n):
            print("[", end=" ")
            for j in range(self.m):
                print(self.e[i][j], end=" ")
            print("]")
    def getGoal(self):
        return (self.goal_y,self.goal_x )
a = Agente()
if = print (scale 50)
textinput =InterruptedError
mainloop(GeneratorExit)
if = print (scale 50)
textinput = interrupt (scale 50)
breakpoint with window_height = 50
