def asal_Sayi_bulma(sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return False
        return True

while True:
    sayi = input("Sayinizi giriniz (cikmak icin q'ya basiniz): ")
    if sayi == 'q':
        break
    try:
        sayi = int(sayi)
    except ValueError:
        print("Gecersiz girdi.")
        continue
    if asal_Sayi_bulma(sayi):
        print("asaldir.")
    else:
        print("asal degildir.")