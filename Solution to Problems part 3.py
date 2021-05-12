# Classes and Objects

# Question 1

'''Create an abstract class Polygon that has a method get_no_of_sides() and get_area()
and it has three subclasses triangle, rectangle and square each with its own two methods
get_no_of_sides() and get_area() and their respective implementations accordingly.'''


class Polygon():

    def __init__ (self,sides):
        self.sides = sides

    def get_no_of_sides(self):
        return ("No. of side are :%s"% self.sides)

    def get_area(self):
        pass
            
class Triangle(Polygon):
    def __init__ (self,base,height):
        super().__init__ (3)
        self.base = base
        self.height= height
            
    def get_no_of_sides(self):
        return ("No. of side are :%s"%self.sides)

    def get_area(self):
        return ("Area of a Triangle using base and height = %s"%(1/2 *(self.base*self.height)))

class Rectangle(Polygon):
    def __init__ (self,length,width):
        super().__init__ (4)
        self.length = length
        self.width= width

    def get_no_of_sides(self):
        return ("No. of side are : %s"%self.sides)

    def get_area(self):
        return ("Area of a Rectangle using length and width = %s"%(self.length * self.width))

class Square(Polygon):
    def __init__ (self,lenght_of_all_sides):
        super().__init__ (4)
        self.lenght_of_all_sides = lenght_of_all_sides
        
    def get_no_of_sides(self):
        return ("No. of side are :%s"% self.sides)

    def get_area(self):
       return ("Area of a Square using length of sides is = %s"%(self.lenght_of_all_sides*self.lenght_of_all_sides))

new_shape = Polygon(4)
print(new_shape.get_no_of_sides())
print("\n")

newshape = Triangle(4,5)
print (newshape.get_area())
print (newshape.get_no_of_sides())
print("\n")

newshape = Square(6)
print (newshape.get_area())
print (newshape.get_no_of_sides())
print("\n")

newshape = Rectangle(3,4)
print (newshape.get_area())
print (newshape.get_no_of_sides())
print("\n")




# Question 2

''': Create a class Account having attribute currentbalance and a method display_balance.
This class has two subclasses Savings and Current. Both subclasses have two methods deposit
and withdrawal. The deposit method of Savings class adds the amount to be deposited in the
currentbalance attribute and adds another 2% interest on it however the Current subclass
only adds the amount. The withdrawal method for both the classes just subtracts the amount
to be withdrawn from the currentbalance'''


class Account:
    def __init__ (self, current_balance):
        self.current_balance = current_balance


    def display_balance(self):
        return  ("Your remaining Cash = %s" % (self.current_balance))

class Saving(Account):
    def __init__ (self, current_balance):
        super().__init__ (current_balance)
    def deposit(self,amount):
        new = amount + self.current_balance 
        balance = new + (new * 0.02)
        self.current_balance = balance
        
    def withdrawal(self,amount):
        balance = (self.current_balance - amount)
        self.current_balance = balance


class Current(Account):
    def __init__ (self, current_balance):
        super().__init__ (current_balance)
    def deposit(self,amount):
        self.current_balance = self.current_balance + amount

    def withdrawal(self,amount):
        balance = (self.current_balance - amount)
        self.current_balance = balance

my_bank = Current(0)
my_bank.deposit(1000)
my_bank.withdrawal(200)
print (my_bank.display_balance())

my_bank = Saving(0)
my_bank.deposit(1000)
my_bank.withdrawal(200)
print (my_bank.display_balance())




# Question 3

''' Create a Vehicle class with name, max_speed and mileage instance attributes.
Create child class Bus that will inherit all the variables and
methods of the Vehicle class. Give the capacity argument of Bus.seating_capacity()
a default value of 50. The default fare charge of any vehicle is seating_capacity * 100.'''


class Vehicle:
    def __init__ (self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def default_fare(self,seating_capacity):
         t_fare = seating_capacity * 100
         return t_fare
    
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self,capacity = 50):
        return ("%s has seating capacity of %s passengers."% (self.name,capacity))

    def total_fear (self,c=50):
        return ("Total fear is: %s "%((Vehicle.default_fare(self,seating_capacity=c))))
                
my_bus = Bus("Big Bus", 80, 21)
print(my_bus.seating_capacity(50))
print (my_bus.total_fear())
