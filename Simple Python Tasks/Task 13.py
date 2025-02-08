def ltk(weight):
    kg = int(weight) * .45
    print(f'Your weight in KG is {kg} kg')

def ktl(weight):
    lbs = int(weight) / .45
    print(f'Your weight in Pounds is {lbs} lbs')

def error():
    print('wrong input!')

weight=input('enter the weight: ')

gg=input('convert to (L)bs or (K)g: ')

if gg.upper()=='L':
   ktl(weight)

elif gg.upper()=='K':
   ltk(weight)

else:
    error()

