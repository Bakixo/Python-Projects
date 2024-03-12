def harf_ekleme():
    bas_harf = ""
    with open("şiir.txt","r",encoding="utf-8") as file:
        for satir in file:
            bas_harf += satir[0]          
    print(bas_harf)
harf_ekleme()