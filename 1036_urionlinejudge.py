from math import sqrt

x, y, z = [float(x) for x in input().split(" ")]

try:
    delta = y * y - 4 * x * z
    r1 = (-y + sqrt(delta)) / (2 * x)
    r2 = (-y - sqrt(delta)) / (2 * x)

    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
except:
        print('Impossivel calcular')