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
            self.a = -1
            if self.a == -1 and self.b == -1 and self.c == -1 and self.d == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")
        elif enemyfire == self.b:
            self.b = -1
            if self.a == -1 and self.b == -1 and self.c == -1 and self.d == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")
        elif enemyfire == self.c:
            self.c = -1
            if self.a == -1 and self.b == -1 and self.c == -1 and self.d == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")
        elif enemyfire == self.d:
            self.d = -1
            if self.a == -1 and self.b == -1 and self.c == -1 and self.d == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")
    
class Trojmaszt():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            self.a = -1
            if self.a == -1 and self.b == -1 and self.c == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")
        elif enemyfire == self.b:
            self.b = -1
            if self.a == -1 and self.b == -1 and self.c == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")
        elif enemyfire == self.c:
            self.c = -1
            if self.a == -1 and self.b == -1 and self.c == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")

class Dwumaszt():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            self.a = -1
            if self.a == -1 and self.b == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")
        elif enemyfire == self.b:
            self.b = -1
            if self.a == -1 and self.b == -1:
                self.a = "już zatopiony"
                print("zatop_")
                return("zatop_")
            else:
                print("trafio")
                return("trafio")

class Jednomaszt():
    def __init__(self,a):
        self.a = a
    def trafiony(self, enemyfire):
        if enemyfire == self.a:
            self.a = -1
        if self.a == -1:
            self.a = "już zatopiony"
            print("zatop_")
            return("zatop_")

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

dziennik = []
ostatnistrzal = []
#zatapianie okrętów trafionych
def prawo(wsp_1,zatop_wsp):
    try:
        wsp_1 = slownik2[wsp_1]
        wsp_1 = slownik1[wsp_1 + 1]
        newkoord = wsp_1 + zatop_wsp[1] + zatop_wsp[2]
        return newkoord, wsp_1
    except:
        newkoord = "blad"
        wsp_1 = "blad"
        return newkoord, wsp_1
def lewo(wsp_1,zatop_wsp):
    try:
        wsp_1 = slownik2[wsp_1]
        wsp_1 = slownik1[wsp_1  - 1]
        newkoord = wsp_1 + zatop_wsp[1] + zatop_wsp[2]
        return newkoord, wsp_1
    except:
        newkoord = "blad"
        wsp_1 = "blad"
        return newkoord, wsp_1
        
def gora(pion):
    pion = int(pion)
    pion = pion - 1
    if pion < 0:
        pion = "blad"
        return pion
    else:
        pion = str(pion)
        pion = "0"+pion
        return pion
def dol(pion):
    pion = int(pion)
    pion = pion + 1
    if pion < 10:
        pion = "0" + str(pion)
        return pion
    else:
        return str(pion)
  
def przygotowanie():
    statek = []
    komunikat = dziennik[len(dziennik)-1]
    #print(komunikat)
    if komunikat == "zatop_":
        #pierwszy koord
        zatop_wsp = ostatnistrzal[len(ostatnistrzal)-1]
        #print(zatop_wsp)
        statek.append(zatop_wsp)
        #print(statek)
        wsp_1 = zatop_wsp[0]
        pion = int(zatop_wsp[1] + zatop_wsp[2])
        #print(pion)
        #w lewo
        newkoord, wsp_2 = lewo(wsp_1, zatop_wsp)
        if newkoord in ostatnistrzal:
            statek.append(newkoord)
            #dalej w lewo
            newkoord, wsp_3 = lewo(wsp_2, zatop_wsp)
            if newkoord in ostatnistrzal:
                statek.append(newkoord)
                #dalej w lewo
                newkoord, wsp_4 = lewo(wsp_3, zatop_wsp)
                if newkoord in ostatnistrzal:
                    statek.append(newkoord)
                 #i w prawo 4
                else:
                    newkoord,wsp_4 = prawo(wsp_1, zatop_wsp)
                    if newkoord in ostatnistrzal:
                        statek.append(newkoord)
             #tez w prawo do 3
            else:
                newkoord,wsp_3 = prawo(wsp_1, zatop_wsp)
                if newkoord in ostatnistrzal:
                    statek.append(newkoord)
                    #do 4 w prawo
                    newkoord,wsp_4 = prawo(wsp_3, zatop_wsp)
                    if newkoord in ostatnistrzal:
                        statek.append(newkoord)
        else:
            #w prawo do 2ch
            newkoord, wsp_2 = prawo(wsp_1, zatop_wsp)
            if newkoord in ostatnistrzal:
                statek.append(newkoord)
                #w prawo do 3ch
                newkoord, wsp_3 = prawo(wsp_2, zatop_wsp)
                if newkoord in ostatnistrzal:
                    statek.append(newkoord)
                    #w prawo do 4rech
                    newkoord, wsp_4 = prawo(wsp_3, zatop_wsp)
                    if newkoord in ostatnistrzal:
                        statek.append(newkoord)
        #PRAWO I LEWO SKOŃCZONE, TERAZ GÓRA DÓŁ
        #do góry 2
        pion_1 = gora(pion)
        newkoord = wsp_1 + pion_1
        if newkoord in ostatnistrzal:
            statek.append(newkoord)
            #wyżej 3
            pion_2 = gora(pion_1)
            newkoord = wsp_1 + pion_2
            if newkoord in ostatnistrzal:
                statek.append(newkoord)
                #wyżej 4
                pion_3 = gora(pion_2)
                newkoord = wsp_1 + pion_3
                if newkoord in ostatnistrzal:
                    statek.append(newkoord)
                #w dół 4
                else :
                    pion_3 = dol(pion)
                    newkoord = wsp_1 + pion_3
                    if newkoord in ostatnistrzal:
                        statek.append(newkoord)
            #w dół 3
            else:
                pion_2 = dol(pion)
                newkoord = wsp_1 + pion_2
                if newkoord in ostatnistrzal:
                    statek.append(newkoord)
                    pion_3 = dol(pion_2)
                    newkoord = wsp_1 + pion_3
                    if newkoord in ostatnistrzal:
                        statek.append(newkoord)
        #w dół 2
        else:
            pion_1 = dol(pion)
            newkoord = wsp_1 + pion_1
            if newkoord in ostatnistrzal:
                statek.append(newkoord)
                pion_2 = dol(pion_1)
                newkoord = wsp_1 + pion_1
                if newkoord in ostatnistrzal:
                    statek.append(newkoord)
                    pion_3 = dol(pion_2)
                    newkoord = wsp_1 + pion_1
                    if newkoord in ostatnistrzal:
                        statek.append(newkoord)

    return statek

