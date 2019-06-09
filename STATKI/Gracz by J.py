"""Gracz"""
#KOORDYNATY PODAWANE SĄ NAJPIERW PIONOWO , POTEM POZIOMO, czyli Y a potem X
import numpy as np
import sys
import random as r

ruchy = ["a01","a02","a03","a04","a05","a06","a07","a08","a09","a10",
         "b01","b02","b03","b04","b05","b06","b07","b08","b09","b10",
         "c01","c02","c03","c04","c05","c06","c07","c08","c09","c10",
         "d01","d02","d03","d04","d05","d06","d07","d08","d09","d10",
         "e01","e02","e03","e04","e05","e06","e07","e08","e09","e10",
         "f01","f02","f03","f04","f05","f06","f07","f08","f09","f10",
         "g01","g02","g03","g04","g05","g06","g07","g08","g09","g10",
         "h01","h02","h03","h04","h05","h06","h07","h08","h09","h10",
         "i01","i02","i03","i04","i05","i06","i07","i08","i09","i10",
         "j01","j02","j03","j04","j05","j06","j07","j08","j09","j10"]

ruchy2 = ["a01","a02","a03","a04","a05","a06","a07","a08","a09","a10",
         "b01","b02","b03","b04","b05","b06","b07","b08","b09","b10",
         "c01","c02","c03","c04","c05","c06","c07","c08","c09","c10",
         "d01","d02","d03","d04","d05","d06","d07","d08","d09","d10",
         "e01","e02","e03","e04","e05","e06","e07","e08","e09","e10",
         "f01","f02","f03","f04","f05","f06","f07","f08","f09","f10",
         "g01","g02","g03","g04","g05","g06","g07","g08","g09","g10",
         "h01","h02","h03","h04","h05","h06","h07","h08","h09","h10",
         "i01","i02","i03","i04","i05","i06","i07","i08","i09","i10",
         "j01","j02","j03","j04","j05","j06","j07","j08","j09","j10"]

slownik1 = {0:"a",
           1:"b",
           2:"c",
           3:"d",
           4:"e",
           5:"f",
           6:"g",
           7:"h",
           8:"i",
           9:"j"}

slownik2 = {"a":0,
           "b":1,
           "c":2,
           "d":3,
           "e":4,
           "f":5,
           "g":6,
           "h":7,
           "i":8,
           "j":9}

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
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -1
        elif enemyfire == self.c:
            print("Trafiony")
            self.c = -1
        elif enemyfire == self.d:
            print("Trafiony")
            self.d = -1
        if self.a == -1 and self.b == -1 and self.c == -1 and self.d == -1:
            self.a = "już zatopiony"
            print ("Czteromasztowiec zatopiony")
            
    
class Trojmaszt():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -1
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -1
        elif enemyfire == self.c:
            print("Trafiony")
            self.c = -1
        if self.a == -1 and self.b == -1 and self.c == -1:
            self.a = "już zatopiony"
            print("Zatopiony trójmasztowiec")

class Dwumaszt():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print("Trafiony")
            self.a = -1
        elif enemyfire == self.b:
            print("Trafiony")
            self.b = -1
        if self.a == -1 and self.b == -1:
            self.a = "już zatopiony"
            print("Zatopiony dwumasztowiec")

class Jednomaszt():
    def __init__(self,a):
        self.a = a
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            print ("Trafiony")
            self.a = -1
        if self.a == -1:
            self.a = "już zatopiony"
            print ("Zatopiony jednomasztowiec")

def tworzenie():
    #czteromasztowiec
    x,y = np.where(mymap == 4)
    cztm = Czteromaszt((y[0],x[0]),(y[1],x[1]),(y[2],x[2]),(y[3],x[3]))
    #trójmasztowce
    x,y = np.where(mymap == 3)
    trz1 = Trojmaszt((y[0],x[0]),(y[1],x[1]),(y[2],x[2]))
    trz2 = Trojmaszt((y[3],x[3]),(y[4],x[4]),(y[5],x[5]))
    #dwumasztowce
    x,y = np.where(mymap == 2)
    dwu1 = Dwumaszt((y[0],x[0]),(y[1],x[1]))
    dwu2 = Dwumaszt((y[2],x[2]),(y[3],x[3]))
    dwu3 = Dwumaszt((y[4],x[4]),(y[5],x[5]))
    #jednomasztowce
    x,y = np.where(mymap == 1)
    jed1 = Jednomaszt((y[0],x[0]))
    jed2 = Jednomaszt((y[1],x[1]))
    jed3 = Jednomaszt((y[2],x[2]))
    jed4 = Jednomaszt((y[3],x[3]))
    return cztm ,trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4
"""
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
        if x[1] < 9:
            print(str(slownik1[x[0]]) + "0" + str(x[1]+1))
            return (str(slownik1[x[0]]) + "0" + str(x[1]+1))
        else:
            print(str(slownik1[x[0]]) + "10")
            return (str(slownik1[x[0]]) + "10")
"""
def fire():
    y = len(ruchy) - 1
    x = r.randint(0, y)
    strzal = ruchy[x]
    print(strzal, "||||||||||", y)
    ruchy.pop(x)
    return(strzal)
#Testowy ostrzał
def fire2():
    y = len(ruchy2) - 1
    x = r.randint(0, y)
    strzal = ruchy2[x]
    print(strzal, "----------", y)
    ruchy2.pop(x)
    return(strzal)

#zatapianie okrętów trafionych
def dobijanie():
    komunikat = sys.stdin
    print("echo", komunikat)
    return komunikat
    
# Iteruje po każdym statku, wywołując metodę "trafiony" względem "enemyfire"=koordynatów
def obrywamy(enemyfire):
    for statek in flota:
        statek.trafiony(enemyfire)
    a = enemyfire[0]
    b = enemyfire[1]
    if mymap[b,a] == 0:
        print ("Pudło")

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

def proba():
    if pierwszenstwo == "-s":
        fire()
        enemyfire = fire2()
        a = enemyfire[0]
        a = slownik2[a]
        b = int(enemyfire[1])
        if b == 0:
            c = int(enemyfire[2])-1
        else:
            c = 9
        obrywamy((a,c))
        if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
            print("koniec")
            sys.exit()
        return proba()
    
    else:
        enemyfire = fire()
        a = enemyfire[0]
        a = slownik2[a]
        b = int(enemyfire[1])
        if b == 0:
            c = int(enemyfire[2])-1
        else:
            c = 9
        obrywamy((a,c))
        fire2()
        if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
            print("koniec")
            sys.exit()
        return proba()
proba()

"""def wielka_gra():
    while True :
        if pierwszenstwo == "s":
            fire()
            czytrafione.append(input())
            enemyfire = input()
            obrywamy(enemyfire)
            
            if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
                sys.exit()
        else:
            enemyfire = input()
            obrywamy(enemyfire)
            fire()
            czytrafione.append(input())
            if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
                sys.exit()"""


