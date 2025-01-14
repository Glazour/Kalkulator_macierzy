import numpy as np
class macierze:
    def __init__(self, nazwa, typ, macierz = None, kolumny = None, wiersze = None, operator = None):
        self.nazwa = nazwa
        self.typ = typ
        self.macierz = macierz
        self.kolumny = kolumny
        self.wiersze = wiersze
        self.operator = operator
    def __str__(self):
        return (f"{self.nazwa}({self.kolumny}x{self.wiersze}) {self.typ}")
    def kol_i_wie(self):
        self.wiersze = len(self.macierz)
        self.kolumny = len(self.macierz[0])

def dodawanie(macierz1, macierz2):
    return macierz1+macierz2
def odejmowanie(macierz1, macierz2):
    return macierz1-macierz2
def mnozenie(macierz1, macierz2):
    macierz1 = np.array(macierz1, dtype = float)
    macierz2 = np.array(macierz2, dtype = float)
    return macierz1.dot(macierz2)
def transpozycja(macierz1):
    macierz1 = macierz1.transpose()
    return macierz1
def determinant(macierz1):
    det = np.linalg.det(macierz1)
    return det
def jednostkowa(stopien):
    return np.eye(stopien, dtype = float)
def przesuniecie(x, y):
    return np.array([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1]
    ], dtype = float)
