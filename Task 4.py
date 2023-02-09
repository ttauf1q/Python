

print('enter numbers: ')
num = input().split()
min=num[0]
for count in num:
    if min>count:
        min=count
print(min)