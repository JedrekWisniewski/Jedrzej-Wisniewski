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
            if x+1 <= 9:
                plansza[y+1,x+1] = 5
            if x-1 >= 0:
                plansza[y+1,x-1] = 5
        if y-1 >= 0:
            plansza[y-1,x] = 5
            if x+1 <= 9:
                plansza[y-1,x+1] = 5
            if x-1 >= 0:
                plansza[y-1,x-1] = 5
        if x+1 <= 9:
            plansza[y,x+1] = 5
        if x-1 >= 0:
            plansza[y,x-1] = 5
    else:
        return one()
        
    #return ("Poziomo:", x, "Pionowo:", y)

def two():
    pozpion = ran.randint(0,1)
    x = ran.randint(0, len(plansza)-1)
    y = ran.randint(0, len(plansza)-1)

    if pozpion == 0:
        x1 = x+1
        if x1 > 9:
            return two()
        else:
            if plansza[y,x] == 0 and plansza[y,x1] == 0:
                plansza[y,x] = 2
                plansza[y,x1] = 2
                if y+1 <= 9:
                    plansza[y+1,x] = 5
                    plansza[y+1,x1] = 5
                    if x1+1 <= 9:
                        plansza[y+1,x1+1] = 5
                    if x-1 >= 0:
                        plansza[y+1,x-1] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
                    plansza[y-1,x1] = 5
                    if x1+1 <= 9:
                        plansza[y-1,x1+1] = 5
                    if x-1 >= 0:
                        plansza[y-1,x-1] = 5
                if x1+1 <= 9:
                    plansza[y,x1+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
            else:
                return two()
        
        #return ("Poziomo:", x, x1, "Pionowo:", y)
    elif pozpion == 1:
        y1 = y+1
        if y1 > 9:
            return two()
        else:
            if plansza[y,x] == 0 and plansza[y1,x] == 0:
                plansza[y,x] = 2
                plansza[y1,x] = 2
                if x+1 <= 9:
                    plansza[y,x+1] = 5
                    plansza[y1,x+1] = 5
                    if y1+1 <= 9:
                        plansza[y1+1,x+1] = 5
                    if y-1 >= 0:
                        plansza[y-1,x+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
                    plansza[y1,x-1] = 5
                    if y1+1 <= 9:
                        plansza[y1+1,x-1] = 5
                    if y-1 >= 0:
                        plansza[y-1,x-1] = 5
                if y1+1 <= 9:
                    plansza[y1+1,x] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
            else:
                return two()
                    
        #return ("Poziomo:", x, "Pionowo:", y, y1) 

def three():
    pozpion = ran.randint(0,1)
    x = ran.randint(0, len(plansza)-1)
    y = ran.randint(0, len(plansza)-1)

    if pozpion == 0:
        x1 = x+1
        x2 = x+2
        if x2 > 9:
            return three()
        else:
            if plansza[y,x] == 0 and plansza[y,x1] == 0 and plansza[y,x2] == 0:
                plansza[y,x] = 3
                plansza[y,x1] = 3
                plansza[y,x2] = 3
                if y+1 <= 9:
                    plansza[y+1,x] = 5
                    plansza[y+1,x1] = 5
                    plansza[y+1,x2] = 5
                    if x2+1 <= 9:
                        plansza[y+1,x2+1] = 5
                    if x-1 >= 0:
                        plansza[y+1,x-1] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
                    plansza[y-1,x1] = 5
                    plansza[y-1,x2] = 5
                    if x1+1 <= 9:
                        plansza[y-1,x2+1] = 5
                    if x-1 >= 0:
                        plansza[y-1,x-1] = 5
                if x2+1 <= 9:
                    plansza[y,x2+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
            else:
                return three()

        #return ("Poziomo:", x, x1, x2, "Pionowo:", y)
    elif pozpion == 1:
        y1 = y+1
        y2 = y+2
        if y2 > 9:
            return three()
        else:
            if plansza[y,x] == 0 and plansza[y1,x] == 0 and plansza[y2,x] == 0:
                plansza[y,x] = 3
                plansza[y1,x] = 3
                plansza[y2,x] = 3
                if x+1 <= 9:
                    plansza[y,x+1] = 5
                    plansza[y1,x+1] = 5
                    plansza[y2,x+1] = 5
                    if y2+1 <= 9:
                        plansza[y2+1,x+1] = 5
                    if y-1 >= 0:
                        plansza[y-1,x+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
                    plansza[y1,x-1] = 5
                    plansza[y2,x-1] = 5
                    if y2+1 <= 9:
                        plansza[y2+1,x-1] = 5
                    if y-1 >= 0:
                        plansza[y-1,x-1] = 5
                if y2+1 <= 9:
                    plansza[y2+1,x] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
            else:
                return three()

        #return ("Poziomo:", x, "Pionowo:", y, y1, y2)

def four():
    pozpion = ran.randint(0,1)
    x = ran.randint(0, len(plansza)-1)
    y = ran.randint(0, len(plansza)-1)

    if pozpion == 0:
        x1 = x+1
        x2 = x+2
        x3 = x+3
        if x3 > 9:
            return four()
        else:
            if plansza[y,x] == 0 and plansza[y,x1] == 0 and plansza[y,x2] == 0 and plansza[y,x3] == 0:
                plansza[y,x] = 4
                plansza[y,x1] = 4
                plansza[y,x2] = 4
                plansza[y,x3] = 4
                if y+1 <= 9:
                    plansza[y+1,x] = 5
                    plansza[y+1,x1] = 5
                    plansza[y+1,x2] = 5
                    plansza[y+1,x3] = 5
                    if x3+1 <= 9:
                        plansza[y+1,x3+1] = 5
                    if x-1 >= 0:
                        plansza[y+1,x-1] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
                    plansza[y-1,x1] = 5
                    plansza[y-1,x2] = 5
                    plansza[y-1,x3] = 5
                    if x2+1 <= 9:
                        plansza[y-1,x3+1] = 5
                    if x-1 >= 0:
                        plansza[y-1,x-1] = 5
                if x3+1 <= 9:
                    plansza[y,x3+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
            else:
                return four()

        #return ("Poziomo:", x, x1, x2, x3, "Pionowo:", y)
    elif pozpion == 1:
        y1 = y+1
        y2 = y+2
        y3 = y+3
        if y3 > 9:
            return four()
        else:
            if plansza[y,x] == 0 and plansza[y1,x] == 0 and plansza[y2,x] == 0 and plansza[y3,x] == 0:
                plansza[y,x] = 4
                plansza[y1,x] = 4
                plansza[y2,x] = 4
                plansza[y3,x] = 4
                if x+1 <= 9:
                    plansza[y,x+1] = 5
                    plansza[y1,x+1] = 5
                    plansza[y2,x+1] = 5
                    plansza[y3,x+1] = 5
                    if y3+1 <= 9:
                        plansza[y3+1,x+1] = 5
                    if y-1 >= 0:
                        plansza[y-1,x+1] = 5
                if x-1 >= 0:
                    plansza[y,x-1] = 5
                    plansza[y1,x-1] = 5
                    plansza[y2,x-1] = 5
                    plansza[y3,x-1] = 5
                    if y3+1 <= 9:
                        plansza[y3+1,x-1] = 5
                    if y-1 >= 0:
                        plansza[y-1,x-1] = 5
                if y2+1 <= 9:
                    plansza[y3+1,x] = 5
                if y-1 >= 0:
                    plansza[y-1,x] = 5
            else:
                return four()

        #return ("Poziomo:", x, "Pionowo:", y, y1, y2, y3)

def czyszczenie():
    y = 0
    while y <= 9:
        x = 0
        while x <= 9:
            if plansza[y,x] == 5:
                plansza[y,x] = 0
            x = x+1
        y = y+1

def generator():
    four()
    three()
    three()
    two()
    two()
    two()
    one()
    one()
    one()
    one()
    czyszczenie()
    return plansza
