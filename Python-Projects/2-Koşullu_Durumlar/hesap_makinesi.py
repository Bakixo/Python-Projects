print("""

1-Toplama
2-Çikartma                      #if 
3-Çarpma
4-Bölme 

q- çikiş

""", "işlem:")
x = input(("Lütfen işlem numarasini giriniz:"))

while True:

    if(x == "1"):
        a = (input("sayi1 :"))
        b = (input("sayi2 :"))
        toplam = a+b
        print(toplam)
        break
    elif(x == "2"):
        a = int(input("sayi1 :"))
        b = int(input("sayi2 :"))
        çikarma = a-b
        print(çikarma)
        break
    elif(x == "3"):
        a = int(input("sayi1 :"))
        b = int(input("sayi2 :"))
        çarpma = a * b
        print(çarpma)
        break
    elif(x == "4"):
        a = int(input("sayi1 :"))
        b = int(input("sayi2 :"))
        bölme = a / b
        print(bölme)
        break
    elif(x == "q" or x == "Q"):
        break
    else:
        print("Lütfen geçerli bir durum giriniz!")
        x = input("Lütfen işlem numarasini giriniz: ")
        