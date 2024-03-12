sayi = int(input("Lütfen sayinizi giriniz :"))

i = 1
toplam = 0

while (i < sayi):
    if sayi % i == 0:
        toplam += i
    i += 1

if(toplam == sayi):
    print("bu sayi mükemmel sayidir.")
else:
    print("mükemmel sayi değildir.")