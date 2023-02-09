num=input('enter the numbers: ').split()
unique=[]
for number in num:
    if num.count(number)>1:
        if number not in unique:
            unique.append(number)

print(unique)