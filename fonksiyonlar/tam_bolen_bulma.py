liste = []
def tam_bolen_bulma(sayi):
      for i in range(1, sayi + 1):
          if(sayi % i == 0):
            liste.append(i)
            i += 1
      print(liste)

while True:
    sayi = input("Sayinizi giriniz (cikmak icin q'ya basiniz): ")
    if sayi == 'q':
        break
    try:
        sayi = int(sayi)
    except ValueError:
        print("Gecersiz girdi.")
        continue
    tam_bolen_bulma(sayi)