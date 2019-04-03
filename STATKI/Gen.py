import numpy as np
import random as ran

plansza = np.zeros(shape=(10,10))


def one():
    
    x = ran.randint(0, len(plansza)-1)
    y = ran.randint(0, len(plansza)-1)
        
    if plansza[y,x] == 0:
        plansza[y,x] = 1
        if y+1 <= 9:
            plansza[y+1,x] = 5
        if y-1 >= 0:
            plansza[y-1,x] = 5
        if x+1 <=9:
            plansza[y,x+1] = 5
        if x-1 >= 0:
            plansza[y,x-1] = 5
    else:
        return one()
        
    return ("Poziomo :",x,"Pionowo :",y)

def two():
    pozpion = ran.randint(0,1)

    x = ran.randint(0, len(plansza)-1)
    y = ran.randint(0, len(plansza)-1)

    if pozpion == 0:
        x1 = x+1
        if x1>9:
            return two()
        else:
            if plansza[y,x] == 0 and plansza[y,x1] == 0:
                plansza[y,x] = 2
                plansza[y,x1] = 2
                if y+1 <= 9:
                    plansza[y+1,x] = 5
                    plansza[y+1,x1] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
                    plansza[y-1,x1] = 5
                if x1+1 <= 9:
                    plansza[y,x1+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
        
        return ("Poziomo:",x,x1,"Pionowo:",y)     
    elif pozpion == 1:
        y1 = y+1
        if y1>9:
            return two()
        else:
            if plansza[y,x] == 0 and plansza[y1,x] == 0:
                plansza[y,x] = 2
                plansza[y1,x] = 2
                if x+1 <= 9:
                    plansza[y,x+1] = 5
                    plansza[y1,x+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
                    plansza[y1,x-1] = 5
                if y1+1 <= 9:
                    plansza[y1+1,x] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
        return ("Poziomo :",x,"Pionowo:",y,y1) 
    
