print("""***********
NOTLANDIRMA
**********""")

vize1 = int(input("vize 1 sinav notunu giriniz :"))
vize2 = int(input("vize 2 sinav notunu giriniz :"))
final = int(input("final sinav notunu giriniz :"))

Toplam_not = (vize1 * (3 / 10)) + (vize2 * (3 / 10)) + (final * (4 / 10))

if(Toplam_not >= 90):
    print("Notunuz : AA")
elif(Toplam_not >= 85):
    print("Notunuz : BA")
elif(Toplam_not >= 80):
    print("Notunuz : BB")
elif(Toplam_not >= 75):
    print("Notunuz : CB")
elif(Toplam_not >= 70):
    print("Notunuz : CC")
elif(Toplam_not >= 65):
    print("Notunuz : DC")
elif(Toplam_not >= 60):
    print("Notunuz : DD")
elif(Toplam_not >= 55):
    print("Notunuz : FD")
elif(Toplam_not >= 50):
    print("Notunuz : FF")
