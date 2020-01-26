num = int(input())
coelhos = 0
ratos = 0
sapos = 0

for i in range(1 , num + 1):
    y = input().split()
    a, b, = y
    if b == 'C':
        coelhos = coelhos + int(a)
    if b == 'R':
        ratos = ratos + int(a)
    if b == 'S':
        sapos = sapos + int(a)

total = coelhos + ratos + sapos
percentualcoelhos = (coelhos / total) * 100
percentualratos = (ratos / total) * 100
percentualsapos = (sapos / total) * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(percentualcoelhos))
print('Percentual de ratos: {:.2f} %'.format(percentualratos))
print('Percentual de sapos: {:.2f} %'.format(percentualsapos))