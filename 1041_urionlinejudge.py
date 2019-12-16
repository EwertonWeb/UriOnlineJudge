e = input().split()
a, b = e

a = float(a)
b = float(b)

if a == 0:
    if b == 0:
        print('Origem')
    if b != 0:
        print('Eixo Y')
if b == 0:
    if a != 0:
        print('Eixo X')
if a > 0:
    if b > 0:
        print('Q1')
    if b < 0:
        print('Q4')
if a < 0:
    if b > 0:
        print('Q2')
    if b < 0:
        print('Q3')