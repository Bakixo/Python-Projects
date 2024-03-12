"""
Klavyeden kullanıcının girdiği 3 adet integer türünde ki sayıyı büyükten küçüğe sıralayarak ortadaki sayı ile olan sayının arasındaki farkı ve yine ortadaki sayı ile küçük olan sayı ile arasındaki farkı ekrana yazdıran python kodlarını yazınız?

örneğin kullanıcının girdiği sayı; 45, 195, 22
örnek ekran çıktısı:
     büyük sayı ile ortadaki sayı arasındaki fark: 150
     küçük sayı ile ortadaki sayı arasındaki fark: 23

"""

mylist=[]
while True:
   mylist.append(int(input("değer girniz:")))
   if (len(mylist) >= 3):
       break
mylist.sort()
mylist.reverse()
print(mylist)
print("büyük sayı ile ortadaki sayının farkı=",max(mylist) - mylist[1])
print("küçük sayı ile ortadaki sayının farkı=", mylist[1] - min(mylist))