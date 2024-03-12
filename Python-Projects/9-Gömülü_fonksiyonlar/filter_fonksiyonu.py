liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]
üçgenler = []

def ucgen_mi(kenarlar):
    a, b, c = kenarlar
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

üçgenler = list(filter(ucgen_mi, liste))
print(üçgenler)
