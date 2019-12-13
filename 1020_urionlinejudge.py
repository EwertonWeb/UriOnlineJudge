value = int(input())
year = int(value / 365)
month = int((value%365/30))
day = int(value%365%30)


print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(year,month,day))