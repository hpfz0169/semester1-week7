class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} was written by {self.author} in the year {self.year}"

harry_potter = Book("Harry Potter", "JK Rowling", "1997")
print(harry_potter)

# Given a Book class with the __init__ method, define the __str__ method
# (1) define a suitable string representation for the attributes
# (2) test your code by creating some book objects and print'ing them
