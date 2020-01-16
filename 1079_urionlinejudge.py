num = int(input())

for i in range(1 , num + 1 ):
    y = input().split()
    a,b,c = y
    print('{:.1f}'.format((float(a) * 2 + float(b) * 3 + float(c) * 5) / 10))