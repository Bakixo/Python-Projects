"""
Kullanıcının girdiği iki birbirine eşit ise ekrana “5” sonucu yazdıracak, 
eşit değil ise 25 defa “eşit değil” sonucunu ekrana yazdıran python kodlarını yazınız? (while döngüsü ile yapılacaktır)

"""


sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

while sayi1 != sayi2:
    print("eşit değil \n"*20)
    break
if sayi1 == sayi2:
    print("5")
