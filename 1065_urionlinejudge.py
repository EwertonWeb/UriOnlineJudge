pair_numbers = 0

for num in range(5):
    number = int(input(''))
    if (number % 2 ==0):
        pair_numbers +=1
print('{} valores pares'.format(pair_numbers))