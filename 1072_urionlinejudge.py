num = int(input())
inside = 0
out = 0
for i in range(1,num + 1):
    x = int(input())
    if x >= 10 and x <= 20:
        inside = inside + 1
    else:
        out = out + 1
print('{} in'.format(inside))
print('{} out'.format(out))