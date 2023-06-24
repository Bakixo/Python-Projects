def not_hesaplama(satir):
    
    satir = satir[:-1] # isim ve notların sonunuda bulunan \n i kaldırıyoruz.
     
    liste = satir.split(",")   #isim ve notları ayırıyoruz 
    isim = liste[0]
    
    not1 = int(liste[1])
    
    not2 = int(liste[2])
    
    not3 = int(liste[3])
    
    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10) 
    
    if(son_not >= 90):
        harf = "AA"
    elif(son_not >= 85):
        harf = "BA"
    elif(son_not >= 80):
        harf = "BB"
    elif(son_not >= 75):
        harf = "CB"
    elif(son_not >= 70):
        harf = "CC"
    elif(son_not >= 65):
        harf = "DC"
    elif(son_not >= 60):
        harf = "DD"
    elif(son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"
        
    return isim + "------------>" + harf + "\n"
        
with open("notlar.txt","r",encoding= "utf-8") as file:  #bizde olan notlar.txt dosyasından içindekileri alıyoruz
                            #endcoding utf-8 Türkçe karakterler için 
    eklencekler = []
    eklenmeyecekler = []
    for i in file:
        
        eklencekler.append(not_hesaplama(i)) 
        
    with open("sonuç.txt", "w", encoding= "utf-8") as file2:  #çalıştırdığımız an yeni bir txt dosyası açarak kendi istediğimiz şeyleri ekliyor
        
        for i in eklencekler:
            file2.write(i)
    
    

            
