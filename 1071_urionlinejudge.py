x = int(input())
y = int(input())

bigger = x if x > y else y
smaller = y if y < x else x
smaller+=1
sum = 0

while (smaller < bigger):
    if(smaller % 2 != 0):
        sum+=smaller
    smaller+=1
print('{}'.format(sum))