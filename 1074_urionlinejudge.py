num = int(input())
y =['']
for z in range(1,num + 1):
    y.append(int(input()))
   
for z in range(1,num + 1):
    if y[z] == 0:
        print('NULL')
       
    if y[z] > 0:
        if y[z] % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
           
    if y[z] < 0:
        if y[z] % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')