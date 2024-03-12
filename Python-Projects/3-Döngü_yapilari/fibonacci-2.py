ilk_basamak = 0
ikinci_basamak = 1
topla = 0
liste = [ilk_basamak, ikinci_basamak]
while True:
    iste = input("Fiboncci sayısı için 1'e basınız. (exit = 'q') :")
    if iste == "1":
        iste2 = int(input("Kaçıncı basamağı görmek istiyorsunuz ? :"))
        
        ilk_basamak, ikinci_basamak = 0, 1
        topla = ilk_basamak + ikinci_basamak
        liste = [ilk_basamak, ikinci_basamak]
        
        if iste2 == 1:
            liste = [ilk_basamak]
            topla = ilk_basamak
        elif iste2 >= 2:
            for i in range(2, iste2):
                ilk_basamak, ikinci_basamak = ikinci_basamak, ilk_basamak + ikinci_basamak
                liste.append(ikinci_basamak)
                topla += ikinci_basamak
                
        print("Toplamı =", topla)
        print("Fibonacci Dizisi:", liste)
        
    elif iste == "q":
        break
