a,b,c =input('').split()

linha = a,b,c
pi=3.14159
triangulo = (float(a) * (float(c)))/2
circulo = (float(c)* float(c))*pi
trapezio =(float(a)+ float(b) )/2 * float(c)
quadrado = (float(b) * float(b))
retangulo = (float(a) * float(b))

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'
      .format(triangulo,circulo,trapezio,quadrado,retangulo))