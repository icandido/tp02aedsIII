from time import time
from random import choice, randrange
from itertools import permutations, combinations
import numpy as np

def gerarGrafo(arquivo):
    keys = []
    values = []
    for line in arquivo:
        aux = line.split(" ")
        keys.append(aux[0] + ', ' + aux[1])
        values.append(float(aux[2]))
    
    grafo = dict(zip(keys, values))
    
    return grafo

def vizinho(grafo,numVertices):
    start = time()

    naoVisitados = [x for x in range(numVertices)]
    vertice = 0
    caminho = [vertice]
    dist = 0
    naoVisitados.remove(vertice)
    inverseGrafo = []

    for x in grafo:
        aux = x.split(", ")
        inverseGrafo.append(aux[1] + ", " + aux[0])
    teste = dict(zip(inverseGrafo, grafo.values()))
    z = grafo | teste

    while len(naoVisitados) != 0:
        aux = 9999999
        origem = caminho[len(caminho)-1]
        for x in z:
            teste = str.split(x,", ")
            if int(teste[0]) == origem and int(teste[1]) in naoVisitados: 
                if aux > z.get(x):
                    aux = z.get(x)
                    i = int(teste[1])
                
        dist = dist + aux

        caminho.append(i)
        naoVisitados.remove(i)
        vertice = i
    
    dist += z.get(str(caminho[len(caminho)-1]) + ', 0')
    caminho.append(0)
    print((time()-start))
    print(caminho)
