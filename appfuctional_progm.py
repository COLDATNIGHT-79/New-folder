#Immutability
'''coordinates = (10,20)
new_coordinates = coordinates + (30,)
print(coordinates)
print(new_coordinates)'''

#Closures:
'''def outerFunction(text):
    t=text
    def innerfunction():
        print(t)
    return innerfunction
myfuction=outerFunction("hey!")
myfuction() ''' 

#Another example of closure
'''def outerfunction(x):
    def innerfunction():
        print(x)
    return innerfunction
myfun=outerfunction(6)
myfun()    
'''

#Anotherv examnple of closure function
'''def make_counter():
    count=0
    def counter():
        nonlocal count
        count+=1
        return count
    return counter

c1=make_counter()
c2=make_counter()
print(c1())
print(c1())
print(c1())

print(c2())
print(c2())

print(c1())
'''

#DECORATOR
'''def decor(fun):
    def inner():
        print("--------- ")
        fun()
        print("---------")
    return inner
@decor
def msg():
    print("python programming")
msg=decor(msg)
msg() '''

#Another program 
'''from datetime import datetime 
def not_during_night(func):
    def inner():
        if 7 <=datetime.now().hour < 22:
            func()
        else:
            print("Sorry! Unable to play music in night")
    return inner

@not_during_night
def music():
    print("playing Music")

music()'''

#Generator
'''def generate_numbers():
    for num in range(1,11):
        yield num

numbers_generator=generate_numbers()
print(type(numbers_generator))

for numb in numbers_generator:
    print(numb)'''

#Create an lst for an iterable form

'''class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x
    
ob=MyNumber()
myiter=iter(ob)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))'''

#Declarative programming
'''n=[1,2,3,4,5]
even_number=list(filter(lambda x: x%2==0,n))
print(even_number)'''

#Another program
'''from functools import reduce
n=[1,2,3,4,5,6]
total=reduce(lambda x,y:x+y,n)
print(total)
'''

#




