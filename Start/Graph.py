import sys
import os

class Graph:
    def __init__(self,u,y):
        self.U = u 
        self.Y = y
        self.setGraph(u,y)

    def setGraph(u,y):
        i =0
        for j in range(0,self.U):
            for k in range(0,self.Y):
             Coordinates[i]=u+"," +y
             i+=1

    Coordinates=[]
    U=0
    Y=0