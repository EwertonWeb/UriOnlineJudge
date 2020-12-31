num = int(input())

group_2 = (num *(num -1)) / 2
group_4 = (num * (num -1) * (num-2) * (num-3)) / (4*3*2*1)

result = 1 + group_2 + group_4 

print('{}'.format(int(result)))