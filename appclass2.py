#Encaplsulation
#modify the car class to encapsulate the brand attribute,making it privateand provide a getter method for it.
""" class Car:
    def __init__(self,brand,model):
        self.__brand=brand     #on making it accesscible by the certain key 
        self.model=model

    def Formula__brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        print("The brand name is {} and its model is {}.".format(self.__brand,self.model))

class ElectronicCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

f2=ElectronicCar("nissan","NissanGTR",'56877') 
print(f2.Formula__brand()) """      


#Polymorphism
#Demonstrate an Polymorphisim by defining a fuel_type in both car and electronic car but with different behaviours.
'''class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def detail(self):
        print("This is the brand {} which has a latest model as {}.".format(self.brand,self.model))

    def fuel_type(self):
        return "disel or petrol"    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)        
        self.battery_size=battery_size

    def detail1(self):
        print("This ev car brand {} is not available in india and is model is {} and its battery size is{}.".format(self.brand,self.model,self.battery_size))

    def fuel_type(self):
        return "electric charge" 
    
on=Car("mercedes","lewis Hamlinton")
print(on.fuel_type())

c=ElectricCar("Tata","Puch ev",'sghv23')
print(c.fuel_type())'''


#Class Variable
#Add a class variable to car that keeps the number of cars created.
'''class Car:
    count=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.count+=1

    def display(self):
        print("This car is french brand of company{} and its new realse is {}.".format(self.brand,self.model))

#r=Car("sdf","vhg")
#r1=Car("gfc","jjh")
#print(Car.count)  
#instead of using above method we can use this method
Car("ad","dd")
Car('js',"n bbd")
print(Car.count) '''


#Add a static method to the car class that returns a general description of a car
'''class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def show_overview(self):
        print("The car {} is currently a famous brand here and its new model is {}.".format(self.brand,self.model))    

    @staticmethod
    def details(avg,fuel):
        return avg,fuel

s1=Car("Tata","safari")
s1.show_overview()
print(Car.details(23,"hybrid"))  '''

'''from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

    def description(self):
        print("This a shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return  3.14*self.radius*self.radius

    def perimeter(self):
        return 2*3.14*self.radius




class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area (self):
        return  self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width) 

c=Circle(5)
r=Rectangle(2,4)

print(f"Circle.Area: {c.area()} ")
print(f"Circle.perimeter : {c.perimeter()}")
print(f"description: {c.description()}")

print(f"recArea: {r.area()}")
print(f"recPeri: {r.perimeter()}")
print(f"recdescription: {r.description()}")'''

#property decorators
#Use the property decorator in car class to make the model attribute read only
""" class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model

    @property
    def model(self):
        return self.__model
    
    def details(self):
        print("This type of model is private with no overtracing form {}".format(self.brand,self.__model))

c1=Car("red bull","Rb20")
print(c1.model)
c1.details()  """


#Class inheritance and isinstance() function
# demonstrate the use of isinstance() to check if my_tesla is an instance of an car and electric car
""" class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def details(self):
        print("This car model is from {} brand,and is modek is {}".format(self.brand,self.model))


class ElectricCar(Car):
    def __init__ (self, brand, model,fuel):
        super().__init__ (brand, model)
        self.fuel=fuel

    def show_details(self):
        print("this is an brand {} and its model is {} and its fuel type is {}".format(self.brand,self.model,self.fuel))

c1=Car("Tata","safari")
c2=ElectricCar("tesla","t01","electric charge")
c1.details()
c2.show_details()
x=isinstance(c2,ElectricCar)
print(x) """

#Multiple Inheritence
# Create two classes battery and engine,and let the electric car inherit from both ,demonstrting the multiple inheritence
'''class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Battery:
    def show(self):
        return "This is a Battery"
    
class Engine:
    def show_details(self):
        return "This a engine" 

class ElectricCar(Battery,Engine,Car):
    pass

a=ElectricCar("fgh","yu56")
print(a.show())
print(a.show_details())'''

