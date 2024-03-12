a = float(input("Lütfen kilonuzu giriniz :"))
b = int(input("Lütfen boyunuzu giriniz(cm cinsinden) :"))

"""
if(b == float(b)):
    print("boyunuzu cm cinsinden tekrar giriniz :")
    b = int(input("boyunuz :"))
"""    

b = b / 100
bki = a / (b * b)

while True:
    if(bki >= 30):  
        print("Obez.")
        break
    elif(bki >= 25 and bki < 30):   
        print("Fazla kilolu.")
        break
    elif(bki >= 18.5 and bki < 25): 
        print("Normal.")
        break
    elif(bki <= 18.5):
        print("Zayif.")
        break