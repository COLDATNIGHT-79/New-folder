#Timing fuction excecution
#Write a function that measures the time of an function takes to execute
""" import time
def timer(func):
    def wrap(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} rann in the {end-start} time")
        return result
    return wrap

@timer
def exp(n):
    time.sleep(n)

exp(5) """

#Debugging the function cell
# create a decorator to print the function name and the values of the srguments every time the function is called
""" def function (name):
    def wrapper(*args,**kwargs):
        args_value= ', '.join(str(arg) for arg in args )
        kwargs_value=', '.join(f"{k}={v}"for k ,v in kwargs.items())
        print(f"calling:{name.__name__}with args {args_value} and {kwargs_value}")
        return name(*args,**kwargs)
    
    return wrapper
@function
def hello():
    print("hello")

@function
def greet(s,d="hello"):
    print(f"{d},{s}")

hello()
greet("chai",d="hanji")  """












