b = []
for i in range(5):
    t = int(input())
    b.append(int(t))

v = 0
x = 0
y = 0
z = 0
for j in range(5):
    if b[j] % 2 == 0:
        v += 1
    if b[j] % 2 == 1:
        x += 1
    if b[j] > 0:
        y += 1
    if b[j] < 0:
        z += 1
print("{} valor(es) par(es)".format(v))
print("{} valor(es) impar(es)".format(x))
print("{} valor(es) positivo(s)".format(y))
print("{} valor(es) negativo(s)".format(z))