#Scientific calculator
from tkinter import*
windows=Tk()
windows.title("Scientific Calculator")
windows.geometry('800x200')

equation_text=""
equation_label= StringVar()

total=0
s=0



def button_press(num):
    
    global equation_text

    equation_text=equation_text + str(num)

    equation_label.set(equation_text)

def Equals():
    global equation_text
    try:
        total=str(eval(equation_text))
        
        equation_label.set(total)
        
        equation_text=total
        
    except SyntaxError:
        
        equation_label.set("Syantax error")

        equation_text=""    
    
    except ZeroDivisionError:
      
        equation_label.set("arthematic error")
       

        equation_text="" 


    

def Clear():
    global equation_text 

    

    equation_label.set("")

    equation_text=""

def Back_space():
    global equation_text

    equation_text=equation_text[:-1]

    equation_label.set(equation_text)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
def Bitwise_left_shift():
    global equation_text

    equation_text=equation_text + "<<"

    equation_label.set(equation_text)

def Bitwise_right_shift():
    global equation_text

    equation_text=equation_text + ">>"

    equation_label.set(equation_text)

def Modulus():
    global equation_text

    equation_text=equation_text + "%"

    equation_label.set(equation_text)        

l1=Label(windows,text="Scientific Calculator",font=40)
l1.config(bg="Black",fg="white")
l1.grid(row=0,column=0,padx=20,pady=15,sticky=N)

e1=Entry(windows,textvariable=equation_label,font=20)
e1.grid(row=0,column=0,padx=50,pady=50,ipadx=200,ipady=10,sticky=W)

f=Frame(windows)
f.grid()

t1=Button(f,text="<<",font=30,height=4,width=9,command=Bitwise_left_shift)
t1.config(bg="Black",fg="white")
t1.grid(row=1,column=0)

t2=Button(f,text=">>",font=30,height=4,width=9,command=Bitwise_right_shift)
t2.config(bg="Black",fg="white")
t2.grid(row=1,column=1)

t3=Button(f,text="C",font=30,height=4,width=9,command=Clear)
t3.config(bg="Black",fg="white")
t3.grid(row=1,column=3)

s1=Button(f,text="B",font=30,height=4,width=9,command=Back_space)
s1.config(bg="Black",fg="white")
s1.grid(row=1,column=4)

t4=Button(f,text="(",font=30,height=4,width=9,command=lambda:button_press("("))
t4.config(bg="Black",fg="white")
t4.grid(row=2,column=0)

t5=Button(f,text=" ) ",font=30,height=4,width=9,command=lambda:button_press(" ) "))
t5.config(bg="Black",fg="white")
t5.grid(row=2,column=1)

t6=Button(f,text="=",font=30,height=4,width=9,command=Equals)
t6.config(bg="Black",fg="white")
t6.grid(row=2,column=3)

s2=Button(f,text="/",font=30,height=4,width=9,command=lambda:button_press("/"))
s2.config(bg="Black",fg="white")
s2.grid(row=2,column=4)

b1=Button(f,text="7",font=30,height=4,width=9,command=lambda:button_press(7))
b1.config(bg="Black",fg="white")
b1.grid(row=3,column=0)

b2=Button(f,text="8",font=30,height=4,width=9,command=lambda:button_press(8))
b2.config(bg="Black",fg="white")
b2.grid(row=3,column=1)


b3=Button(f,text="9",font=30,height=4,width=9,command=lambda:button_press(9))
b3.config(bg="Black",fg="white")
b3.grid(row=3,column=3)

s3=Button(f,text="*",font=30,height=4,width=9,command=lambda:button_press("*"))
s3.config(bg="Black",fg="white")
s3.grid(row=3,column=4)

b4=Button(f,text="4",font=30,height=4,width=9,command=lambda:button_press(4))
b4.config(bg="Black",fg="white")
b4.grid(row=4,column=0)

b5=Button(f,text="5",font=30,height=4,width=9,command=lambda:button_press(5))
b5.config(bg="Black",fg="white")
b5.grid(row=4,column=1)


b6=Button(f,text="6",font=30,height=4,width=9,command=lambda:button_press(6))
b6.config(bg="Black",fg="white")
b6.grid(row=4,column=3) 

s4=Button(f,text="-",font=30,height=4,width=9,command=lambda:button_press("-"))
s4.config(bg="Black",fg="white")
s4.grid(row=4,column=4)

b7=Button(f,text="1",font=30,height=4,width=9,command=lambda:button_press(1))
b7.config(bg="Black",fg="white")
b7.grid(row=5,column=0)


b8=Button(f,text="2",font=30,height=4,width=9,command=lambda:button_press(2))
b8.config(bg="Black",fg="white")
b8.grid(row=5,column=1)


b9=Button(f,text="3",font=30,height=4,width=9,command=lambda:button_press(3))
b9.config(bg="Black",fg="white")
b9.grid(row=5,column=3)


s5=Button(f,text="+",font=30,height=4,width=9,command=lambda:button_press("+"))
s5.config(bg="Black",fg="white")
s5.grid(row=5,column=4)

u1=Button(f,text="!",font=30,height=4,width=9,command=lambda:button_press("!"))
u1.config(bg="Black",fg="white")
u1.grid(row=6,column=0)

u2=Button(f,text=".",font=30,height=4,width=9,command=lambda:button_press("."))
u2.config(bg="Black",fg="white")
u2.grid(row=6,column=1)

u3=Button(f,text="0",font=30,height=4,width=9,command=lambda:button_press(0))
u3.config(bg="Black",fg="white")
u3.grid(row=6,column=3)

u4=Button(f,text="=",font=30,height=4,width=9,command=Equals)
u4.config(bg="Black",fg="white")
u4.grid(row=6,column=4)




windows.mainloop()