#Sıcaklık dönüşüm programı 

"""
f=cx1.8+32
c=(f-32)/1.8
k=c+273.15
c=k-273.15
"""
print("Celsius = 1")
print("Fahrebheit = 2")
print("Kelvin = 3")
birim1=input("Giriş Yapacağınız Sıcaklık Biriminiz Seçiniz:")
deger=float(input("Sıcaklık Değeri Giriniz:"))
birim2=input("Dönüştürmek İstediğiniz Birimi Seçiniz:")
if birim1 == "1" : #celsius
   if birim2== "2" :
       print(deger,"celsius,",float(deger*1.8+32)," fahreit degerine eşittir")
   elif birim2 == "3":
       print(deger,"celsius,",deger+273.15," kelvin değeri:")
   else:
       print("HATA - Giriş yaptığınız birim değerine dönüştürme yapılamaz.")
elif birim1 == "2" : #fahrenheit
   if birim2=="1":
       print(deger,"fahrenheit, celsius değer:",(deger-32)/1.8)
   elif birim2 == "3":
       print(deger,"fahrenheit, kelvin değeri:", (deger-32)/1.8 + 273.15)
   else:
       print("HATA - Giriş yaptığınız birim değerine dönüştürme yapılamaz.")
elif birim1 == "3" : #kelvin
   if birim2=="1":
       print(deger,"kelvin, celsius  değeri:", deger-273.15)
   elif birim2 == "2":
       print(deger,"kelvin, fahrenheit değeri:",(deger-273.15)*1.8+32 )
   else:
       print("HATA - Giriş yaptığınız birim değerine dönüştürme yapılamaz.")
else:
   print("Lütfen 1 ile 3 arasında bir değer seçiniz.")