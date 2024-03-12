# Kullanıcıdan alınan 5 basamaklı sayının basamakları toplamı nasıl bulunur ?

while True:
    sayi = input("5 basamaklı bir sayı giriniz: ")
    if len(sayi) != 5:
        print("Lütfen 5 basamaklı bir sayı girin.")
    else:
        toplam = 0
        for basamak in sayi:
            toplam += int(basamak)
    
        print("Basamaklarının toplamı:", toplam)
        break