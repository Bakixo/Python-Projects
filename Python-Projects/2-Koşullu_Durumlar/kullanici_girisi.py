print("""*****************************
KULLANICI GİRİŞİ

*****************************
""")

kullanici_adi = "baki"
sifre = "1234"
deneme_hakki = 5

print("Lütfen kullanici adi ve şifre giriniz:")
kullanici_adi1 = input("kullanici adi :")

while True:
    if(kullanici_adi1 == kullanici_adi):
        sifre1 = input("şifrenizi giriniz :")
        if(sifre1 == sifre):
            print("hoşgeldiniz...")
            break
        else:
            print("sifreniz yanlistir tekrar giriniz")
            deneme_hakki -= 1
    elif(deneme_hakki == 0):
        print("deneme hakkiniz bitmiştir daha sonra tekrar deneyiniz...")
        break
    else:
        print("kullanici adiniz yanlis girilmistir tekrar deneyiniz")
        deneme_hakki -= 1
        kullanici_adi1 = input("Kullanici adinizi giriniz : ")
