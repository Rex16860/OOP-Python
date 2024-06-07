"""
Class and Object
"""


class Programmer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name: {self.name}, age: {self.age}'


class Backend(Programmer):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.language = language.split(', ')

    def details(self):
        print(f'My Language is: ')
        for i in range(len(self.language)):
            print(f'{i + 1}. {self.language[i]}')


a = Backend('ard', 25, 'Python, PHP, Java')

print(a)
print(a.details())
