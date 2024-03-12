def ekok_bulma(sayi1, sayi2):
      i = 1
      while True:
            if(i % sayi1 == 0 and i % sayi2 == 0):
                  return i
            i += 1
            
                        
sayi1 = int(input("sayi 1 :"))
sayi2 = int(input("sayi 2 :"))

print("Sayilarin ekoku: ", ekok_bulma(sayi1, sayi2))