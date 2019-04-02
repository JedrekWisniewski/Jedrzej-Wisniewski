import numpy as np
import random as ran

plansza = np.zeros(shape=(10,10))
def one():
    
        x = ran.randint(0, len(plansza)-1)
        y = ran.randint(0, len(plansza)-1)
        
    try:
        if plansza[y,x] == 0:

            if plansza[y+1,x] != 0:
                return one()
            elif plansza[y-1,x] != 0:
                return one()
            elif plansza[y,x+1] != 0:
                return one()
            elif plansza[y,x-1] != 0:
                return one()
            else:
                plansza[y,x] = 1
                
    except IndexError:
        return one()
    
        
    return print(plansza),print("Poziomo :",x,"\nPionowo :",y)


