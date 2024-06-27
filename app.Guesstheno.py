#GUESS THE NUMBER
from urllib.request import urlopen
from tkinter import*
import random
from PIL import ImageTk


window=Tk()
window.title("GUESS THE NUMBER")
window.geometry('800x200')
window.minsize(200,400)

image_url="https://cdn.memes.com/up/77021971602474177/i/1604138690995.jpg"

data=urlopen(image_url)
image=ImageTk.PhotoImage(data=data.read())


attempts=10
solution =random.randint(1,99)

def Checking():
    global attempts
    global tex

    attempts-=1

    guess=int(e1.get())

    if solution == guess:
        tex.set("YOU WON CONGRATS!!")
        b1.pack_forget()

    elif guess < solution:
        tex.set("INCORRECT YOU HAVE"  +   str(attempts)   +  "REMAINING GO HIGHER")  

    elif guess > solution:
        tex.set("INCORRECT YOU HAVE"  +  str(attempts)    +  "REMAINING GO LOWER")

            
        return
    
   
  

def Out():
    b2.config(text="QUIT",image=image,bg="black",fg="white",height=700,width=1000)

   

l=Label(window,text="Guess the number between 1 to 99",font=20)
l.config(bg="white",fg="Black")
l.grid(row=0,column=0,padx=20,pady=10,sticky=N)

e1=Entry(window,font=20)
e1.grid(row=1,column=0,padx=50,pady=50,ipadx=100,ipady=5,sticky=N)

f=Frame(window)
f.grid()

b1 =Button(f,text="CHECK",font=20,height=4,width=9,command=Checking)
b1.config(fg="white",bg="black")
b1.grid(row=3,column=1,ipadx=15,ipady=5,sticky=N)

b2=Button(f,text="QUIT",font=20,height=4,width=9,command=Out)
b2.config(fg="white",bg="black")
b2.grid(row=4,column=1,ipadx=15,ipady=5,sticky=E)

tex=StringVar()
tex.set("You have 10 attemps Remaining!Good luck!!")

attempts_left=Label(textvariable=tex,font=50)
attempts_left.grid()
window.mainloop()