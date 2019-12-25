salario =float(input(''))

if salario >= 0.0 and  salario <= 400.00:
    reajuste= (salario * 15 )/100
    novo_salario = (reajuste + salario)
    percentual =(reajuste / salario)*100
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(novo_salario,reajuste,percentual))
elif salario >= 400.01 and salario <= 800.00:
    reajuste = (salario * 12)/100
    novo_salario = (reajuste +salario)
    percentual = (reajuste / salario)*100
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(novo_salario, reajuste,percentual))
elif salario >= 800.01 and salario <= 1200.00:
    reajuste =(salario * 10)/100
    novo_salario = (reajuste + salario)
    percentual = (reajuste / salario)*100
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(novo_salario, reajuste, percentual))
elif  salario >= 1200.01 and salario <= 2000.00:
    reajuste = (salario *7)/100
    novo_salario =(reajuste + salario)
    percentual =(reajuste/ salario)*100
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(novo_salario, reajuste, percentual))
elif salario > 2000.00:
    reajuste =( salario *4)/100
    novo_salario = (reajuste + salario)
    percentual=(reajuste/salario)*100
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:.0f} %'.format(novo_salario, reajuste,
                                                                                         percentual))
