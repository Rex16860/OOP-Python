# Python program to
# demonstrate private members
# "__" double underscore represents private attribute.
# Private attributes start with "__".

# Creating a Base class
class Users:
    def __init__(self):
        self.username = 'Rx169'
        self.__password = 'Rx123321'


# Creating a derived class
class Rex(Users):
    def __init__(self):
        # Calling constructor of
        # Users class
        Users.__init__(self)
        print('Calling private member of Users class')
        print(self.__password)


# Driver code
obj1 = Users()
print(obj1.username)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
