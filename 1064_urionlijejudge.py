counter =0
sum = 0

for num in range (6):
    number = float(input(''))
    if (number > 0.0):
        counter += 1
        sum += number
print('{} valores positivos'.format(counter))
print('{:.1f}'.format(sum / counter))