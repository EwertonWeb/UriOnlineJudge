valores = input('').split()
codigo, qtde = valores

qtde = int(qtde)

preco = {"1":4.0, "2":4.5,"3":5.0,"4":2.0,"5":1.5}

total = qtde * preco[codigo]

print('Total: R$ {:.2f}'.format(total))