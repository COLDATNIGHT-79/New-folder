from urllib.request import urlopen
from tkinter import*
from PIL import ImageTk

window=Tk()
window.title("Introducing myself")
window.geometry('800x200')

image_url="https://static1.srcdn.com/wordpress/wp-content/uploads/2018/02/harry-potter-logic-mems.jpg"

data=urlopen(image_url)
image=ImageTk.PhotoImage(data=data.read())

def my_name():
   t=  "Hello"  +   e1.get()
   my_label=Label(window , text =  t,font=20)
   my_label.config(image=image)
   my_label.grid(row=5,column=1)
 


l=Label(window,text="Enter your Name:",font=20,bg="black",fg="white")
l.grid(row=2,column=1,padx=5,pady=2,sticky=W)

e1=Entry(window,fg="black",bg="white")
e1.grid(row=2,column=3,padx=25,pady=10,sticky=N)


f=Frame(window)
f.grid()

b=Button(f,text="click",command=my_name,font=20)
b.grid(row=4,column=3,padx=10,pady=5,sticky=E)

window.mainloop()