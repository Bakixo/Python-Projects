x = input(("lütfen şeklinizi giriniz:"))

while True:
    if(x == "Dörtgen" or x == "dörtgen"):
        print("kenarlari giriniz:")
        kenar1 = int(input("kenar 1 : "))
        kenar2 = int(input("kenar 2 : "))
        kenar3 = int(input("kenar 3 : "))
        kenar4 = int(input("kenar 4 : "))
        if(kenar1 == kenar2 == kenar3 == kenar4):
         print("kare.")
         break
        elif(kenar1 == kenar2 and kenar3 == kenar4):
            print("diktörtgen.")
            break
        else:
            print("Dörtgen.")
            break
    elif(x == "Üçgen" or x == "üçgen"):
        print("kenarlari giriniz:")
        kenar11 = int(input("kenar 1 : "))
        kenar22 = int(input("kenar 2 : "))
        kenar33 = int(input("kenar 3 : "))
        if( abs(kenar11 + kenar22 ) > kenar33 and abs(kenar22 + kenar33) > kenar11 and abs(kenar11 + kenar33) > kenar22):
            if((kenar11 == kenar22 and kenar11 != kenar33) or (kenar11 == kenar33 and kenar11 != kenar22) or (kenar22 == kenar33 and kenar22 != kenar11 )):
                print("ikizkenar.")
                break
            elif(kenar11 == kenar22 == kenar33):
                print("eşkenar.")
                break
            else:
                print("siradan üçgen.")
                break
        else:
            print("üçgen belirtmiyor")
    else:
        print("Lütfen geçerli bir şekil giriniz!")
        x = input(("lütfen şeklinizi giriniz:"))