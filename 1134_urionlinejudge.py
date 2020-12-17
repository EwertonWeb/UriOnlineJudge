alcool = 0
gasolina = 0
disel = 0
a = 0
while a != 4:
    a = int(input())
    if a == 1:
        alcool = alcool + 1
    if a == 2:
        gasolina = gasolina + 1
    if a == 3:
        disel = disel + 1
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(disel))