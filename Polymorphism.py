"""
Polymorphism
"""


class Books:
    def intro(self):
        print('There are many types of books')

    def types(self):
        print('one of them is Fiction and Nonfiction Books')


class Biographies(Books):
    def types(self):
        print('This is Nonfiction Books')


class SherlockHolmes(Books):
    def types(self):
        print('This is Fiction Books')


books = Books()
biographies = Biographies()
sherlock_holmes = SherlockHolmes()

books.intro()
books.types()
biographies.intro()
biographies.types()
sherlock_holmes.intro()
sherlock_holmes.types()
