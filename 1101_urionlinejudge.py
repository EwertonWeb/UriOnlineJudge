while True:
    value = [int(x) for x in input().split()]

    m = min(value)
    n = max(value)

    if m <= 0:
        break

    text = ""
    sum = 0
    for num in range(m, n +1):
        sum += num
        text += str(num) + " "

    print('{}Sum={}'.format(text, sum))