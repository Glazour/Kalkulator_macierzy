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
        return f"{self.nazwa}({self.kolumny}x{self.wiersze}) {self.typ}"

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
def operacje(lista_macierzy, i):
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
rownanie = 0
rown_index = 0
nowa_macierz = macierze(
    nazwa = "nowa",
    typ = "wpisanej"
)
#####################################################
###################WIP###############################
#####################################################
# if len(lista_macierzy) > 1:
#     for i in range(len(lista_macierzy)):
#         if "niewiadoma" in lista_macierzy[i].typ:
#             for i in range(len(lista_macierzy)-1):
#               niew += 1
#               niew_index = i
#               lista_macierzy[i].operator = input("Podaj operator +, -, *, = między macierzą " + f"{lista_macierzy[i]}" + ", a macierzą " + f"{lista_macierzy[i+1]}")
#         if lista_macierzy[i].operator == "=":
#             rownanie += 1
#             rown_index = i
#     if niew == 1 and rownanie == 1:
#         nowe_rownanie = list()
#         if niew_index == 0:
#             if rown_index == 0:
#                 for i in range(1, len(lista_macierzy)-1):
#                     nowa_macierz.macierz = operacje(lista_macierzy, i)
#             else:
#                 for i in range(1, rown_index):
#                     nowa_macierz.macierz = operacje(lista_macierzy, i)
#         else:
#             if rown_index < niew_index:
#                 print("Niewiadoma ma być po lewej stronie równania")
#                 exit()
#             if niew_index == 1:
#                 nowa_macierz.macierz = lista_macierzy[0]
#                 nowe_rownanie.append(nowa_macierz)
#             else:
#                 for i in range(0, niew_index-2):
#                     nowa_macierz.macierz = operacje(lista_macierzy, i)
#                 nowe_rownanie.append(nowa_macierz)
#             if niew_index+1 != rown_index:
#                 for i in range(niew_index+1, rown_index-1):
#                     nowa_macierz.macierz = operacje(lista_macierzy, i)
#                 nowe_rownanie.append(nowa_macierz)
#             else:
#                 nowe_rownanie.append(lista_macierzy[niew_index+1])
#             if nowe_rownanie[0].operator == "+" or nowe_rownanie[0].operator == "-":
#                 nowe_rownanie[1].kolumny = nowe_rownanie[0].kolumny
#                 nowe_rownanie[1].wiersze = nowe_rownanie[0].wiersze
#             nowe_rownanie[1].kolumny = nowe_rownanie[rown_index+1].kolumny
#             nowe_rownanie[1].wiersze = nowe_rownanie[rown_index+1].wiersze
#             elif nowe_rownanie[0].operator == "*":
#                 nowe_rownanie[1].kolumny = nowe_rownanie[0].wiersze
#                 nowe_rownanie[1].wiersze = nower_rownanie[2].kolumny
#             nowe_rownanie.append(lista_macierzy[niew_index])
#
#             if rown_index+1 != len(lista_macierzy)-1:
#                 for i in range(rown_index+1, len(lista_macierzy)-1):
#                     nowa_macierz = operacje(lista_macierzy, i)
#                     nowe_rownanie.append(nowa_macierz)
#             else:
#                 nowe_rownanie.append(lista_macierzy[rown_index+1])
#
#
#
#
# for i in range(len(lista_macierzy)-1):
#     if lista_macierzy[i].typ == "niewiadoma" and i != 0:
#         pass
#     if lista_macierzy[i].typ == "niewiadoma" and lista_macierzy[i].operator == "=":
#         pass
##########################################################################################
nowa_macierz = lista_macierzy[0].macierz

for i in range(len(lista_macierzy)-1):
    lista_macierzy[i].operator = input("Podaj operator +, -, *, = między macierzą " + f"{lista_macierzy[i]}" + ", a macierzą " + f"{lista_macierzy[i+1]}")
    nowa_macierz = operacje(lista_macierzy, i)
for wiersz in range(len(nowa_macierz)):
    for kolumna in range(len(nowa_macierz[0])):
            nowa_macierz[wiersz][kolumna] = round(float(nowa_macierz[wiersz][kolumna]),2)
for row in nowa_macierz:
    print(row)


