note_add = 0 
counter = 0
continuar = True

while continuar==True:
  nota = float(input())
  
  if nota>=0.0 and nota <=10:
    note_add += nota
    counter += 1 

    if counter == 2:
      
      print("media = %.2f"%(note_add/2))
      counter = 0 
      note_add = 0

      while True:
        print("novo calculo (1-sim 2-nao)")
        novo = int(input())
        if novo == 2:
          continuar = False
          break
        elif novo == 1:
          continuar = True
          break
      
  else:
    print("nota invalida")