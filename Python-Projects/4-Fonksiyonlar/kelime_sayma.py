strin = "Tabi Siz Anneleri Tarafından Size Emanet Edilen Çocuklara Her Bakımdan Yetersiz Gördüğünüz Bir Kadının Annelik Etmesine Şiddetle Karşısınız Ama."


def saygardas(str):
    say = 0
    for i in str.lower().split():
        if i[:4] == "anne":
            say += 1 
    print(say)

saygardas(strin)