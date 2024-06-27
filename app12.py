'''n = int(input("Enter the number of rows: "))

for i in range(0, n):
    for j in range(0, i+1):
        print("i", end="")
    print()
'''
'''for i in range (1,10,):
    for j in range(i):
        print(i,end="")
    print()    '''

'''n=int(input("enter the number"))
for i in range(n-1):
    for j in range (i-1):
        print("*",end="")
    print()    
'''
'''def fun(a,b,c,d):
    print(a,b,b,c,d)
my_list=[1,2,3,4]
fun(*my_list)    
'''

'''def add(a1,a2):
    return a1+a2
a1=3
a2=4
print(add(a1,a2))'''

'''def max_num(a,b,c):
    s=max(a,b,c)
    d=a+b+c
    return s,d
print(max_num(2,3,5))
    '''


'''import math
def factoraial(a,):
    z=math.factorial(a)
    return z
print(factoraial(3))'''


'''def fac(a,):
    i=1
    z=1
    while(i<=a):
        z*=i
        i+=1
    return z
print(fac(3))    
'''

'''for i in range(4):
    print(" "*(i),end="")
    for j in range(4-i):
        print("*",end=" ")
    print('\n')'''  


'''numbers=[1,2,3,4,5,6,7,8,9,10]
def is_even(n):
    if n % 2==0:
        return True
even_number =filter(is_even,numbers)
even_number_list=list(even_number)
print(even_number_list)    '''


#filter function
'''numbers=[1,2,3,4,5,6,7,8,9]
even_number=filter(lambda n: n%2==0,numbers)
even_number_list=list(even_number)
print(even_number_list)'''

'''age=[5,10,16,18,25,27]
adults=list(filter(lambda x: x>18 ,age))
print(adults)
'''


'''#map function
num_list=[1,2,3,4,5,6,7,8,9,10]
cube_list = list(map(lambda x: x**2 ,num_list))
print(cube_list)
'''

'''a=["APPLE","Banana","Cerry","Orange"]
b=list(filter(lambda x: x.isupper() ,a))
print(b)'''

'''a=[10,20,30,40,50]
b=map(lambda r: 3.14*r*r,a)
area_list=list(b)
print(area_list)'''

#Reduce function is used ton perform the mathematical functions
#printing the largest number
'''from functools import reduce
num_list=[20,12,30,79,30,100,90]
large=reduce(lambda x,y:x if x>y else y ,num_list)
print(large)
'''


#summing all the parts using reduce module
'''from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
b=reduce(lambda x,y:x+y ,a)
print(b)
'''



    



    

