value = input().split()

x = int(value[0])
last_value = len(value) -1
y = int(value[last_value])

sum = 0

for num in range(0, y):
    sum += x + num 
print('{}'.format(sum))