def pisagor():
      aa = list()
      for i in range (1, 101):
          for j in range(1, 101):
            hipo = (i ** 2 + j ** 2) ** (1/2)
            if (hipo == int(hipo)):
                 aa.append((i,j,int(hipo)))
      return(aa)

for i in pisagor():
      print(i)
