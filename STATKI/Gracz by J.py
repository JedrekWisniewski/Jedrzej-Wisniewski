#Gracz

import numpy as np
import sys
import random as r

def wczytywanie(nazwapliku="Gracz1.npy"):
    mymap = np.load(nazwapliku)
    return mymap
    #enemymap tez bedzie

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

def wrogi_ostrzal(enemyfire):
    t = "trafiony"
    n = "nietrafiony"
    z = "zatopiony"
    if mymap [enemyfire] == 1:
        mymap[enemyfire] = -1
        return z
    elif mymap[enemyfire] == 2.0:
        if mymap[enemyfire + (1,0)] == -2:
            mymap[enemyfire] = -2
            return z
        elif mymap[enemyfire -(1,0)] == -2:
            return z
        elif mymap[enemyfire +(0,1)] == -2:
            return z
        elif mymap[enemyfire -(1,0)] == -2:
            return z
        else:
            return t
    else:
        mymap[enemyfire] = -5
        return "pudło"

def test(enemyfire):
    return enemyfire , mymap[enemyfire]
mymap = wczytywanie()


