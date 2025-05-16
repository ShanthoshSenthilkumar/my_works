from tkinter import *

form1=Tk()
form1.geometry("500x500")

lbl=Label(form1,text="Login Form",bg="red",fg="Yellow",font=("times new roman",30))
lbl.pack()

lbl1=Label(form1,text="Username",bg="yellow",fg="red",font=("times new roman",20))
lbl1.place(x=50,y=100)

text=Entry(form1,font=("Times new roman",20),bg="yellow",fg="red")
text.place(x=200,y=100)

lbl2=Label(form1,text="Password",bg="yellow",fg="red", font=("Times new roman",20))
lbl2.place(x=50,y=200)


text=Entry(form1,font=("times new roman",20),bg="yellow", fg="red")
text.place(x=200,y=200)

btn=Button(form1,text="Submit",bg="red",fg="Yellow",font=("Times new roman",15))
btn.place(x=150,y=250)




form1.mainloop()
