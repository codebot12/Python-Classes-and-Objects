# Classes and Objects

# Question 1

'''Implement a class BookStore that has three attributes title, author and publisher.
Initialize these in the constructor. Also make the mutators and accessors for the three.
Lastly make a method Book_Info() that displays all the information.'''


class BookStore:

    def __init__  (self, title='', author='', publisher=''):
        self.title = title
        self.author = author
        self.publisher = publisher

    def set_title(self, title):
        self.title = title
    def get_title(self):
        return self.title

    def set_author (self, author):
        self.author = author
    def get_author (self):
        return self.author

    def set_publisher (self, publisher):
        self.publisher = publisher
    def get_publisher (self):
        return self.publisher

    def book_info(self):
        a1 = self.get_title()
        a2 = self.get_author()
        a3 = self.get_publisher()
        return ("\nBook Title : %s \nBook Author : %s \nBook Publishers : %s\n"
                % (self.get_title(),self.get_author(),self.get_publisher()))

new_bookStore = BookStore("A Passage to India"," E. M. Forster"," Edward Arnold, (UK) Harcourt Brace (US) " )
print (new_bookStore.book_info())

bookStore2 = BookStore()
bookStore2.set_title("To Kill a Mockingbird")
bookStore2.set_author(" Harper Lee")
bookStore2.set_publisher(" J. B. Lippincott & Co.")
print (bookStore2.book_info())


# Question 2

''' Write a Python class named Circle constructed by a radius. Write the mutators and accessors
for radius and write methods to compute the area of a circle and circumference and
another method display() that prints the radius  along with the area and circumference of the circle.'''


import math
class Circle:

    def __init__(self, radius=0):
        self.radius = radius

    def radius_update (self, new_radius):
        self.radius = new_radius
    def radius_getter (self):
        return self.radius

    def area(self):
        total_area = math.pi*self.radius**2
        return round(total_area,3)
    
    def circumference(self):
        total_circumference = 2*self.radius*math.pi
        return round(total_circumference,3)

    def display(self):
        print ("\nRadius = %s \nArea of Circle = %s \nCircumference of the circle = %s \n"
                % (self.radius_getter(), self.area(), self.circumference()))
         

new_Circle = Circle(4)
new_Circle.display()

new2_Circle = Circle()
new2_Circle.radius_update(8)
new2_Circle.display()



# Question 3

''' Write a Python class called String_Play which includes three methods:
•	string_Taking
•	string_Printing_UC
•	string_Printing_LC
string_Taking method receives a string from the user, string_Printing_UC
method prints that string in upper case and string_Printing_LC method prints that string in lower case.
After writing the class, make an object of this class and call all the functions.'''


class String_play:

    def __init__(self, string1=''):
        self.string1 = string1

    def string_taking (self, my_string):
        self.string1 = str(my_string)

    def string_Printing_UC (self):
        return self.string1.upper()

    def string_Printing_LC(self):
        return self.string1.lower()
    
new_string = String_play("\nI am Pakistani.")
print (new_string.string_Printing_UC())
print (new_string.string_Printing_LC())

its_string = String_play()
its_string.string_taking ("\nThe quick brown fox jumps over the lazy dog")
print (its_string.string_Printing_UC())
print (its_string.string_Printing_LC())





