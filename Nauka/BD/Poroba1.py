import numpy as np

# tworzymy słownik, w ktorym przypisujemy wartości odpowiednio dla dopasowania, niedopasowania i przerwy
pt = {'match': 1, 'mismatch': -1, 'gap': -1}

# tworzymy funkcję, której argumentami są dwa nukleotyd
# i która porównuje je ze sobą i określa, co gdy pasują co gdy nie, oraz co jak jednen z nich jest przerwą
def dopasowanie(nuk1, nuk2):
    if nuk1 == nuk2:
        return pt['match']
    elif nuk1 == '-' or nuk2 == '-':
        return pt['gap']
    else:
        return pt['mismatch']

# funkcja opisująca algorytm needelmana-wunscha
#argumentami są dwie porównywane sekwencje

def algorytm(sekwencja1, sekwencja2):
    m, n = len(sekwencja1), len(sekwencja2)
    score = np.zeros((m + 1, n + 1))    #tworzym macierz, o wielkości sekwencja1 x sekwencja2 + dodajemy po jednym wierszu i jednej kolumnie, z polami wypełnionymi zerami; m+1 to pion, n+1 poziom
    '''Pierwszy wiersz oraz pierwsza kolumna macierzy mogą być po prostu wypełnione zerami,
        gdyż nie ma dopasowania pomiędzy żadnym z nukleotydów żadnej sekwencji z przerwą. 
        Jeśli jednak przyjmiemy, że będziemy zliczać punkty dla dopasowania z przerwą,
        wtedy je sumujemy. Dla pierwszego niedopasowania do przerwy dajemy 0 punktów. 
        Dla drugiego z rzędu niedopasowania do przerwy odejmujemy już 1 punkt. 
        Dla trzeciego z rzędu niedopasowania do przerwy odejmujemy 2 punkty. 
        Czyli przy każdym kolejnym z rzędu niedopasowaniu do przerwy odejmujemy punkt.'''

    for i in range(m + 1):         # nadajemy wartości początkowe dla pierwszego wiersza i pierwszej kolumny
        score[i][0] = pt['gap'] * i
    for j in range(n + 1):
        score[0][j] = pt['gap'] * j
    #print(score) - sprawdzam, czy faktycznie właściwie wypełnia się pierwszy wiersz i kolumna


    # Wypełniamy macierz wartościami według schematu z teorii algorytmu needelman'a - wunscha
    for i in range(1, m + 1):
        for j in range(1, n + 1): #zaznaczamy, że wypełniamy od drugiego wiersza i drugiej kolumny, bo pierwsze już wpisaliśmy powyżej
            przekatna = score[i - 1][j - 1] + dopasowanie(sekwencja1[i - 1], sekwencja2[j - 1]) #wartość po skosie
            pion = score[i - 1][j] + pt['gap'] #wartość z góry
            poziom = score[i][j - 1] + pt['gap'] #wartość z boku
            score[i][j] = max(przekatna, pion, poziom)

    #print('wypełniona macierz : \n%s\n' % score)
    dopasowywana1, dopasowywana2 = '', '' #tworzymy sobie zmienne dla sekwencji po dopasowaniu, do których będziemy dodawać kolejno pozycje
    i, j = m, n #wskazujemy na m i n pod zmienne i i j

    # wyznaczenie trasy od prawego dolnego rogu do lewego górnego po najmniejszych wartościach
    while i > 0 and j > 0: #wyznaczamy dopki nie dojdziemy do pierwszej kolumny i pierwszego wiersza(czyli koonczymy na 2)
        score_biezacy = score[i][j] #oznaczamy zmienne ktore beda porownywane czyli bieżący score i score z przekatnej z gory i z boku
        score_przekatna = score[i - 1][j - 1]
        score_bok = score[i][j - 1]
        score_gora = score[i - 1][j]

        #dla każdego score wyświetlamy sobie jego wartość i wartości opcji, po których mozemy się poruszać
       # print('Bieżący score: ', score_biezacy)
        #print('Następny score po przekątnej: ', score_przekatna)
        #print('Następny score po lewej: ', score_bok)
        #print('Następny score z góry: ', score_gora)

        #robimy warunek, który określa, jak będziemy się poruszać wybierając największe wartości z możłiwych
        if max(score_przekatna, score_bok, score_gora) == score_przekatna:
           # print('Wybór: przekątna')
            nukleotyd1, nukleotyd2 = sekwencja1[i - 1], sekwencja2[j - 1]
            i, j = i - 1, j - 1
        elif max(score_przekatna, score_bok, score_gora) == score_gora:
            #print('Wybór: góra')
            nukleotyd1, nukleotyd2 = sekwencja1[i - 1], '-'
            i -= 1
        elif max(score_przekatna, score_bok, score_gora) == score_bok:
            #print('Wybór: bok')
            nukleotyd1, nukleotyd2 = '-', sekwencja2[j - 1]
            j -= 1

       # print('%s ---> nukleotyd z sekwencji 1 = %s\t nukleotyd z sekwencji 2 = %s\n' % ('Dodajemy do dopasowania', nukleotyd1, nukleotyd2)) #pokazujemy wynik porównania danych pozycji
        dopasowywana1 += nukleotyd1
        dopasowywana2 += nukleotyd2  #dodajemy kolejną pozycje do dopasowania

    # while i > 0:   #nie jestem pewna czy ten zahaszowany fragment jest potrzebny, wydaje mi sie ze while z góry jest ok dla każdego przypadku, ale sprawdź moze jeszcze ty
    #     a1, a2 = sekwencja1[i - 1], '-'
    #     print('%s ---> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
    #     align1 += a1
    #     align2 += a2
    #     i -= 1
    #
    # while j > 0:
    #     a1, a2 = '-', sekwencja2[j - 1]
    #     print('%s --> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
    #     align1 += a1
    #     align2 += a2
    #     j -= 1

    dopasowywana1 = dopasowywana1[::-1]
    dopasowywana2 = dopasowywana2[::-1] # obracamy sobie dopasowane sekwencje, zeby były od lewej do prawej, a nie tak je odczytywalismy z macierz od prawej do lewej
    sekwencja = len(dopasowywana1)
    wspolne = ''#wprowadzamy zmienna wspolne, ktora z gory ma przypisana wartosc pusta,
                # ale gdy nukletoyd z sekwencji1 bedzie taki sam jak z drugiej, to bedzi on wyswietlany
                #co jest opisane niżej w pętli for

    wsp_dopasowania = 0 #zmienna która pokaże ogólne dopasowanie obliczone na podstawie poszczegołnych dopasowań
    procent = 0 #zmienna gdzie policzymy procent identycznosci sekwencji
    for i in range(sekwencja):
        d1 = dopasowywana1[i]
        d2 = dopasowywana2[i]
        if d1 == d2:
            wspolne += d1
            procent += 1
            wsp_dopasowania += dopasowanie(d1, d2) #dodajemy wartości kolejnych dopasowań, żeby uzyskać ogolne dopasowanie

        else:
            wsp_dopasowania += dopasowanie(d1, d2) #dodajemy wartości kolejnych niedopasowań(lub gap), żeby uzyskać ogolne dopasowanie
            wspolne += ' '

    procent = procent / sekwencja * 100 #liczymy ile identycznych na cala sekwencje

   # print('Identyczność = %2.1f procent' % procent)
   # print('Dopasowanie na poziomie = %d\n' % wsp_dopasowania)
   # print(dopasowywana1)
   # print(wspolne)
   #print(dopasowywana2)

    return wsp_dopasowania



