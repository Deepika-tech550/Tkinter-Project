from tkinter import *

root= Tk()
v=StringVar()
root.geometry('500x700')
root.configure(bg='Violet')
root.title('TO-DO APP')

l= Label(text='TO-DO APP',font=('Courier',30))
l.pack(padx=9,pady=15,side=TOP)
         
l1= Listbox(width=30,height=15,font=('Courier',15,'bold'))
l1.place(x=70,y=80)

e=Entry(width=18,font=('Courier',20,'bold'),textvariable=v)
e.place(x=100,y=450)
def add():
    var=e.get()
    l1.insert(END,var)
    v.set('')

def dele():
    l1.delete(ANCHOR)

b= Button(text='ADD',width=10,height=3,bg='Green',fg='White',command=add)
b.place(x=130,y=500)

b1=Button(text='DELETE',width=10,height=3,bg='Red',fg='White',command=dele)
b1.place(x=300,y=500)

root.mainloop()
