x = input("Lütfen ilk sayiyi girmek için a'ya çikmak için q ya basiniz:")
while True:
    if(x == "a"):
        y = int(input("Lütfen ilk sayiyi giriniz:"))
        z = int(input("Lütfen ikinci sayiyi giriniz:"))
        d = int(input("Lütfen üçüncü sayiyi giriniz:"))
        çarpim = y*z*d
        print("çarpimlari:{}".format(çarpim))
        break
    else:
        print("işlem sonlandiriliyor...")
        break


