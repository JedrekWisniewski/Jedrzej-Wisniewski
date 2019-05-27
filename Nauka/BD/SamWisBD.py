import Poroba1 as Ned
import random as r
import math
#Liczba aminokwasów w sekwencji
n = 10
#Słownik dla wylosowanych aminokwasów
slownik = { 1:'G', 2:'A', 3:'V', 4:'L', 5:'I', 6:'P', 7:'S', 8:'T', 9:'C',
            10:'M', 11:'F', 12:'Y', 13:'W', 14:'D',
            15:'N', 16:'E', 17:'Q', 18:'K', 19:'R', 20:'H'}
#funkcja los_sek tworzy dwie sekwencje o długości n-aminokwasów : sekwencja1 oraz sekwencja2
def los_sek(n):            
    sekwencja1 = str()
    sekwencja2 = str()
    for i in range(n):
        sekwencja1 = sekwencja1 + slownik[r.randint(1,20)]
        sekwencja2 = sekwencja2 + slownik[r.randint(1,20)]
        
    return sekwencja1, sekwencja2
#Przynajmniej 100
ilerazy = 100
#Funkcja Sr_wyn oblicza średnią dla "n = ilerazy" par sekwencji aminokwasowych
#z algorytmu N-W
def Sr_wyn():
    suma = 0
    for i in range(ilerazy):
        sek1,sek2 = los_sek(n)
        wynik = Ned.algorytm(sek1,sek2)
        suma = suma + wynik
    srednia = suma / ilerazy
    return srednia
#Średnia dla n=ilerazy identycznych par sekwencji z algorytmu N-W     
def Sr_id():
    suma = 0
    for i in range(ilerazy):
        sek1,sek2 = los_sek(n)
        wynik = Ned.algorytm(sek1, sek1)
        suma = suma + wynik
    srednia = suma / ilerazy
    return srednia
def fun_odleg():
    sek1 = "GAVGAVGAVG"
    sek2 = "GAVGAVGAVG"
    S = Ned.algorytm(sek1, sek2) # Wartość dopasowania naszych sekwencji
    Sr = Sr_wyn()
    Sid = Sr_id()
    nawias = (S - Sr)/(Sid - Sr)
    d = -100*math.log1p(nawias) #wzór z Lista1A
    return d
print(fun_odleg())
 
