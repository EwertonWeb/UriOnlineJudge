entrada1 =input('').split()
entrada2 =input('').split()

cp1 ,np1, vu1= entrada1
cp2, np2, vu2 = entrada2

soma= (int (np1) * (float(vu1)) + (int(np2) * (float(vu2))))


print('VALOR A PAGAR: R$ {:.2f}'.format(soma))