class Cow:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def voice(self, voice):
        self.voice = voice


cow1 = Cow(name='Saryshka', age=2, color='brown and white')
print(f'{cow1.name} is {cow1.age} years old. Color of {cow1.name} is {cow1.color}')
cow1.voice('MU-UU-UU\n')
print(cow1.voice)


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def voice(self, voice):
        self.voice = voice


dog1 = Dog(name='Layka', age=1, color='white')
print(f'{dog1.name} is {dog1.age} years old. Color of {dog1.name} is {dog1.color}')
dog1.voice('WAF-WAF\n')
print(dog1.voice)

class Bear:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def voice(self, voice):
        self.voice = voice


bear1 = Bear(name='Mamalak', age=1, color='brown')
print(f'{bear1.name} is {bear1.age} years old. {bear1.name}\'s color is {bear1.color}')
bear1.voice('BaAaAaAAaA\n')   # he is 1 year old, so...
print(bear1.voice)


class Cat:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def voice(self, voice):
        self.voice = voice


cat1 = Cat(name='MyiMyi', age=1, color='black')
print(f'{cat1.name} is {cat1.age} years old. {cat1.name}\'s color is {cat1.color}')
cat1.voice('myaw-myaw\n')
print(cat1.voice)