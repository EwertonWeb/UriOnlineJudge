a=b=1


while b != 0 and a != 0:
    b, a = map(int, input().split())
    if b > 0:
        if a > 0:
            print('primeiro')
        if a< 0:
            print('quarto')
    if b < 0:
        if a > 0:
            print('segundo')
        if a < 0:
            print('terceiro')