print("""**********************
İşlemler ;
1. Bakiye sorgulama

2. Para yatirma 

3. Para çekme 

programdan çikmak için 'q' ya basiniz
***********************""")

bakiye = 1000

while True:
    x = input("Seçiminiz : ")
    if (x == "1"):
        print(bakiye, "TL")
    elif(x == "2"):
        yatirma_bakiyesi = int(input("yatirmak istediğiniz bakiyeyi giriniz :"))
        bakiye += yatirma_bakiyesi
        print("Para yatirilmiştir.")
    elif(x == "3"):
        çekme_bakiyesi = int(input("Çekmek istediğiniz para miktarini giriniz :"))
        if(bakiye < çekme_bakiyesi):
            print("bakiyeniz yetersiz...")
        elif(çekme_bakiyesi == 0):
            print("çekmek için geçerli bir para giriniz")
        else:
            bakiye -= çekme_bakiyesi
            print("Güle Güle harcayiniz.")
    elif(x == "q"):
        print("hoşçakalin...")
        break
    else:
        print("geçerli bir seçim yapiniz!")
