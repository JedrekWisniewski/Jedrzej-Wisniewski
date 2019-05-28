#Gracz

import numpy as np
import sys
import random as r

def wczytywanie(nazwapliku="Gracz1.npy"):
    mymap = np.load(nazwapliku)
    return mymap
    #enemymap tez bedzie
class Czteromasz():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -4
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -4
        elif enemyfire == self.c:
            print("Trafiony")
            self.c = -4
        elif enemyfire == self.d:
            print("Trafiony")
            self.d = -4
        if self.a == -4 and self.b == -4 and self.c == -4 and self.d == -4:
            print("Zatopiony czteromasztowiec")
            return
class Trojmaszt():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -3
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -3
        elif enemyfire == self.c:
            print("Trafiony")
            self.c = -3
        if self.a == -3 and self.b == -3 and self.c == -3:
            print("Zatopiony trójmasztowiec")
            return

class Dwumaszt():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -2
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -2
        if self.a == -2 and self.b == -2:
            print("Zatopiony dwumasztowiec")
            return

class Jednomaszt():
    def __init__(self,a):
        self.a = a
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print ("Trafiony")
            self.a = -1
        if self.a == -1:
            print ("Zatopiony jednomasztowiec")
            return

# Do dobrego sprawdzenia kiedy pion a kiedy poziom bo późno i spać sie chciało
def tworzenie():
    #czteromasztowiec
    y,x = np.where(mymap == 4)
    cztm = Czteromasz((x[0],y[0]),(x[1],y[1]),(x[2],y[2]),(x[3],y[3]))
    #trójmasztowce
    y,x = np.where(mymap == 3)
    trz1 = Trojmaszt((x[0],y[0]),(x[1],y[1]),(x[2],y[2]))
    trz2 = Trojmaszt((x[3],y[3]),(x[4],y[4]),(x[5],y[5]))
    #dwumasztowce
    y,x = np.where(mymap == 2)
    dwu1 = Dwumaszt((x[0],y[0]),(x[1],y[1]))
    dwu2 = Dwumaszt((x[2],y[2]),(x[3],y[3]))
    dwu3 = Dwumaszt((x[4],y[4]),(x[5],y[5]))
    #jednomasztowce
    y,x = np.where(mymap == 1)
    jed1 = Jednomaszt((x[0],y[0]))
    jed2 = Jednomaszt((x[1],y[1]))
    jed3 = Jednomaszt((x[2],y[2]))
    jed4 = Jednomaszt((x[3],y[3]))
    return cztm ,trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4
            
ourshots = []
def random_shoot():
    strzalpoz = r.randint(0,9)
    strzalpion = r.randint(0,9)
    return strzalpoz, strzalpion

def fire():    
    x = random_shoot()
    if x in ourshots:
        return fire()
    else:
        ourshots.append(x)
        return x
def obrywamy(enemyfire):
    for statek in flota:
        statek.trafiony(enemyfire)
    if mymap[enemyfire] == 0:
        print("pudło")

#TESTY######
def test(strzaltest = 10):
    for i in range(strzaltest):
        print("strzelam")
        x = fire()
        print(x)
        obrywamy(x)

mymap = wczytywanie()
cztm, trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4 = tworzenie()
flota = [cztm, trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4]
#test()

