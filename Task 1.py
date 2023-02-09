

weight = input('what is ur weight: ')

char = input('(L)bs or (K)g: ')

if ord(char)==107 or ord(char)==75:
    weight = int(weight) * 2.20
    print(f'Your weight in lbs is {weight}')

elif ord(char)==108 or ord(char)==76:
    weight = int(weight) * 0.45
    print(f'Your weight in kg is {weight}')

else:
    print('please enter L/l or K/k')