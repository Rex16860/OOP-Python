class Person:
    # Hidden member of MyClass
    __num = 0

    # A member method that changes
    # __hiddenVariable
    def sum(self, increment):
        self.__num += increment
        print(self.__num)


# Driver code
myObject = Person()
myObject.sum(2)
myObject.sum(5)

# This line causes error
print(myObject.__num)
