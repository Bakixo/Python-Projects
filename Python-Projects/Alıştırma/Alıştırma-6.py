"""
Kullanıcının girdiği 4 basamaklı sayıyı basamaklarını ayırıp 
tek tek rakamlarını ve rakamlarının toplamını ekrana yazdıran python kodlarını yazınız?

"""
while True:

    sayi = int(input("Sayi : "))
    liste1 = []
    topla = 0
    sayi_str = str(sayi)
    if len(sayi_str) == 4:
        for i in sayi_str:
            liste1.append(i)
            topla += int(i)
        print(liste1)
        print(topla)
        break
    else:
        print("4 basamaklı bir sayı giriniz!")