def usungoradol(pozycja):
    poz1 = pozycja[0]
    poz2 = pozycja[1]
    poz3 = pozycja[2]
    pion = int(poz2+poz3)
    czygora = pion - 1
    czygora = "0" + str(czygora)
    czydol = pion + 1
    if czydol < 10:
        czydol = "0" + str(czydol)
    czygora = poz1 + czygora
    czydol = poz1 + czydol
    if czygora in ruchy:
        ruchy.remove(czygora)
    if czydol in ruchy:
        ruchy.remove(czydol)
    
def usunboki(pozycja):
    poz1 = pozycja[0]
    pion = pozycja[1] + pozycja[2]
    poz1 = slownik2[poz1]
    lewo = slownik1[poz1 - 1]
    prawo = slownik1[poz1 + 1]

    lewo = lewo + pion
    prawo = prawo + pion
    if lewo in ruchy:
        ruchy.remove(lewo)
    if prawo in ruchy:
        ruchy.remove(prawo)
    
def usunskosy(pozycja):
    poz1 = pozycja[0]
    pion = pozycja[1] + pozycja[2]
    poz1 = slownik2[poz1]
    lewo = slownik1[poz1 - 1]
    prawo = slownik1[poz1 + 1]
    usungoradol(prawo)
    usungoradol(lewo)
def korekta():
    statek = przygotowanie()
    #print(statek)
    for pozycja in statek:
        try:
            usungoradol(pozycja)
        except:
            pass
        try:
            usunboki(pozycja)
        except:
            pass
        try:
            usunskosy(pozycja)
        except:
            pass   

#Losowanie strzału i wykorzystanie funkcji powyzej.
def fire():
    y = len(ruchy) - 1
    x = r.randint(0, y)
    strzal = ruchy[x]
    print(strzal)
    #ostatnistrzal.append(strzal)
    ruchy.pop(x)
    return(strzal)
    
# Iteruje po każdym statku, wywołując metodę "trafiony" względem "enemyfire"=koordynatów
def obrywamy(enemyfire):
    for i in flota:
        x = i.trafiony(enemyfire)
        if x == "trafio":
            return x
        elif x == "zatop_":
            return x
    a = enemyfire[0]
    b = enemyfire[1]
    if mymap[b,a] == 0:
        print("pudlo_")
        return("pudlo_")

#TESTY####

#Wczytanie, stworzenie statków, dodanie do floty
mymap = wczytywanie()
cztm, trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4 = tworzenie()
flota = [cztm, trz1, trz2, dwu1, dwu2, dwu3, jed1, jed2, jed3, jed4]

pierwszenstwo = sys.argv[1]

def gra():
    if pierwszenstwo == "-s":
        x = fire()
        print(x)
        y = input()
        if y == "trafio" or y == "zatop_":
            ostatnistrzal.append(x)
        dziennik.append(y)
        korekta()
        enemyfire = input()
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
        return gra()
    
    elif pierwszenstwo == "-d":
        enemyfire = input()
        a = enemyfire[0]
        a = slownik2[a]
        b = int(enemyfire[1])
        if b == 0:
            c = int(enemyfire[2])-1
        else:
            c = 9
        obrywamy((a,c))
        x = fire()
        print(x)
        y = input()
        if y == "trafio" or y == "zatop_":
            ostatnistrzal.append(x)
        dziennik.append(input())
        korekta()
        if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
            print("koniec")
            sys.exit()
        return gra()

gra()
"""
def test():
    enemyfire = fire()
    a = enemyfire[0]
    a = slownik2[a]
    b = int(enemyfire[1])
    if b == 0:
        c = int(enemyfire[2])-1
    else:
        c = 9
    y = obrywamy((a,c))
    if y == "trafio" or y == "zatop_":
        ostatnistrzal.append(x)
    dziennik.append(y)
    korekta()
    if cztm.a == "już zatopiony" and trz1.a == "już zatopiony" and trz2.a == "już zatopiony" and dwu1.a == "już zatopiony" and dwu2.a == "już zatopiony" and dwu3.a == "już zatopiony" and jed1.a == "już zatopiony" and jed2.a == "już zatopiony" and jed3.a == "już zatopiony" and jed4.a == "już zatopiony":
        print("koniec")
        sys.exit()
    return test()

test()
"""
