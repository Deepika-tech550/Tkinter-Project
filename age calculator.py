from tkinter import *
from datetime import *
import tkinter.messagebox as messagebox
from PIL import Image
# date.today()  --> (2021,month,date)
# store date.today in variable (a=date.today())
#datetime.date(2021, 6, 18) call a.year,a.day,a.month
root = Tk()

img= PhotoImage(file='C:\\Users\\ELCOT\\Downloads\\age.png')
i = Label(image=img)
i.pack(padx=100,pady=30,side=RIGHT)
root.geometry('700x580')

global var
var =StringVar()
global var1
var1 =StringVar()
global var2
var2 =StringVar()



def calc():
    
        
    try:
        today = date.today()
        age = int(today.year)- int(var2.get())
        messagebox.showinfo('Age','Your age is '+str(age))
        
    except:
        messagebox.showinfo('Age','Incorrect Data format')
        
        
       


def refresh():
    var.set('')
    var1.set('')
    var2.set('')
    
    
        
    

l = Label(root,text='AGE CALCULATOR',font=('Algerian',20,'bold'))
l.pack(anchor='ne')


f = Frame(root)
f.pack(fill=X)
l1 = Label(f,text="Date",font=('Algerian',12,'bold'))
l1.grid(row=1,column=0,padx=10,pady=30)
e1= Entry(f,font=('Algerian',12,'bold'),borderwidth=3,textvariable=var)
e1.grid(row=1,column=3,padx=10)

l2 = Label(f,text="Month",font=('Algerian',12,'bold'))
l2.grid(row=2,column=0,padx=10,pady=30)
e2= Entry(f,font=('Algerian',12,'bold'),borderwidth=3,textvariable=var1)
e2.grid(row=2,column=3,padx=10)


l3 = Label(f,text="Year",font=('Algerian',12,'bold'))
l3.grid(row=3,column=0,padx=10,pady=30)
e3= Entry(f,font=('Algerian',12,'bold'),borderwidth=3,textvariable=var2)
e3.grid(row=3,column=3,padx=10)

b= Button(root,text='Calculate Age',font=('Algerian',14,'bold'),fg='White',bg='Green',command=calc)
b.pack()

b1 = Button(root,text='Refresh',font=('Algerian',14,'bold'),fg='White',bg='Red',command=refresh)
b1.pack()

root.mainloop()
