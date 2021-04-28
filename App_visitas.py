
#importamos el conector del driver
from selenium import  webdriver
import time
from random import randrange

tiempo_vista = 10
lista_navegador = []

#Levanatamos 3 navegadores
navegador_1 = webdriver.Edge(executable_path='./msedgedriver.exe')
navegador_2 = webdriver.Edge(executable_path='./msedgedriver.exe')
navegador_3 = webdriver.Edge(executable_path='./msedgedriver.exe')

#Los agregamos a la lista
lista_navegador.append(navegador_1)
lista_navegador.append(navegador_2)
lista_navegador.append(navegador_3)

for navegador in lista_navegador:
    navegador.get('https://www.youtube.com/watch?v=5ZBgx1NeUWg')

while(True):
    numero_random = randrange(0,len(lista_navegador))
    lista_navegador[numero_random].refresh() #Refrescamos 
    print("Navegador Numero ", numero_random, "Se a actualizado")
    time.sleep(tiempo_vista) #Asignamos los 10 segundos de espera, de la variable