#question 1 of day 5
# 46. Question: Create a base class Animal with a method sound() that prints "Some sound".
# Derive a class Dog from Animal and override the sound() method to print "Bark". Instantiate an
# object of Dog and call the sound() method.
""" class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("bark")

c=Dog()
c.sound()  """

#47. Question: Create two base classes Swimming with a method swim() that prints "Swimming"
# and Flying with a method fly() that prints "Flying". Derive a class Duck from both Swimming and
# Flying. Instantiate an object of Duck and call both the swim() and fly() methods.
""" class Swimming:
    def swim(self):
        print("Swimming")

class Flying:
    def fly(self):
        print("Flying")

class Duck(Swimming,Flying):
    pass

c=Duck()
c.swim()
c.fly() """

#48. Question: Create a base class LivingBeing with a method live() that prints "Living". Derive a
# class Animal from LivingBeing and add a method breathe() that prints "Breathing". Derive a
# class Human from Animal and add a method speak() that prints "Speaking". Instantiate an
# object of Human and call all three methods (live(), breathe(), and speak()).
""" class LivingBeing:
    def live(self):
        print("Living")

class Animal(LivingBeing):
    def breathe(self):
        print("Breathing")

class Human(Animal):
    def speak(self):
        print("Speaking")

c=Human()
c.speak()
c.breathe()
c.live()   """

# 49. Question: Create a base class Shape with a method area() that returns 0. Derive two
# classes Circle and Rectangle from Shape. Override the area() method in both derived classes to
# calculate and return the area of a circle and a rectangle, respectively. Instantiate objects of both
# Circle and Rectangle and call their area() methods.
""" class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

c=Shape()
print(c.area())

d=Circle(5)
print(d.area())

e=Rectangle(2,4)
print(e.area()) """

#50. Question: Create a base class Vehicle with a method drive() that prints "Driving". Create two
# classes Car and Truck that inherit from Vehicle and add specific methods carry_passengers()
# for Car and carry_cargo() for Truck. Create another class PickupTruck that inherits from both
# Car and Truck. Instantiate an object of PickupTruck and call the methods drive(),
# carry_passengers(), and carry_cargo().
""" class Vehicle:
    def drive(self):
        print("Driving")

class Car(Vehicle):
    def carry_passengers(self):
        print("This a carry_passenger method")        

class Truck(Vehicle):
    def carry_cargo(self):
        print("This is a carry_cargo method")

class PickupTruck(Car,Truck):
    def drive(self):
        print("This is an another type of method")

c=PickupTruck()
c.drive()
c.carry_cargo()
c.carry_passengers() """

# Create an abstract base class Employee with an abstract method
# calculate_salary(). Derive two classes PermanentEmployee and ContractEmployee from
# Employee. Implement the calculate_salary() method in both derived classes to print respective
# salary calculations. Instantiate objects of both PermanentEmployee and ContractEmployee and
# call their calculate_salary() methods.
""" from abc import ABC ,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class PermanentEmployee(Employee):
    def calculate_salary(self,salary_calculation):
        self.salary_calculation=salary_calculation
        return self.salary_calculation

    # def details(self):
    #     print(f"Permanebt employee salary is : {self.salary_calculation}")    

class ContractEmployee(Employee):
    def calculate_salary(self,salary_calculation):
        self.salary_calculation=salary_calculation
        return self.salary_calculation

    # def show_details(self):
    #     print(f"The salary of contractEmployee : {self.salary_calculation}")

a=PermanentEmployee()
print(f"salary is : {a.calculate_salary(12789)}")

b=ContractEmployee()
print(f"Salary is: {b.calculate_salary(23000)}") """


# 52. Question: Create a class Person with a method greet() that prints "Hello". Create another
# class Student that inherits from Person and overrides the greet() method to print "Hello, I am a
# student". Create a third class Teacher that also inherits from Person and overrides the greet()
# method to print "Hello, I am a teacher". Instantiate objects of Student and Teacher and call their
# greet() methods.

""" class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hello,I am a student")

class Teacher(Person):
    def greet(self):
        print("Hello,I am a Teacher")

c=Student()
c.greet()

d=Teacher()
d.greet() """


