ilk_eleman = 0
ikinci_eleman = 1

liste = [ilk_eleman, ikinci_eleman]

while True:
    a = input(("fibonacciyi görmek için 1 e , çikmak için 'q' ya basiniz :"))
    if(a == "1"):
        b = int(input("kaç adet basamağini görmek istediğinizi sayiyla belirtirmisiniz :"))
        if(b == 1):
            print(ilk_eleman)
        else:
            for i in range(2, b):
                ilk_eleman, ikinci_eleman = ikinci_eleman, ilk_eleman + ikinci_eleman
                liste.append(ikinci_eleman)
            print(liste)
    elif (a == "q"):
        break