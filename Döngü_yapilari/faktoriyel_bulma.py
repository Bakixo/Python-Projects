x = int(input("faktöriyelini bulmak istediğiniz sayiyi giriniz :"))

faktoriyel = 1

for a in range(1, x + 1):
    faktoriyel *= x
    x -= 1
print(a, "! =", faktoriyel)
