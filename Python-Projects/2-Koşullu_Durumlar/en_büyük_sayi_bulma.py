print("3 tane sayi giriniz:")

a = int(input("sayi-1 :"))
b = int(input("sayi-2 :"))
c = int(input("sayi-3 :"))

if(a > b and a > c):
    print(a)
elif(b > a and b > c):
    print(b)
else:
    print(c)