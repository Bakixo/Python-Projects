liste = [(3, 4), (10, 3), (5, 6), (1, 9)]

def alan(kenar):
    x, y = kenar
    return x * y

carpilmis_liste = list(map(alan, liste))
print(carpilmis_liste)
