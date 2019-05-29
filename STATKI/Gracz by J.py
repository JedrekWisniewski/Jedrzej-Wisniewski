"""Gracz"""
#KOORDYNATY PODAWANE SĄ NAJPIERW PIONOWO , POTEM POZIOMO, czyli Y a potem X
import numpy as np
import sys
import random as r



def wczytywanie(nazwapliku="Gracz1.npy"):
    mymap = np.load(nazwapliku)
    return mymap
    #enemymap tez bedzie
class Czteromaszt():
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -1
            return "4t"
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -1
            return "4t"
        elif enemyfire == self.c:
            print("Trafiony")
            self.c = -1
            return "4t"
        elif enemyfire == self.d:
            print("Trafiony")
            self.d = -1
            return "4t"
        if self.a == -1 and self.b == -1 and self.c == -1 and self.d == -1:
            self.a = "już zatopiony"
            print ("Czteromasztowiec zatopiony")
            return "4z"
            
    
class Trojmaszt():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -1
            return "3t"
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -1
            return "3t"
        elif enemyfire == self.c:
            print("Trafiony")
            self.c = -1
            return "3t"
        if self.a == -1 and self.b == -1 and self.c == -1:
            self.a = "już zatopiony"
            print("Zatopiony trójmasztowiec")
            return "3z"

class Dwumaszt():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -1
            return "2t"
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -1
            return "2t"
        if self.a == -1 and self.b == -1:
            self.a = "już zatopiony"
            print("Zatopiony dwumasztowiec")
            return "2z"

class Jednomaszt():
    def __init__(self,a):
        self.a = a
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print ("Trafiony")
            self.a = -1
            return "1t"
        if self.a == -1:
            self.a = "już zatopiony"
            print ("Zatopiony jednomasztowiec")
            return "1z"

def tworzenie():
    #czteromasztowiec
    y,x = np.where(mymap == 4)
    cztm = Czteromaszt((y[0],x[0]),(y[1],x[1]),(y[2],x[2]),(y[3],x[3]))
    #trójmasztowce
    y,x = np.where(mymap == 3)
    trz1 = Trojmaszt((y[0],x[0]),(y[1],x[1]),(y[2],x[2]))
    trz2 = Trojmaszt((y[3],x[3]),(y[4],x[4]),(y[5],x[5]))
    #dwumasztowce
    y,x = np.where(mymap == 2)
    dwu1 = Dwumaszt((y[0],x[0]),(y[1],x[1]))
    dwu2 = Dwumaszt((y[2],x[2]),(y[3],x[3]))
    dwu3 = Dwumaszt((y[4],x[4]),(y[5],x[5]))
    #jednomasztowce
    y,x = np.where(mymap == 1)
    jed1 = Jednomaszt((y[0],x[0]))
    jed2 = Jednomaszt((y[1],x[1]))
    jed3 = Jednomaszt((y[2],x[2]))
    jed4 = Jednomaszt((y[3],x[3]))
    return cztm ,trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4

#Lista w której zapisywane są koordynaty strzałów            
ourshots = []
#Strzał losowy, koordynaty
def random_shoot():
    strzalpoz = r.randint(0,9)
    strzalpion = r.randint(0,9)
    return strzalpion, strzalpoz

#Sprawdza czy strzał dozwolony, jeśli tak, wypluwa koordynaty , a strzał zapisuje do listy
def fire():    
    x = random_shoot()
    if x in ourshots:
        return fire()
    else:
        ourshots.append(x)
        return x

# Iteruje po każdym statku, wywołując metodę "trafiony" względem "enemyfire"=koordynatów
def obrywamy(enemyfire):
    for statek in flota:
        statek.trafiony(enemyfire)
    if mymap[enemyfire] == 0:
        print ("Pudło")
        return "p"

#TESTY######
def test(strzaltest = 10):
    for i in range(strzaltest):
        print("strzelam")
        x = fire()
        print(x)
        obrywamy(x)

#Wczytanie, stworzenie statków, dodanie do floty
mymap = wczytywanie()
cztm, trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4 = tworzenie()
flota = [cztm, trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4]

czytrafione = []
pierwszenstwo = sys.argv[1]
def wielka_gra():    
    if pierwszenstwo == "s":
        fire()
        czytrafione.append(input())
        enemyfire = input()
        obrywamy(enemyfire)
        if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
            return 1
    else:
        enemyfire = input()
        obrywamy(enemyfire)
        fire()
        czytrafione.append(input())
        if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
            return 1

while wielka_gra() != 0:
    wielka_gra()