def odbicia():
    os = input("Odbicie względem - środka (s), x, y, czy niestandardowej x (x1) lub niestandardowej y (y1)")
    if os == "s":
        return np.array([
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ], dtype = float)
    elif os.lower == "x":
        return np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ], dtype = float)
    elif os.lower == "y":
        return np.array([
            [-1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype = float)
    elif os.lower == "x1":
        prosta = input("podaj współrzędną x")
        return np.array([
            [-1, 0, prosta],
            [0, 1, 0],
            [0, 0, 1]
        ], dtype = float)
    elif os.lower == "y1":
        prosta = input("podaj współrzędną y")
        return np.array([
            [-1, 0, 0],
            [0, 1, prosta],
            [0, 0, 1]
        ], dtype = float)
    else:
        print("Blad, nie ma takiego odbicia")
        return 0
def odwrotna(macierz1):
    macierz1 = np.array(macierz1, dtype = float)
    if determinant(macierz1) == 0:
        print("Ta macierz nie ma macierzy odwrotnej")
        return 0
    else:
        return np.linalg.inv(macierz1)
def obrotu(stopnie):
    stopnie = np.radians(int(stopnie))
    return np.array([
        [np.cos(stopnie), -np.sin(stopnie), 0],
        [np.sin(stopnie), np.cos(stopnie), 0],
        [0 , 0, 1]
    ], dtype = float)
def wpisanie_macierzy():
    kolumny = int(input("Ile kolumn ma macierz?"))
    wiersze = int(input("Ile wierszy ma macierz?"))
    if kolumny <= 0 or wiersze <= 0:
        print("Niepoprawna macierz")
        return 0
    wielkosc = kolumny * wiersze
    elementy = list()
    for element in range(wielkosc):
        elementy.append(input("Podaj "+str(element+1)+" element macierzy (wierszami) "))
    return np.array(elementy, dtype = float).reshape(wiersze, kolumny)
def operacje(nowa_macierz, lista_macierzy, i):
    if lista_macierzy[i].operator == "+":
        return dodawanie(nowa_macierz, lista_macierzy[i + 1].macierz)
    elif lista_macierzy[i].operator == "-":
        return odejmowanie(nowa_macierz, lista_macierzy[i + 1].macierz)
    else:
        return mnozenie(nowa_macierz, lista_macierzy[i + 1].macierz)




ilosc = int(input("Podaj ile macierzy jest w rownaniu"))
lista_macierzy = list()


for i in range(1, ilosc+1):
    typ_macierzy = input("Podaj typ "+str(i)+" macierzy (zwykla[z]\nobrotu[obr]\nprzesunięcia[p]\nodbicia[odb]\njednostkowa[j]\nodwrotna[odw]\noblicz[obl] (oblicza det)\ntransponowana[t]\n").lower()
    if typ_macierzy == "z":
        typ_macierzy = "wpisanej"
        nowa_macierz = wpisanie_macierzy()
    elif typ_macierzy == "obr":
        typ_macierzy = "obrotu"
        st = input("O ile stopni chcesz obrocic?")
        nowa_macierz = obrotu(st)
    elif typ_macierzy == "p":
        typ_macierzy = "przesunięcia"
        x = input("O ile x?")
        y = input("O ile y?")
        nowa_macierz = przesuniecie(x, y)
    elif typ_macierzy == "odb":
        typ_macierzy = "odbicia"
        nowa_macierz = odbicia()
    elif typ_macierzy == "j":
        typ_macierzy = "jednostkową"
        st = input("Którego stopnia?")
        nowa_macierz = jednostkowa(int(st))
    elif typ_macierzy == "odw":
        typ_macierzy = "odwrotną"
        nowa_macierz = odwrotna(wpisanie_macierzy())
    elif typ_macierzy == "obl":
        print(determinant(wpisanie_macierzy()))
    elif typ_macierzy == "t":
        typ_macierzy = "transponowaną"
        nowa_macierz = transpozycja(wpisanie_macierzy())
    elif typ_macierzy == "n":
        typ_macierzy = "niewiadoma"
    else:
        typ_macierzy = "jednostkowa"
        nowa_macierz = jednostkowa(3)
    if typ_macierzy != "niewiadoma":
        lista_macierzy.append(macierze(
            nazwa = f"macierz_{i}",
            typ = typ_macierzy,
            macierz = nowa_macierz,
            kolumny = len(nowa_macierz[0]),
            wiersze = len(nowa_macierz)
        ))
    else:
        lista_macierzy.append(macierze(
            nazwa=f"macierz_{i}",
            typ=typ_macierzy,
        ))
niew = 0
niew_index = 0
new_niew_index = 0
rownanie = 0
rown_index = 0
new_rown_index = 0
nowe_rownanie = list()
nowa_macierz = macierze(
    nazwa = "nowa",
    typ = "wpisanej"
)
for i in range(len(lista_macierzy)):
    if "niewiadoma" in lista_macierzy[i].typ:
          niew += 1
          niew_index = i
          for i in range(len(lista_macierzy) - 1):
            lista_macierzy[i].operator = input("Podaj operator +, -, *, = między macierzą " + f"{lista_macierzy[i]}" + ", a macierzą " + f"{lista_macierzy[i+1]}")
for i in range(len(lista_macierzy)):
  if lista_macierzy[i].operator == "=":
        rownanie += 1
        rown_index = i
if (niew == 0 and rownanie == 1) or (niew == 1 and rownanie == 0) or (niew_index > rown_index):
    print("Nie mozna rozwiazac rownan bez znaku =, bądź bez niewiadomej")
    exit()
if rownanie == 1 and niew == 1:
###########DLA INDEXU 0#############
    if(niew_index == 0):
        new_niew_index = 0
        if niew_index == rown_index:
            nowe_rownanie.append(lista_macierzy[0])
            nowa_macierz = lista_macierzy[1]
            for i in range(1, len(lista_macierzy)-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)
        else:
            nowe_rownanie.append(lista_macierzy[0])
            nowa_macierz = lista_macierzy[1]
            for i in range(1, rown_index-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowa_macierz.operator = "="
            nowe_rownanie.append(nowa_macierz)
            nowa_macierz = lista_macierzy[rown_index+1]
            for i in range(rown_index+1, len(lista_macierzy)-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)
#######DLA INDEXU 1#################################
    elif(niew_index == 1):
        new_niew_index = 1
        if niew_index == rown_index:
            nowe_rownanie.append(lista_macierzy[0])
            nowe_rownanie.append(lista_macierzy[1])
            nowa_macierz = lista_macierzy[2]
            for i in range(2, len(lista_macierzy)-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)
        else:
            nowe_rownanie.append(lista_macierzy[0])
            nowe_rownanie.append(lista_macierzy[1])
            nowa_macierz = lista_macierzy[2]
            for i in range(2, rown_index-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowa_macierz.operator = "="
            nowe_rownanie.append(nowa_macierz)
            nowa_macierz = lista_macierzy[rown_index+1]
            for i in range(rown_index+1, len(lista_macierzy)-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)
######################DLA INNEGO INDEXU#############################
    elif niew_index == 2:
        new_niew_index = 1
        if niew_index == rown_index:
            nowa_macierz = lista_macierzy[0]
            nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, 0)
            nowa_macierz.operator = lista_macierzy[1].operator
            nowe_rownanie.append(nowa_macierz)
            nowe_rownanie.append(lista_macierzy[niew_index])
            nowa_macierz = lista_macierzy[3]
            for i in range(3, len(lista_macierzy) - 1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)
        else:
            nowa_macierz = lista_macierzy[0]
            nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, 0)
            nowa_macierz.operator = lista_macierzy[1].operator
            nowe_rownanie.append(nowa_macierz)
            nowe_rownanie.append(lista_macierzy[niew_index])
            nowa_macierz = lista_macierzy[3]
            for i in range(3, rown_index - 1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowa_macierz.operator = "="
            nowe_rownanie.append(nowa_macierz)
            nowa_macierz = lista_macierzy[rown_index + 1]
            for i in range(rown_index + 1, len(lista_macierzy) - 1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)
    else:
        if niew_index == rown_index:
            nowa_macierz = lista_macierzy[0]
            for i in range(0, niew_index-2):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowa_macierz.operator = lista_macierzy[niew_index-1].operator
            nowe_rownanie.append(nowa_macierz)
            nowe_rownanie.append(lista_macierzy[niew_index])
            new_niew_index = len(nowe_rownanie)
            nowa_macierz = lista_macierzy[niew_index+1]
            for i in range(niew_index+1, rown_index-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowa_macierz.operator = "="
            nowa_macierz = lista_macierzy[rown_index+1]
            nowe_rownanie.append(nowa_macierz)
            for i in range(rown_index+1, len(lista_macierzy)-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)
        else:
            nowa_macierz = lista_macierzy[0]
            for i in range(0, niew_index-2):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowa_macierz.operator = lista_macierzy[niew_index-1].operator
            nowe_rownanie.append(nowa_macierz)
            nowe_rownanie.append(lista_macierzy[niew_index])
            new_niew_index = len(nowe_rownanie)
            nowa_macierz = lista_macierzy[niew_index+1]
            for i in range(niew_index+1, rown_index-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowa_macierz.operator = "="
            nowe_rownanie.append(nowa_macierz)
            nowa_macierz = lista_macierzy[rown_index+1]
            for i in range(rown_index+1, len(lista_macierzy)-1):
                nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
            nowe_rownanie.append(nowa_macierz)

    for i in range(len(nowe_rownanie)):
        if nowe_rownanie[i].operator == "=":
            new_rown_index = i
        if i != new_niew_index:
            nowe_rownanie[i].nazwa = f"nowa_macierz_{i+1}"
            nowe_rownanie[i].kol_i_wie()

    if new_niew_index > 0:
        if nowe_rownanie[new_niew_index-1].operator == "*":
            nowe_rownanie[new_niew_index].wiersze = nowe_rownanie[new_niew_index-1].kolumny
        elif nowe_rownanie[new_niew_index-1].operator == "+" or nowe_rownanie[new_niew_index-1].operator == "-":
            nowe_rownanie[new_niew_index].wiersze = nowe_rownanie[new_niew_index-1].wiersze
            nowe_rownanie[new_niew_index].kolumny = nowe_rownanie[new_niew_index-1].kolumny

        if nowe_rownanie[new_niew_index+1].operator == "*":
            if nowe_rownanie[new_niew_index].kolumny is None or nowe_rownanie[new_niew_index].kolumny == nowe_rownanie[new_niew_index + 1].wiersze:
                nowe_rownanie[new_niew_index].kolumny = nowe_rownanie[new_niew_index + 1].wiersze
            elif nowe_rownanie[new_niew_index].kolumny != nowe_rownanie[new_niew_index + 1].wiersze:
                print("Podane zle wymiary macierzy")
                exit()
        elif nowe_rownanie[new_niew_index+1].operator == "+" or nowe_rownanie[new_niew_index + 1].operator == "-":
            if (nowe_rownanie[new_niew_index].kolumny == None and nowe_rownanie[new_niew_index].wiersze == nowe_rownanie[new_niew_index + 1].wiersze) or (nowe_rownanie[new_niew_index].kolumny == nowe_rownanie[new_niew_index + 1].kolumny):
                nowe_rownanie[new_niew_index].kolumny = nowe_rownanie[new_niew_index + 1].kolumny
                nowe_rownanie[new_niew_index].wiersze = nowe_rownanie[new_niew_index + 1].wiersze
            else:
                print("Podane zle wymiary macierzy")
                exit()
        if nowe_rownanie[new_niew_index].kolumny is None:
            nowe_rownanie[new_niew_index].kolumny = nowe_rownanie[len(nowe_rownanie)-1].kolumny
        if nowe_rownanie[new_niew_index].wiersze is None:
            nowe_rownanie[new_niew_index].wiersze = nowe_rownanie[len(nowe_rownanie)-1].wiersze
    else:
        if nowe_rownanie[new_niew_index + 1].operator == "*":
            nowe_rownanie[new_niew_index].kolumny = nowe_rownanie[new_niew_index + 1].wiersze
        elif nowe_rownanie[new_niew_index + 1].operator == "+" or nowe_rownanie[new_niew_index + 1].operator == "-":
            nowe_rownanie[new_niew_index].wiersze = nowe_rownanie[new_niew_index + 1].wiersze
            nowe_rownanie[new_niew_index].kolumny = nowe_rownanie[new_niew_index + 1].kolumny
        if nowe_rownanie[new_niew_index].kolumny is None:
            nowe_rownanie[new_niew_index].kolumny = nowe_rownanie[len(nowe_rownanie)-1].kolumny
        if nowe_rownanie[new_niew_index].wiersze is None:
            nowe_rownanie[new_niew_index].wiersze = nowe_rownanie[len(nowe_rownanie)-1].wiersze
    if len(nowe_rownanie) == 2:
        if (nowe_rownanie[0].kolumny == nowe_rownanie[1].kolumny and nowe_rownanie[0].wiersze == nowe_rownanie[1].wiersze):
            nowe_rownanie[0].kolumny = nowe_rownanie[1].kolumny
            nowe_rownanie[0].wiersze = nowe_rownanie[1].wiersze
            for row in nowe_rownanie[1].macierz:
                print(row)
                exit()
        else:
            print("Podano zle wymiary macierzy")
            exit()
    elif len(nowe_rownanie) == 3:
        if new_niew_index == 0:
            if nowe_rownanie[0].operator == "*" and nowe_rownanie[0].kolumny == nowe_rownanie[2].kolumny and nowe_rownanie[1].wiersze == nowe_rownanie[2].wiersze:
                nowa_macierz.macierz = np.linalg.solve(nowe_rownanie[1].macierz, nowe_rownanie[2].macierz)
                for row in nowa_macierz.macierz:
                    print(row)
                    exit()
            elif nowe_rownanie[0].operator == "+":
                nowa_macierz.macierz = odejmowanie(nowe_rownanie[2].macierz, nowe_rownanie[1].macierz)
                for row in nowa_macierz.macierz:
                    print(row)
                    exit()
            elif nowe_rownanie[0].operator == "-":
                nowa_macierz.macierz = (nowe_rownanie[2].macierz, nowe_rownanie[1].macierz)
                for row in nowa_macierz.macierz:
                    print(row)
                    exit()
            else:
                print("Podano zle wymiary macierzy")
    else:
        for i in range(len(nowe_rownanie)):
            print(nowe_rownanie[i])
        print(new_niew_index)
        macierz1_wektory = np.reshape(nowe_rownanie[0].macierz, (nowe_rownanie[0].wiersze, -1))
        A = np.kron(macierz1_wektory.T, nowe_rownanie[2].macierz.T)  # Kronecker product
        B = np.reshape(nowe_rownanie[3].macierz, (-1,))
        X_vektory = np.linalg.solve(A, B)
        nowe_rownanie[1].macierz = np.reshape(X_vektory, (nowe_rownanie[0].kolumny, nowe_rownanie[3].wiersze))
        for wiersz in range(nowe_rownanie[1].wiersze):
            for kolumna in range(nowe_rownanie[1].kolumny):
                nowe_rownanie[1].macierz[wiersz][kolumna] = round(float(nowe_rownanie[1].macierz[wiersz][kolumna]), 2)
        for row in nowe_rownanie[1].macierz:
            print(row)
else:
    nowa_macierz.macierz = lista_macierzy[0]
    for i in range(len(lista_macierzy)-1):
        nowa_macierz.macierz = operacje(nowa_macierz.macierz, lista_macierzy, i)
    for wiersz in range(len(nowa_macierz.macierz)):
        for kolumna in range(len(nowa_macierz.macierz[0])):
            nowa_macierz.macierz[wiersz][kolumna] = round(float(nowa_macierz.macierz[wiersz][kolumna]),2)
    for row in nowa_macierz.macierz:
        print(row)




