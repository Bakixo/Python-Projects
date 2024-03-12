"""
Rastgele 600 adet 0 ile 1000 arasında sayı oluşturup 
bir liste içerisine aktaran ve 100’den küçük olan sayıların adedini ekrana yazdıran python kodlarını yazınız?

""" 

import random

rastgele_sayilar = [random.randint(0, 1000) for sayac in range(600)]
liste = []

for i in rastgele_sayilar:
    if i < 100:
        liste.append(i)
print(liste)