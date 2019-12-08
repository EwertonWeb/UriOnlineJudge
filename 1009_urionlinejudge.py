nome=str(input())
salfixo=float(input())
vendas_mes=float(input())

fim_mes = (vendas_mes * 0.15 )+ salfixo
print('TOTAL = R$ {:.2f}'.format(fim_mes))