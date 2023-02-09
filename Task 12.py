class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f'Hey {self.name}')


taufiq=Person('Taufiq')
alam=Person('Alam')
taufiq.talk()
alam.talk()