import random

number = random.randint(1,2)

Choosen = input("Choose Head or Tails (h/t): ")

if Choosen == 'h':
    h = 1
    if h == number:
        print(" Its HEAD !! YOU WIN !! ")
    else:
        print(" OOPS !! Its Tails !! YOU LOST !! ")

elif Choosen == 't':
    t = 2
    if t == number:
        print(" Its Tails !! YOU WIN !! ")
    else:
        print(" OOPS !! Its Heads !! YOU LOST !! ")

else:
    print(" Wrong Input !! ")