# Classes and Objects

# Question 1

'''Make a class called Restaurant. The __init__()
method for Restaurant should store two attributes: a restaurant_name
and a cuisine_type. Make a method called describe_restaurant() that prints
these two pieces of information, and a method called open_restaurant() that
prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.'''


class Restaurant():
    def __init__ (self,restaurant_name, cuisine_type):
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(self.restaurant_name.title()+ " offers "+ self.cuisine_type.title()+ " cuisine.")

    def open_restaurant(self):
        print(self.restaurant_name.title()+ " is now Open.")
        

restaurant= Restaurant('Qabail Tribes','Asian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Question 2

''' Write a Python class MyString which has methods get_String and print_String
and reverse_String. The function get_String accepts a string from the user and
print_String prints the string in upper case and reverse_String
returns the reverse of the string.'''


class Mystring():
    def __init__ (self): 
        self.my_string = ''
        
    def get_string(self):
        data = input("Enter a string:")
        self.my_string = data

    def print_string(self):
        print(self.my_string.upper())

    def reverse_string(self):
        reverse_string = self.my_string[::-1]
        print(reverse_string)
        
new_string = Mystring()
new_string.get_string()
new_string.print_string()
new_string.reverse_string()


# Question 3

''' Implement a class Address. An address has a house number, a street,
an optional apartment number, a city, a state, and a postal code.
Define the constructor such that an object can be created in one of
two ways: with an apartment number or without Supply a print method
that prints the address with the street on one line and the city state,
and postal code on the next line. '''

class Address():
    def __init__ (self,house_number, street_number, city, state,postal_code, apartment_number="" ):# we can also initillize in these ways too (*apartment_number,apartment_number=None)  
        self.house_number = house_number
        self.street_number = street_number
        self.apartment_number = apartment_number
        self.city = city 
        self.state = state
        self.postal_code = postal_code
        
    def print_address(self):
        if len(self.apartment_number)>0:
            print("House.No: %s, Street.No:%s, Apartment.No:%s,\nCity:%s, State:%s, \nPostal Code:%s\n"%(self.house_number,self.street_number,
                                            self.apartment_number,self.city,self.state, self.postal_code))
        else:
            print("House.No: %s, Street.No:%s,\nCity:%s, State:%s, \nPostal Code:%s\n"%(self.house_number,self.street_number,
                                            self.city,self.state, self.postal_code))
            


        
new_address= Address('323_A','12A','Multan','Punjab','6000','534')
new_address.print_address()
new_address= Address('323_A','12A','Multan','Punjab','6000')
new_address.print_address()





