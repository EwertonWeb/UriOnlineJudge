a, b, c = [int(x) for x in input().split(' ')]


if a > b and a > c:
    d = a
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b
if b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
if c > a and c > b:
    d = c
    if a > b:
        e = a
        f = b
    else:
        f = a
        e = b

print('{}'.format(f))
print('{}'.format(e))
print('{}'.format(d))
print()
print('{}'.format(a))
print('{}'.format(b))
print('{}'.format(c))