'''class Person:
    def __init__(self,name,age,gender,salary):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary
    def show_details(self):
        print("the name is {} ,age is {},gender is {},salary is {}".format(self.name,self.age,self.gender,self.salary))

p1=Person('agrim',89,'male',0) #this is a instance
p1.show_details()   
p2=Person("a",23,"male",20)
p2.show_details()   '''

#Write a program using oops to create class  employes for the the employees of the organisation employe
#has data (name,employ id,designation ) and also display the details of the emplooyes on the screen
'''class Employee:
    def __init__(self,name,employeeid,designation):
        self.name =name
        self.employeeid=employeeid
        self.designation=designation
    def show_details(self):
        print("The name is {},and his employeeid is {},and his designation is {}".format(self.name,self.employeeid,self.designation))
p1=Employee('Aditi',12,'PM')
p2=Employee('Agrim',13,'Ass.Manager')
p3=Employee('Nikhil',24,'CMO')
p4=Employee('as',34,'CEO')
p5=Employee('amrit',23,'Secretary')

emp_list=[p1,p2,p3,p4,p5]
for i in emp_list:
    i.show_details()
   '''


'''class Greeting:
    message="What is an object"

    def say (self):
        print(self.message)

greet=Greeting()
greet.say()        
'''








#day 3 question 1 of hw
'''class Book:
    def __init__ (self,title,author,no_of_pages):
        self.title=title
        self.author=author
        self.no_of_pages=no_of_pages
    def details(self):
        print("This is a {} book,by {} ,and has {} pages.".format(self.title,self.author,self.no_of_pages))
a= Book("creature","ads",345) 
b=Book("mischivious","dfdh",567)   
c=Book("Time","fjy",678) 
book_list=[a,b,c]
for i in book_list:
    i.details()
       '''

#question 3
#develop a class circle create an instance variable for radius and methods to calculate the area and the 
#circumference
'''class circle:
    c=3.14 #a type of class variable
    d=2
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.c*self.radius*self.radius
        # return area
        
    def circumference(self):
        circumference = self.d*self.c*self.radius
        return circumference

    
    def display(self):
        print("Area: ",self.area())
        print("Circumference: ",self.circumference())
        
r1=circle(4)
r1.display()'''


#An example of class variable(Static variable)
'''class Employee:
    company_name="ABC Organisation" #a class variable

    def __init__(self,name,designation):
        self.name = name
        self.designation=designation

    def show_details (self):
        print(f"Company name: {Employee.company_name} \n name: {self.name} \n Designation: {self.designation}")
e1=Employee("asd","fg")
e1.show_details()  '''


#an example of self parameters
'''class Numbers:
    even=[]
    odd=[]
    def __init__(my,num):  #it is not necesscary to use self ,we can use any term instead og self
        my.num=num
        if num % 2 ==0:
            Numbers.even.append(num)
        else:
            Numbers.odd.append(num) 
n1=Numbers(5)
n2=Numbers(45)
n3=Numbers(68)
n4=Numbers(82)
print("Even numbers are: ",Numbers.even)
print("Odd numbers are:",Numbers.odd)  '''

#using an instant method foe updating the information
'''class Employee:
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position

    def show_details(self):
        print("The name of emplayee is {},and the salary is {},and the designation is {}.".format(self.name,self.salary,self.position))

    def give_raise(self,amount):
        self.salary+=amount
        print(f" the name is {self.name} and his raise in salary of ({amount}.New salary is {self.salary})")
    def update_position(self,new_position):
        self.position=new_position
        print(f"{self.name} fot a new position which is {self.position}")

e1=Employee("ads",10000,"hr")
e1.show_details()
e1.give_raise(6000)
e1.update_position("ceo")
e1.show_details()
            '''

#Class method
#program to count how many object of a class are created.

'''class Student:
    counter=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.counter+=1

    def msg(self):
        print("hello"+self.name+"you got",self.marks,"% marks")

    @classmethod
    def object_method(cls):
        return cls.counter

s1=Student("afd",98)
s2=Student("fgd",99)
s3=Student("nbc",90)
print(Student.object_method())
print(s1.object_method()) '''           
            
    


#Static method
'''class Mathoperations:
    @staticmethod
    def add_num(a,b):
        return a+b
    
    @staticmethod
    def sub_num(a,b):
        return a-b
    
obj = Mathoperations()
result_add=Mathoperations.add_num(9,8)
result_subtra=Mathoperations.sub_num(10,7)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtra}")'''

#Example of default constructor
'''class Student:
    def __init__(self):
        print("This is a default constructor")

    def show(self,name):
        print("Hello",name) 

s1=Student()
s1.show("ads")
s2=Student()
s2.show("fyg")'''

#An Example
'''class Addition:
    first = 0
    second = 0
    answer = 0
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def display(self):
        print("First number = ",self.first)
        print("Second number = ",self.second)
        print("Addition of two numbers = ",self.answer)

    def calculate(self):
        self.answer = self.first+self.second

ob=Addition(1000,2000) 
ob.calculate()
ob.display()
               '''


