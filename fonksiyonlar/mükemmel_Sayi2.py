liste = []
def mükemmel_Sayi(sayi):
      for i in range(1, 1001):
          if(sayi % i == 0):
                if(i < sayi):     
                  liste.append(i)
                  i+= 1
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
    mükemmel_Sayi(sayi)
    if(sum(liste) == sayi):
        print("mükemmel sayidir. ")
        break
    else:
        print("mükemmel değildir.")
        break