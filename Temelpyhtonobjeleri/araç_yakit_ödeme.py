yakit_tuketimi = float(input("Aracinizin yakit tüketimini (L/100km) giriniz: "))
kilometre = float(input("Aracinizin kaç kilometre yol yaptiğimi giriniz: "))

# Toplam ödenecek tutar = Yakıt tüketimi * Yol uzunluğu / 100 * ortalama benzin fiyatı
fiyat = float(input("Bir litre benzinin ortalama fiyatini giriniz: "))
toplam_odeme = yakit_tuketimi * kilometre / 100 * fiyat

print("Toplam ödenecek tutar: ", toplam_odeme, "TL")
