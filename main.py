import dados
import os
from time import sleep
from threading import Thread

diretorio = os.path.dirname(__file__)
nome_arquivo = input("Informe o grafo: ")
tempo_limite = int(input("Tempo limite (s): "))
my_file = open(diretorio + "/Datasets/" + nome_arquivo, "r")
content = my_file.read()
content_list = content.splitlines()
my_file.close()

numVertices, numArestas = content_list[0].split(" ")
content_list.pop(0)

grafo = dados.gerarGrafo(content_list)




t = Thread(target=dados.vizinho(grafo,int(numVertices)))
t.daemon = True
t.start()

sleep(tempo_limite)

