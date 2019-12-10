a, b, c, =input('').split()
valores = a,b,c
num1 = int(a)
num2 = int(b)
num3 = int(c)

maior = (int(a) + int(b) + abs(int(a) - int(b))) / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print('{:.0f} eh o maior'.format(resultado))