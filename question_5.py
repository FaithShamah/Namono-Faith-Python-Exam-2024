# i)

# Book class with attributes title, author, and pages

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def get_title_and_author(self):
        return f"Title: {self.title}, Author: {self.author}"
    
# Creating an instance of Book and displaying its information

book1 = Book("The Python Languages", "F. Namono", 200)
print("Book Information:")
book1.display_info()


# ii)

# Derived class Ebook that inherits from Book and adds 'format' attribute

class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def display_info(self):
        super().display_info()
        print(f"Format: {self.format}")

# Creating an instance of Ebook and displaying its information

ebook1 = Ebook("Programming With Python", "Namono Faith", 500, "WITU")
print("\nEbook Information:")
ebook1.display_info()

# iii)

# Creating an instance of Book and getting only the title and author

book2 = Book("To Pass Python Made Simple", "N.F.Shamah", 400)
print("\nBook Title and Author:")
title_and_author = book2.get_title_and_author()
print(title_and_author)

# iv)

# a)

#     Class:
#          A class refers to a blue print of an object.
           #Forexample the class WITU Cohort 4 with it's objects as students.
           #A class also has methods.

# b)

#    Object:
#          An object refers to a variable that is used to define functions and data inorder to display data.
#          An object als refers to an instanciation of a class.



