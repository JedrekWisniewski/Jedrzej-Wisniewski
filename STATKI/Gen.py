import numpy as np
import random as ran
import sys
miejscedocelowe = sys.argv[1]
class Gracz(object):
    def __init__(self):
        self.plansza = np.zeros(shape=(10,10))

    def one(self):
        x = ran.randint(0, len(self.plansza)-1)
        y = ran.randint(0, len(self.plansza)-1)
        
        if self.plansza[y,x] == 0:
            self.plansza[y,x] = 1
            if y+1 <= 9:
                self.plansza[y+1,x] = 5
                if x+1 <= 9:
                    self.plansza[y+1,x+1] = 5
                if x-1 >= 0:
                    self.plansza[y+1,x-1] = 5
            if y-1 >= 0:
                self.plansza[y-1,x] = 5
                if x+1 <= 9:
                    self.plansza[y-1,x+1] = 5
                if x-1 >= 0:
                    self.plansza[y-1,x-1] = 5
            if x+1 <= 9:
                self.plansza[y,x+1] = 5
            if x-1 >= 0:
                self.plansza[y,x-1] = 5
        else:
            return self.one()

    def two(self):
        pozpion = ran.randint(0,1)
        x = ran.randint(0, len(self.plansza)-1)
        y = ran.randint(0, len(self.plansza)-1)

        if pozpion == 0:
            x1 = x+1
            if x1 > 9:
                return self.two()
            else:
                if self.plansza[y,x] == 0 and self.plansza[y,x1] == 0:
                    self.plansza[y,x] = 2
                    self.plansza[y,x1] = 2
                    if y+1 <= 9:
                        self.plansza[y+1,x] = 5
                        self.plansza[y+1,x1] = 5
                        if x1+1 <= 9:
                            self.plansza[y+1,x1+1] = 5
                        if x-1 >= 0:
                            self.plansza[y+1,x-1] = 5
                    if y-1 >= 0:
                        self.plansza[y-1,x] = 5
                        self.plansza[y-1,x1] = 5
                        if x1+1 <= 9:
                            self.plansza[y-1,x1+1] = 5
                        if x-1 >= 0:
                            self.plansza[y-1,x-1] = 5
                    if x1+1 <= 9:
                        self.plansza[y,x1+1] = 5
                    if x-1 >= 0:
                        self.plansza[y,x-1] = 5
                else:
                    return self.two()
            
        elif pozpion == 1:
            y1 = y+1
            if y1 > 9:
                return self.two()
            else:
                if self.plansza[y,x] == 0 and self.plansza[y1,x] == 0:
                    self.plansza[y,x] = 2
                    self.plansza[y1,x] = 2
                    if x+1 <= 9:
                        self.plansza[y,x+1] = 5
                        self.plansza[y1,x+1] = 5
                        if y1+1 <= 9:
                            self.plansza[y1+1,x+1] = 5
                        if y-1 >= 0:
                            self.plansza[y-1,x+1] = 5
                    if x-1 >= 0:
                        self.plansza[y,x-1] = 5
                        self.plansza[y1,x-1] = 5
                        if y1+1 <= 9:
                            self.plansza[y1+1,x-1] = 5
                        if y-1 >= 0:
                            self.plansza[y-1,x-1] = 5
                    if y1+1 <= 9:
                        self.plansza[y1+1,x] = 5
                    if y-1 >= 0:
                        self.plansza[y-1,x] = 5
                else:
                    return self.two() 

    def three(self):
        pozpion = ran.randint(0,1)
        x = ran.randint(0, len(self.plansza)-1)
        y = ran.randint(0, len(self.plansza)-1)

        if pozpion == 0:
            x1 = x+1
            x2 = x+2
            if x2 > 9:
                return self.three()
            else:
                if self.plansza[y,x] == 0 and self.plansza[y,x1] == 0 and self.plansza[y,x2] == 0:
                    self.plansza[y,x] = 3
                    self.plansza[y,x1] = 3
                    self.plansza[y,x2] = 3
                    if y+1 <= 9:
                        self.plansza[y+1,x] = 5
                        self.plansza[y+1,x1] = 5
                        self.plansza[y+1,x2] = 5
                        if x2+1 <= 9:
                            self.plansza[y+1,x2+1] = 5
                        if x-1 >= 0:
                            self.plansza[y+1,x-1] = 5
                    if y-1 >= 0:
                        self.plansza[y-1,x] = 5
                        self.plansza[y-1,x1] = 5
                        self.plansza[y-1,x2] = 5
                        if x2+1 <= 9:
                            self.plansza[y-1,x2+1] = 5
                        if x-1 >= 0:
                            self.plansza[y-1,x-1] = 5
                    if x2+1 <= 9:
                        self.plansza[y,x2+1] = 5
                    if x-1 >= 0:
                        self.plansza[y,x-1] = 5
                else:
                    return self.three()

        elif pozpion == 1:
            y1 = y+1
            y2 = y+2
            if y2 > 9:
                return self.three()
            else:
                if self.plansza[y,x] == 0 and self.plansza[y1,x] == 0 and self.plansza[y2,x] == 0:
                    self.plansza[y,x] = 3
                    self.plansza[y1,x] = 3
                    self.plansza[y2,x] = 3
                    if x+1 <= 9:
                        self.plansza[y,x+1] = 5
                        self.plansza[y1,x+1] = 5
                        self.plansza[y2,x+1] = 5
                        if y2+1 <= 9:
                            self.plansza[y2+1,x+1] = 5
                        if y-1 >= 0:
                            self.plansza[y-1,x+1] = 5
                    if x-1 >= 0:
                        self.plansza[y,x-1] = 5
                        self.plansza[y1,x-1] = 5
                        self.plansza[y2,x-1] = 5
                        if y2+1 <= 9:
                            self.plansza[y2+1,x-1] = 5
                        if y-1 >= 0:
                            self.plansza[y-1,x-1] = 5
                    if y2+1 <= 9:
                        self.plansza[y2+1,x] = 5
                    if y-1 >= 0:
                        self.plansza[y-1,x] = 5
                else:
                    return self.three()

    def four(self):
        pozpion = ran.randint(0,1)
        x = ran.randint(0, len(self.plansza)-1)
        y = ran.randint(0, len(self.plansza)-1)

        if pozpion == 0:
            x1 = x+1
            x2 = x+2
            x3 = x+3
            if x3 > 9:
                return self.four()
            else:
                if self.plansza[y,x] == 0 and self.plansza[y,x1] == 0 and self.plansza[y,x2] == 0 and self.plansza[y,x3] == 0:
                    self.plansza[y,x] = 4
                    self.plansza[y,x1] = 4
                    self.plansza[y,x2] = 4
                    self.plansza[y,x3] = 4
                    if y+1 <= 9:
                        self.plansza[y+1,x] = 5
                        self.plansza[y+1,x1] = 5
                        self.plansza[y+1,x2] = 5
                        self.plansza[y+1,x3] = 5
                        if x3+1 <= 9:
                            self.plansza[y+1,x3+1] = 5
                        if x-1 >= 0:
                            self.plansza[y+1,x-1] = 5
                    if y-1 >= 0:
                        self.plansza[y-1,x] = 5
                        self.plansza[y-1,x1] = 5
                        self.plansza[y-1,x2] = 5
                        self.plansza[y-1,x3] = 5
                        if x2+1 <= 9:
                            self.plansza[y-1,x3+1] = 5
                        if x-1 >= 0:
                            self.plansza[y-1,x-1] = 5
                    if x3+1 <= 9:
                        self.plansza[y,x3+1] = 5
                    if x-1 >= 0:
                        self.plansza[y,x-1] = 5
                else:
                    return self.four()

        elif pozpion == 1:
            y1 = y+1
            y2 = y+2
            y3 = y+3
            if y3 > 9:
                return self.four()
            else:
                if self.plansza[y,x] == 0 and self.plansza[y1,x] == 0 and self.plansza[y2,x] == 0 and self.plansza[y3,x] == 0:
                    self.plansza[y,x] = 4
                    self.plansza[y1,x] = 4
                    self.plansza[y2,x] = 4
                    self.plansza[y3,x] = 4
                    if x+1 <= 9:
                        self.plansza[y,x+1] = 5
                        self.plansza[y1,x+1] = 5
                        self.plansza[y2,x+1] = 5
                        self.plansza[y3,x+1] = 5
                        if y3+1 <= 9:
                            self.plansza[y3+1,x+1] = 5
                        if y-1 >= 0:
                            self.plansza[y-1,x+1] = 5
                    if x-1 >= 0:
                        self.plansza[y,x-1] = 5
                        self.plansza[y1,x-1] = 5
                        self.plansza[y2,x-1] = 5
                        self.plansza[y3,x-1] = 5
                        if y3+1 <= 9:
                            self.plansza[y3+1,x-1] = 5
                        if y-1 >= 0:
                            self.plansza[y-1,x-1] = 5
                    if y2+1 <= 9:
                        self.plansza[y3+1,x] = 5
                    if y-1 >= 0:
                        self.plansza[y-1,x] = 5
                else:
                    return self.four()

    def czyszczenie(self):
        y = 0
        while y <= 9:
            x = 0
            while x <= 9:
                if self.plansza[y,x] == 5:
                    self.plansza[y,x] = 0
                x = x+1
            y = y+1
            
    def generator(self):
        try:
            self.four()
            self.three()
            self.three()
            self.two()
            self.two()
            self.two()
            self.one()
            self.one()
            self.one()
            self.one()
            self.czyszczenie()
            np.save(miejscedocelowe,self.plansza,)
        except:
            return self.generator()
if __name__ == "__main__":
    Gracz = Gracz()
    Gracz.generator()
    print(Gracz.plansza)
 
