#Define a class Student with a class variable school_name. Create a class
#method to change the school's name and an instance method to display student details
#along with the school name.

""" class Student:
    def __init__(self,school_name,student_name,id):
        self.school_name=school_name
        self.student_name=student_name
        self.id=id

    def show_details(self):
            print("The school name is {},and the student name is {},and that person id no. is {}.".format(self.school_name,self.student_name,self.id))

    def update_school_name(self,new_school):
         self.school_name=new_school
         print(f"The student new school is {self.school_name}")

std1 = Student("abs school","fgh","fg23")
std1.show_details()
std1.school_name="akg"
print(std1.school_name)
std1.update_school_name("DPS") """

#instead of updating we can use std.school_name="akg"


#Implement a class MathOperations with static methods for addition,
#subtraction, multiplication, and division of two numbers.

'''class MathOperations:
    def add_opp(a,b):
        return a+b
    
    def sub_opp(a,b):
        return a-b
    
    def mul_opp(a,b):
        return a*b
    
    def div_opp(a,b):
        return a/b
    
mopp = MathOperations()
result_add=MathOperations.add_opp(4,7)
result_sub=MathOperations.sub_opp(34,89)
result_mul=MathOperations.mul_opp(8,9)
result_div=MathOperations.div_opp(56,7)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division : {result_div}")
        '''


#Create a class Person with a constructor that initializes the name and age of
#a person. Add a method to display these details.
'''class Person:
    def __init__(self):
        print("The details of the person are given below:")

    def detail(self,name,age):
        print("The details of the person are:",name,age)
det=Person()
det.detail("fg",34) '''


#Develop a class Rectangle with a parameterized constructor that initializes
#the length and width. Add methods to calculate and return the area and perimeter.
'''class Rectangle:
    length=0
    breath=0
    def __init__(self,l,b):
        self.length=l
        self.breath=b
    def display(self):
        print("The length is: ",self.length)
        print("The breath is :",self.breath)

    def area(self):
        area=self.length*self.breath
        return area

    def perimeter(self):
        perimeter=2*(self.length+self.breath)
        return perimeter

    def function(self):
        print("the area is :",self.area())
        print("The perimeter is :",self.perimeter())

len=Rectangle(3,7)
len.display()
len.function()'''

#Implement a class Movie with instance variables for title, director, and rating.
#Use both default and parameterized constructors to initialize these variables.
'''class Movie:
    rating=0
    def __init__(self,r):
        self.rating=r

    def display(self):
        print("The rating of this movie is:",self.rating)

    def details(self,movie_title,director):
        print("The details are:",movie_title,director)

m1=Movie(3.14)
m1.display()
m1.details("strive hard","yj") '''  


#Another example of inheritence of constructor over writing
'''class Father:
    money=1000
    def show(self):
        print("Parent class instance method")

    @classmethod
    def money_show(cls):
        print("Parent class Class method: Total Money =",cls.money)

    @staticmethod
    def sat_method():
        a=5
        print("Parent Class static method : the value of a is ",a)

class Son(Father):
    def son_display(self):
        print("Child class instance method")

s=Son()
s.show()
s.money_show()
s.sat_method()
s.son_display()         '''

#a public key
'''class Student:
    name = None
    roll=None
    branch= None
    def __init__(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    def _display(self):
        print("name: ",self.name)
        print("Roll : ",self.roll)
        print("branch: ",self.branch)
    def access_private_method(self):
        self._display()

r=Student("asd",34,'klkhk')
r.access_private_method() '''

#Design a class BankAccount with class variable bank_name, instance
#variables for account holder name and balance, and methods for depositing,
#withdrawing, and displaying account details. Include a class method to change the bank
#name and a static method to validate account numbers.
'''class BankAccount:
    bank_name= "HDFC"
    def __init__(self,accountholder_no,balance):
        self.accountholder_no= accountholder_no
        self.balance=balance

    def deposition(self,amount):
        self.balance+=amount
        print(f"Deposit amount : {amount},new balance is : {self.balance}")

    def withdrawing(self,amount):
        if amount > self.balance:
            print("Insufficient amount")
        else:
            self.balance-=amount
            print(f"Withdrew:{amount}, new balance is : {self.balance} ")

    def display(self):
        print("The bank name is {},and the account holder no is {} and the balance in it is {}".format(self.bank_name,self.accountholder_no,self.balance))


    @classmethod
    def new_bank(cls,new_name):
        cls.bank_name=new_name
        print(f"The new bank name is :{new_name}")

    @staticmethod
    def validation(account_no):
        if len(account_no)==13:
            print("It is valid")
        else:
            print("Non validation error!")

a1=BankAccount("asd12453ngln ",123)
a1.display()

a1.withdrawing(750)
a1.deposition(500)

BankAccount.new_bank("IDFC")
BankAccount.validation("1234567897")'''

""" class Number:
    even =[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)

a=Number(23)
b=Number(56)
c=Number(7)
print(Number.even)
print(Number.odd)                
 """




            



           

                