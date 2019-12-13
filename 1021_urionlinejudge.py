values = float(input())

cash = [100,50,20,10,5,2]
coins = [1,0.50,0.25,0.10,0.05,0.01]

print('NOTAS:')
for cash in cash:
    volume_cash = int(values / cash)
    print('{} nota(s) de R$ {:.2f}'.format(volume_cash,cash))
    values -= volume_cash * cash

print('MOEDAS:')
for coins in coins:
    volume_coins = int(round(values,2) / coins)
    print('{} moeda(s) de R$ {:.2f}'.format(volume_coins,coins))
    values -= volume_coins * coins
