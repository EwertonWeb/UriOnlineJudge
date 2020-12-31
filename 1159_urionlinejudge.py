while True:
    a = int(input())

    if a == 0:
        break

    if a % 2 !=0:
        a += 1

    sum = 0
    for b in range (0,5):
        sum += a
        a += 2
    print('{}'.format(sum))