'''
print(r'c:\docs\aditi')
'''
'''
a = "python"
print(a[4:1:-1])
'''

'''i = 10

if (i < 15):
    print("10 is less than 15")
else:    
    print("I am Not in if")
'''
'''def multiply(a,b):
    """ hello """
    return a*b
print(multiply.__doc__)'''

'''name="Alice"
age=25
print("%s is %d years old." % (name,age))'''
#where s is a string and d is a number

#dot format method
'''name=" adi"
branch="iot"
print("{} is in {}. " . format(name,branch))'''

'''product = "python course"
price = 99.1111
print("{name} costs ${price:.3f}.".format(name=product,price=price))'''

'''name ="Aditi"
age=18
print(f"{name} is {age} years old.")
'''

'''a= "and"
c= "but"
b = 2
print(f"{a} ,{c} are the {b} are the two types of conjuction.")
 
'''
'''x= "adi"
y= 4
print(type(x))
print(type(y))'''

#implicit
'''a=10
b=2.3
c=a+b
print (c)'''

#explicit
'''a=2
b=float(a)
print(b)'''

#Operators
'''percentage=int(input("enter your percentage: "))
if percentage >= 90:
    print("grade a")
elif percentage >=80:
    print("grade b")
elif percentage >=70:
    print("grade c")
elif percentage >=60:
    print("grade d")
else:
    print("fail")'''  


'''s=0
for i in range(1,5):
    s+=i
    for j in range(s):
        print(s, end=" ")
    print()    
    '''


'''n = int(input("Enter the number of rows: "))

for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end="")
    print()'''

def is_even(*n):
    for i in n:
        if i%2==0:
            print("true") 
        else:
            print("false") 
c=[1,2,3,4,5,6,7,8]
# for i in c:
#     print(i)
#     a = is_even(i)
#     # print(a)

print(is_even(1,2,3,4,5,6,7,8))




