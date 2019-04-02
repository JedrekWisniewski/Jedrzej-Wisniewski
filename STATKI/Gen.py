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
        else:
            raise Exception
                
    except IndexError:
        return one()
    
        
    return print(plansza),print("Poziomo :",x,"\nPionowo :",y)

def four():
    pozpion = ran.randint(0,1)

    x = ran.randint(0, len(plansza)-1)
    y = ran.randint(0, len(plansza)-1)

    if pozpion == 0:
        y.append(y[0]+1)
        y.append(y[1]+1)
        y.append(y[2]+1)
    elif pozpion == 1:
        x.append(x[0]+1)
        x.append(x[1]+1)
         x.append(x[2]+1)
    else:
        raise Exception
    
    return pozpion

