""" from tkinter import *
window = Tk()
window.title("suck!")
window.geometry('600x600')
w = Label(window,text="It sucks to come and attend workshop lecture !",font=("Arial bold",30))
w.config(bg="grey",fg="white")
c=Button(window,text='welcome to hell',width=25,command=window.destroy)
c.pack()
w.pack(side="top",pady=15,ipady=50)
window.mainloop() """

#Button formation can be done in this manner
""" from tkinter import *
a=Tk()
a.title("Button formation")
def button_clicked():
    d.config(text="Agrim said he will be a sloth in next life",bg="grey",fg="white")

d=Button(a,text="Agrim has gone mad!",command=button_clicked)
d.pack(padx=15,pady=15)    
a.mainloop()
 """
#Numeric widgets in tkinter as scale widget
""" from tkinter import *
s=Tk()
s.title("freak!")
s.geometry('800x200')

d=Scale(s,from_=0,to=100,orient=HORIZONTAL)
d.pack()
s.mainloop()
 """

#Spinbox widget
""" from tkinter import *
s=Tk()
s.title("crazy as heck")
s.geometry('800x200')

e=Spinbox(s,from_=0,to=10)
e.pack()
s.mainloop()
 """

#Boolean widgets
""" from tkinter import *
s=Tk()
s.title("It's coding time")
s.geometry('800x200')

check_var=BooleanVar()
g=Checkbutton(s,text="Agrim is dancing as shala la la",variable=check_var)
g.pack()
s.mainloop() """

#Radio Button widget
""" from tkinter import *
window=Tk()
window.title("tramp")
window.geometry('800x200')

radio_var=StringVar()
rb=Radiobutton(window,text="male",variable=radio_var,value="male")
rb2=Radiobutton(window,text="Female",variable=radio_var,value="Female")

rb.pack(padx=5,pady=5,ipadx=5,ipady=5)
rb2.pack(padx=10,pady=10,ipadx=10,ipady=10)
window.mainloop()
 """

#Selection widgets (Listbox widgets)
""" from tkinter import *
window=Tk()
window.title("time to sleep")
window.geometry('800x200')

l=Listbox(window)
l.insert(1,"Option 1")
l.insert(2,'Option 2')
l.insert(3,"Option 3")
l.pack()
window.mainloop()
 """


#Comobox Widgets
""" from tkinter import *
from tkinter.ttk import Combobox

window=Tk()
window.title("Welcome")
window.geometry('800x500')

def combobox_selected(event):
    selected_value=combobox.get()
    Label.config(text=f"seclectd: {selected_value} ")

l=Label(window,text="Select an option")
l.pack(padx=20,pady=10) 

options= ["Option 1","Option 2","Option 3"]
combobox=Combobox(window,values=options)
combobox.pack(padx=20,pady=10)

combobox.bind("<<ComboboxSelected>>",combobox_selected)
window.mainloop() """


#String widgets
""" from tkinter import *
window=Tk()
window.title("String widgets")
window.geometry('800x400')

en=Entry(window)
en.pack()

window.mainloop() """

#making a form
""" from tkinter import *
from tkinter.ttk import Combobox

window=Tk()
window.title("Login form")
window.geometry('800x200')

def entryclick():
    passward=e2.get()
    print(passward)

    if passward == 123456:
        return new
    else:
        print(text = "don't be like Neville Longbottom")  
          

l=Label(window,text="Login Form",font=50)
l.grid(row= 0,column=1000,padx=391,pady=50)

l1=Label(window,text="Username:",font=(18))
l1.grid(row=2,column=50,padx=10,pady=5)

l2=Label(window,text="Passward:",font=(18))
l2.grid(row=4,column=50,padx=10,pady=5)

l3=Label(window,text="Age: ",font=18)
l3.grid(row=6,column=50,padx=10,pady=5)

l4=Label(window,text="Gender: ",font=18)
l4.grid(row=8,column=50,padx=10,pady=5)

e1=Entry(window)
e1.grid(row=2,column=100,padx=15,pady=10)

e2=Entry(window)
e2.grid(row=4,column=100,padx=15,pady=15)

scale=Scale(window,from_=1,to=100,orient=HORIZONTAL)
scale.grid(row=6,column=100,padx=15,pady=5)

def button_clicked():
    print("The form is successfully submitted")
    b.config(text="Thanks for your kind response",bg="black",fg="white")

b=Button(window,text="Submit",command=button_clicked,font=20)
b.grid(row=12,column=1000,padx=391,pady=50) 



radi_var=StringVar()
op=Radiobutton(window,text="Male",variable=radi_var,value="Male")
op2=Radiobutton(window,text="Female",variable=radi_var,value="Female")
op.grid(row=8,column=100,padx=15,pady=10)
op2.grid(row=9,column=100,padx=15,pady=10)

check_var=BooleanVar()
checking=Checkbutton(window,text="I am not a Robot",variable=check_var)
checking.grid(row=10,column=1000,padx=391,pady=50)

def combobox_selection(event):
    selected_value=combobox.get()
    Label.config(text=f"Religion: {selected_value}")

l5=Label(window,text="Your religion: ",font=18)
l5.grid(row=11,column=50,padx=10,pady=5)

options=("Hindu","Christian","Jewish","Terrorist","Sikh")
combobox=Combobox(window,values=options)
combobox.grid(row=11,column=100,padx=15,pady=10)


new=Button(window,text="Issue Detected",command=entryclick,font=20)
new.grid(row=13,column=1000,padx=15,pady=10,sticky=S)

window.mainloop() 
 """