# 53. Question: Create an abstract class Appliance with an abstract method turn_on(). Create two
# classes WashingMachine and Refrigerator that inherit from Appliance. Implement the turn_on()
# method in both derived classes to print "Washing machine is now on" and "Refrigerator is now
# on", respectively. Instantiate objects of both WashingMachine and Refrigerator and call their
# turn_on() methods.
""" from abc import ABC ,abstractmethod
class Appliance(ABC):
    @abstractmethod

    def turn_on(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now on")

class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is now on") 

c=WashingMachine()
c.turn_on()

d=Refrigerator()
d.turn_on() """

# 54. Question: Create a class Device with a method operate() that prints "Operating device".
# Create two classes Phone and Tablet that inherit from Device and add specific methods
# make_call() for Phone and browse() for Tablet. Create another class Smartphone that inherits
# from both Phone and Tablet. Instantiate an object of Smartphone and call the methods
# operate(), make_call(), and browse().
""" class Device:
    def operate(self):
        print("Operating device")

class Phone(Device):
    def make_call(self):
        print("new instance")

class Tablet(Device):
    def browse(self):
        print("This is an another new instance")

class Smartphone(Phone,Tablet):
    pass

c=Smartphone()
c.operate()
c.make_call()
c.browse() """

# 55. Question: Create a base class BankAccount with a method deposit() that increases the
# balance by a given amount. Derive a class SavingsAccount from BankAccount and add a
# method add_interest() that increases the balance by a fixed interest rate. Instantiate an object of
# SavingsAccount, call the deposit() method, and then call the add_interest() method.
""" class BankAccount:
    def __init__ (self,amount):
        self.amount=amount

    def deposit(self,new_amount,amount):
        self.amount=amount
        self.amount+=new_amount
        return  new_amount

class SavingsAccount(BankAccount):
    def __init__ (self,interest):
        self.interest=interest

    def add_interest(self):
        return self.interest**self.amount
    
c=SavingsAccount(2.3) 
print(f"the increase amount is: {c.deposit(289,56)}")
print(c.add_interest()) """


# 56. Question: Create an abstract class Shape with an abstract method perimeter(). Derive two
# classes Square and Triangle from Shape. Implement the perimeter() method in both derived
# classes to calculate and return the perimeter of a square and a triangle, respectively. Instantiate
# objects of both Square and Triangle and call their perimeter() methods.
""" from abc import ABC ,abstractmethod
class Shape:
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def perimeter(self):
        return 4*self.length

class Triangle(Shape):
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def perimeter(self):
        return self.l+self.b+self.h

c=Square(4)
print(c.perimeter())
d=Triangle(2,3,4)
print(d.perimeter()) """

# 57. Question: Create a class User with a method login() that prints "User logged in". Create
# another class Admin that inherits from User and overrides the login() method to print "Admin
# logged in". Create a third class Guest that inherits from User and overrides the login() method to
# print "Guest logged in". Instantiate objects of Admin and Guest and call their login() methods.
""" class User:
    def login(self):
        print("User logged in")

class Admin(User):
    def login(self):
        print("Admin logged in")

class Guest(User):
    def login(self):
        print("guest logged in")

c=Admin()
c.login()
d=Guest() 
d.login()       """     


# day 4 questions
# 41. Create a class Counter with a class variable count to track the number of
# instances created. Implement the __init__ method to increment this counter. Add a
# method to return a new Counter object initialized to the current count value.
""" class Counter:
    count=0
class Count(Counter):
    def __init__(self,count,new_counter):
        self.count=count
        self.count+=new_counter
    def details(self):
        print(f"the new counter : {self.count}")    

     
      
c=Count(3,8)
c.details() """

# 42. Define a class Sentence with an instance variable text. Overload the +
# operator using __add__ to concatenate two Sentence objects. Create a method that
# returns a new Sentence object as a result of the concatenation.
""" class Sentences:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self):
        return self.a+self.b

c=Sentences("asd","sdf") """

#
                
        

        






        


                



















     


