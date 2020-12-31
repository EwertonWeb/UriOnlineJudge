insert = int(input())

for a in range(0, insert):
    value = input().split()
    b = int(value[0])
    c = int(value[1])

    if b % 2 ==0:
        b += 1

    sum = 0

    for y in range(0, c):
        sum += b
        b += 2
    print('{}'.format(sum))