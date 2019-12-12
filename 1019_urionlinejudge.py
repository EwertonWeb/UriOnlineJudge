n=int(input(''))

a =int( n / 3600)
b = n% 3600
c = int(b / 60)
d = int(b% 60)
print('{}:{}:{}'.format(a,c,d))