try:
    age =  int(input('age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("u can't div anything by zero!")
except ValueError:
    print('invalid value')
