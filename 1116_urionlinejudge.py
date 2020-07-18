num = int(input(''))

for i in range(1, num + 1):
    a, b = map(int,input().split())
  
    if b == 0:
        print('divisao impossivel')
      
    if b != 0:
        div = a / b
        print('{:.1f}'.format(div))