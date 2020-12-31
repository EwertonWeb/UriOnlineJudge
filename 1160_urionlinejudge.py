test_number = int(input())

for test in range(0, test_number):
    entry = input().split()
    pa =int(entry[0])
    pb =int(entry[1])
    g1 =float(entry[2])/100
    g2 = float(entry[3])/100
    year =0
    while True:
        pa += int(pa * g1)
        pb += int(pb * g2)
        year += 1

        if pa > pb or year >100:
            break

    if year <=100:
        print('{} anos.'.format(year))
    else:
        print('Mais de 1 seculo.')