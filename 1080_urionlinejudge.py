num = int(input())
y=0

for i in range(1,100):
    x = int(input())
    if x > y:
        bigger = x
        position = i + 1
        y = x

print('{}'.format(bigger))
print('{}'.format(position))