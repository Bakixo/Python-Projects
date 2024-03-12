birler = ["", "bir", "iki", "üç", "dört", "beş", "alti", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kirk", "elli", "altmiş", "yetmiş", "seksen","doksan"]

def okunuş(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10
    return (onlar[ikinci] + " " + birler[birinci])

sayi = int(input("sayiniz giriniz : "))
print(okunuş(sayi))