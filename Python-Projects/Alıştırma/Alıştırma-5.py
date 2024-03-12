"""
Kullanıcının girdiği iki sayıyı toplayan ve 
toplam sonucu 40 ile 50 arasında ise ekrana “Başarı” yazdıran python kodlarını yazınız?

"""

sayi1 = int(input("Sayi 1 :"))
sayi2 = int(input("Sayi 2 :"))

topla = sayi1 + sayi2
if 40 <= topla <= 50:
    print("Başarı")

"""
- alternatif yöntem -

for i in range(40,51):
   if (topla == i):
       print("Başarı")
"""