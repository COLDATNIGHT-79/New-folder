from tkinter import*
window=Tk()
window.title("TO DO LIST")
window.geometry('800x200')

def fuctionality():
    pass

e1=Entry(window)
e1.grid(row=4,column=1,padx=35,pady=25,columnspan=1,sticky=N)

f=Frame(window)
f.grid()

b1=Button(f,text="Submit",command=fuctionality,width=4)
b1.config(bg="white",fg="black")
b1.grid(row=4,column=6)


window.mainloop()
