print("Kilonuzu giriniz")
a = float(input("Kilo:"))
print("Boy uzunluğunuzu giriniz (cm cinsinden)")
b = float(input("Boy (cm):"))

# Boy değerini metre cinsine dönüştürüyoruz ki 185 de 1.85 de aynı sonuç çıksın.
b = b / 100

beden_kitle_indeksi = a / (b * b)
print("Beden kitle indeksi:", beden_kitle_indeksi)
