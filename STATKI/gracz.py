import numpy as np
from numpy import *


#GRACZ______________________________________________________________________________________________________

#otweranie pliku tekstowego do odczytu:
#gracz1=array(open("gracz2.txt","r"))
#gracz2=array(open("gracz2.txt","r"))
#gracz1.close()
#gracz2.close()

gracz1=[0, 0, 0, 0, 0, 0, 0, 2, 2, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0, 0, 3, 0],[0, 0, 0, 0, 0, 0, 0, 0, 3, 0],[3, 3, 3, 0, 0, 0, 0, 0, 3, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 4, 4, 4, 4, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],[2, 2, 0, 0, 2, 2, 0, 0, 0, 0]
#print(gracz1)

print("Alfabet :") #petelka co to zrobi zbior alfabetu
x = 0
tmp=[]
for i in range(65, 91):
    litera = chr(i)
    x += 1
    tmp.append(litera)
    if i > 65 and x % 5 == 0:
        x = 0
print(tmp)

ilewierszy=[]
wiersze=[]
ilekolumn=[]
kolumny=[]
for  i in range(0,(len(gracz1))):#  ma zliczac ile jest  wierszy zeby potem im przypisac kolumny
    ilewierszy= i+1 #  licza ile wierszy
    wiersze=list(range(1,ilewierszy+1))#z liczby wierszy tworzy liste zeby potem mozna bylo im przypisywac kolumne
    ilekolumn=len(gracz1[i])#zlicza ile ma byc kolumn
    kolumny=list(range(1,ilekolumn+1))# z liczby kolumn robi liste
    for i in range(0,len(kolumny)):#kazdemu elementowi z listy kolumn przypisuje litere z alfabetu
        kolumny[i]=tmp[i]

print("liczba kolumn: ",ilekolumn)
print("liczba wierszy: ",ilewierszy)
print("lista wierszy: ",wiersze)
print("lista kolumn: ",kolumny)