#Built in methods in class
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("set",56)

n1 = getattr(p1,"name")
print(f"Name: {n1}")

setattr(p1,"age",21)
print(f"Update Age: {p1.age}")

has_name = hasattr(p1,"name")
print(f"Has attribute 'name': {has_name}")

delattr(p1,"age")

has_age=hasattr(p1,"age")
print(f"Has attribute 'age' after deletion : {has_age}")
'''
#magic methods
'''num=10
x=num.__add__(5)
print(x)
'''

'''st = "Agrim"
x=st.__add__(" is sick")
print(x)
'''

'''class Students:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __gt__ (self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
s1=Students(3,78)
s2=Students(87,89)
if s1 > s2:
    print("s1 is greater")
else:
    print("s2 is greatest")'''

#New example
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"The name is {self.name} and age is {self.age}"    
p = Person("mkl",89)
print(p)        '''


#Another example
'''class Person:
    def __new__(self):
        print("This is a new method")
        self.__init__(self)
    def __init__(self):
        print("init method")'''

#Object as argument
'''class Myclass:
    def __init__(self,value):
        self.value=value

def print_value (obj):
    print(f"The value is : {obj.value}")

obj = Myclass(10)
obj2 = Myclass(23)
print_value(obj)  
print_value(obj2) '''

#Another Example object as an argument
'''class Person:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"Person ({self.name})"
    
class Greeting:
    def generate_greeting(self,person):
        return f"Hello,{person.name}! Welcome!"

person = Person("asd")
greeting= Greeting()

message = greeting.generate_greeting(person)
print(message)'''

#Instances as return values
# Function can return object,they can return the intances of classes.

'''class Myclass:
    def __init__(self,name,section):
        self.name=name
        self.section=section

        
def create_obj(name,section):
    return Myclass(name,section)
    
obj = create_obj("asd",'a')
print(obj.name)
print(obj.section)
'''


#'''local scope and global scope
'''def outer_function():
    x=20

    def inner_function():
        y=4
        print(x)
    inner_function()
#if you use print(y) here in line then it wil show error because y is an inner function and can be called
outer_function()    '''

#Another exmple:
'''def outer_function():
    x=20

    def inner_function():
        
        nonlocal x #nonlocal variables are used in nested functions whose local scope is not defined. 
        print(x)
    inner_function()

outer_function() '''      


#Global Scope
'''x = 50

def my_function():
    x=90
    print(x)
my_function()
print(x)    
'''

#Develop a program that defines a global variable count and a function
#increment that has a local variable count. Show how to use and differentiate between
#the global and local count variables.

'''count=0
def increment():
    count=2
    count+=1
    print("the count before:",count)
    print("the increment count is:",count)
increment()  
print("the global count ater:",count)  
    '''

#create an Electric Car class that inherites from the car class and has an additional attribute battery size
'''class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def details(self):
        print("The car brand is {} and its model is {}.".format(self.brand,self.model))

f1=Car("BMW","AWM")
print(f1.details())       

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

f2=ElectricCar("Tesla","sdf","56mkh")
f2.details()      '''


#Abstraction classes
#An example of encapsulation
'''class Myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def display(self):
        print(self.x)
        print(self.y)

ob1=Myclass(4,5)
ob1.display()            
    '''

#Inheritence with super() method
'''class Person:
    def __init__(self,f,l):
        self.fnam=f
        self.snam=l
        print("The person first name is {} and the lat name is {}.".format(self.fnam,self.snam))

class Child(Person):
    def __init__(self, x, y):
        super().__init__(x, y)
        print("this person has a same first name {} and last name {}.".format(self.x,self.y))

s=Person("papa","tundey")        
'''

#Inheritance another example:
'''class Animal:
    name=""
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def display(self):
        print("My anme is :",self.name)

lab=Dog()
lab.name="rtg"
lab.eat()
lab.display()    
'''
      
                    
#multi inheritance
'''class Father:
    def __init__(self):
        print("Father class constructor")

    def show_father(self):
        print("fathedr class method")

class Son(Father):
    def __init__(self):
        print("Son class Constructor")
    def show_son(self):
        print("son class method")

class Grandson(Son):
    def __init__(self):
        print("Grandson class constructor")
    def show_grandson(self):
        print("grandson class method")

g=Grandson()
g.show_grandson()
g.show_father()
g.show_son() '''                                   


#hirarchial inheritance
'''class Father:
    def __init__(self):
        print("This is a father inheritance")
    def show_father(self):
        print("father class method")

class Son(Father):
    def __init__(self):
        print("this is son inhertitance")
    def show_son(self):
        print("This is son class method")

class Daughter(Father):
    def __init__(self):
        print("This is the sdaughter inheritence")
    def shoe_daughter(self):
        print("This is the daughter class method")

s=Son()
s.show_father()
s.show_son()

d=Daughter()
d.shoe_daughter()
d.show_father()'''


#Another type of inheritance
'''class Father():
    def __init__(self):
        print("This is a Father constructor")
    def show_father(self):
        print("This is a father class method")

class Mother():
    def __init__(self):
        print("this is a mother class constructor")
    def show_mother(self):
        print("Mother class constructor")

class Son(Father,Mother):
    def __init__(self):
        print("this is son constructor")
    def show_son(self):
        print("this is son class method")

d=Son()
d.show_father()
d.show_mother()
d.show_son()  '''

#An example of encapsulation

'''class Computer:
    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print("Selling price : {}".format(self.__maxprice))

    def setMaxprice(self,price):
        self.__maxprice=price

c=Computer()
c.sell()
c.setMaxprice(9000)
c.sell()'''      

#A type of protected class encapsulation
'''class Students:
    _name=None
    _roll=None
    _branch=None

    def __init__(self,name,roll,branch):
        self._namename=name
        self._branch= branch
        self._roll=roll
    def _displayinfo (self):
        print("roll:",self._roll)
        print("branch: ",self._branch)

class Learnowx(Students):
    def __init__(self, name, roll, branch):
        Students.__init__(self,name, roll, branch)  

    def display_details(self):
        print("name: ",self._name)
        self._displayinfo()

r=Learnowx("asd",231,"cse")
r.display_details()'''

#An private example of private 
'''class Student:
    __name = None
    __roll=None
    __branch= None
    def __init__(self,name,roll,branch):
        self.__name=name
        self.__roll=roll
        self.__branch=branch
    def __display(self):
        print("name: ",self.__name)
        print("Roll : ",self.__roll)
        print("branch: ",self.__branch)
    def access_private_method(self):
        self.__display()

r=Student("asd",34,'klkhk')
r.access_private_method()'''
'''r.__display() '''   #on using this it shows an error as it is an private key     

#Data hiding in python
'''class Myclass:
    __hiddenvar=12
    def add(self,increment):
        self.__hiddenvar+=increment
        print(self.__hiddenvar)
u=Myclass()
u.add(7)
u.add(100)'''
'''print(u.__hiddenvar)''' #error will be showed as it is not accessible ouside       



#Method resolution order
'''class A:
    def method(self):
        print("Method is A")

class B(A):
    def method(self):
        print("Method is B")

class C(A):
    def method(self):
        print("Method is C")

class D(B,C):
    pass

d=D()
d.method()
print(D.mro())''' #This function tell us about the heriarchial structure and tell us if d is said to
#be pass the it will check in the parent class and if both the parent class in b and c is said yo be passed
#then it will check the parent class of b and c and will print that instance.



#duck typing in polymorphism
#Here it will call its own class function
'''class Bird:
    def fly(self):
        print("bird can fly")

class Aeroplane:
    def fly(self):
        print("Aeroplane can fly")

class Fish:
    def swim(self):
        print("fish can't fly")

for obj in Bird(),Aeroplane(),Fish(): #fish has no attribute fly so it will show error
    obj.fly() '''


#Method overloading
'''class Operations:
    def sum(self,a=0,b=0,c=0):
        s=0
        if a!=0 and b!=0 and c!=0:
            s=a+b+c
        elif a!=0 and b!=0:
            s=a+b
        else:
            s=a
        return s

s=Operations()

print(s.sum(2,4,5))
print(s.sum(2,5))
print(s.sum(56))'''

#Operator overloading
'''class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        std=Student(m1,m2)
        return std
    
s1=Student("asd","sdd")
s2=Student("sdf","jkb")
std=s1+s2
print(std.m2)'''



#New question
#Perform vector operations like addition, subtract and dot product.using operator overloading

'''class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__ (self,other):
        return Vector(self.x-other.x,self.y-other.y) 

    def __mul__(self,other):
        return self.x*other.x +self.y*other.y

    def __str__(self):
        return f"{self.x},{self.y}"

v1=Vector(2,3)
v2=Vector(1,2)

v3=v1+v2
v4=v1-v2
dot_product=v1*v2

print("v1: ",v1)
print("v2: ",v2)
print("v1+v2: ",v3)
print("v1-v2: ",v4)
print("v1*v2: ",dot_product)'''


#Create a base class BankAccount and two derived classes SavingsAccount and
#CurrentAccount. The derived classes will override a method calculate_interest to provide
#specific implementations for calculating interest for savings and current accounts.
'''class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def calculate_interest(self):
        return self.balance*0.01

    def display(self):
        print("The account no is {} and its balance is {}.".format(self.account_number,self.balance))

class SavingAccount(BankAccount):
    def calculate_interest(self):
        return self.balance*0.04

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return self.balance*0.02
    
s=SavingAccount("123",4567)
n=CurrentAccount("gh",808)
s.display()
n.display()
print(f"saving interst : {s.calculate_interest()}")
print(f"balance: {n.calculate_interest()}")'''


#Abstraction Method
'''from abc import ABC ,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    def message(self):
        print("computer is an ec device")
class Laptop(Computer):
    def process(self):
        print("Excuting in process")

class Desktop(Computer):
    def process(self):
        print("Excecuting desktop process")

c1=Laptop()
c2=Desktop()
c1.process()
c2.message()
c2.process()'''


                        
             















    






        

        







    

    
        
        