# Data Picker
""" from tkinter import*
from tkcalendar import DateEntry

root=Tk()
root.title("Data Picker Example")
root.geometry('800x200')

data_entry=DateEntry(root)
data_entry.pack()

root.mainloop() """

#Color Picker:
""" from tkinter import*
from tkinter import colorchooser
def choose_color():
    color_code = colorchooser.askcolor(title="choose a color")
    print(color_code)

window=Tk()
window.title("Color picker example")
window.geometry('800x200')

b=Button(window,text="Choose Color",command=choose_color)
b.pack()
window.mainloop()
 """


#Container Widgets
""" from tkinter import *

root=Tk()
root.title("Frame example")
root.geometry('800x200')

frame=Frame(root,bg="lightblue",width=200,height=100)
frame.pack()
root.mainloop() """

# Canvas widgets
""" from tkinter import *
root=Tk()
root.title("Canvas example")

c=Canvas(root,width=400,height=300)
c.pack()

c.create_line(0,0,200,100)
# c.create_polygon(2,3,40,fill="sky blue")
root.mainloop()
 """

#Calculator
""" from tkinter import *

window=Tk()
window.title("Arthemetic Calculator")
window.geometry('800x200')

def calculate():
    try:
        num1=float(e1.get())
        num2=float(e2.get())

    except ValueError:
        b.config(text="Please enter the valid number")
        return
    
    operation=operation_var.get()
    result=0

    if operation=="+":
        result = num1+num2

    elif operation=="-":
        result = num1-num2

    elif operation=="*":
        result = num1*num2

    elif operation=="/":
        b.config(text="Can't be divided by zero")
        return
        result = num1/num2
    else:
        b.config(text="please select an operation")
        return    
    b.config(text=f"Result: {result}")  

operation_var = StringVar()
operation_var.set("+")

operations_frame=Frame(window)
operations_frame.grid(row=9,column=2,padx=10,pady=5)

r1=Radiobutton(operations_frame,text="+",variable=operation_var,value="+")
r1.grid (row=9,column=2,padx=20,pady=5,sticky=W)


r2=Radiobutton(operations_frame,text="-",variable=operation_var,value="-")
r2.grid (row=9,column=4,padx=20,pady=5)

r3=Radiobutton(operations_frame,text="*",variable=operation_var,value="*")
r3.grid (row=9,column=6,padx=20,pady=5)

r4=Radiobutton(operations_frame,text="/",variable=operation_var,value="/")
r4.grid (row=9,column=8,padx=20,pady=5)



        

l1=Label(window,text="Calculator",font=50)
l1.grid(row=1,column=1000,padx=15,pady=10,sticky=E)

l2=Label(window,text="Number 1:",font=38)
l2.grid(row=3,column=1,padx=10,pady=5,sticky=W)

l3=Label(window,text="Number 2:",font=38)
l3.grid(row=5,column=1,padx=10,pady=5,sticky=W)

l4=Label(window,text="Operations: ",font=38)
l4.grid(row=9,column=1,padx=5,pady=5,sticky=W)

e1=Entry(window)
e1.grid(row=3,column=4,padx=20,pady=15,sticky=N)

e2=Entry(window)
e2.grid(row=5,column=4,padx=20,pady=15,sticky=N) 


def button_skill():
    print("The sum has been calculated")
    b.config(text="You have sucessfully calculated all the arthematic operation")

b=Button(window,text="Result",bg="grey",fg="Black",font=30)
b.grid(row=13,column=500,padx=15,pady=10,sticky=S)   

c=Button(window,text="Calculation",command=calculate)
c.grid(row=12,column=500,padx=15,pady=10,sticky=S)

window.mainloop()
"""

#image
""" from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk

import_url="https://img.goodfon.com/wallpaper/big/4/df/welcome-to-hell-smert-ad-satana-uzhas-goriashchie-glaza-prei.jpg"

root=tk.Tk()
data=urlopen(import_url)
image=ImageTk.PhotoImage(data=data.read())
tk.Label(root,image=image,text="Welcome to hell Vampire chronicles",font=20).pack()
root.mainloop()  """

#Image formation 
from urllib.request import urlopen
import tkinter as tk
from PIL import ImageTk

window=tk.Tk()
window.title("Welcome to my blog")
window.geometry('800x200')

image_url="https://img.goodfon.com/wallpaper/big/4/df/welcome-to-hell-smert-ad-satana-uzhas-goriashchie-glaza-prei.jpg"
s=tk.Label(window,text="This a a very big gossip",font=20)
s.pack()


data=urlopen(image_url)
image=ImageTk.PhotoImage(data=data.read())

def flash():
    b.config(text="I am dean",bg="black",fg="white",image=image)
    print("I am dean")

b=tk.Button(window,text="This is the dean",command=flash)
b.pack()


window.mainloop()



