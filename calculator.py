from tkinter import *

import tkinter.messagebox as messagebox
root= Tk()


root.geometry('350x400')
root.configure(bg='Blue')
root.title('Calculator')


operator = ''
var= StringVar()

# create entry
e= Entry(width=30,borderwidth=3,textvariable=var,font=('courier',10))
e.place(x=280,y=40,anchor='ne')

# fun
def btclick(num):
    global operator
    operator = operator + str(num)
    var.set(operator)
   
    

#button


b1= Button(text='7',width=5,height=2,command=lambda:btclick(7))
b1.place(x=55,y=80)

b2= Button(text='8',width=5,height=2,command=lambda:btclick(8))
b2.place(x=110,y=80)

b3= Button(text='9',width=5,height=2,command=lambda:btclick(9))
b3.place(x=165,y=80)

b4= Button(text='/',width=5,height=2,command=lambda:btclick('/'))
b4.place(x=220,y=80)

b5= Button(text='4',width=5,height=2,command=lambda:btclick(4))
b5.place(x=55,y=140)

b6= Button(text='5',width=5,height=2,command=lambda:btclick(5))
b6.place(x=110,y=140)

b7= Button(text='6',width=5,height=2,command=lambda:btclick(6))
b7.place(x=165,y=140)

b8= Button(text='x',width=5,height=2,command=lambda:btclick('*'))
b8.place(x=220,y=140)


b9= Button(text='1',width=5,height=2,command=lambda:btclick(1))
b9.place(x=55,y=200)


b10= Button(text='2',width=5,height=2,command=lambda:btclick(2))
b10.place(x=110,y=200)

b11= Button(text='3',width=5,height=2,command=lambda:btclick(3))
b11.place(x=165,y=200)

b12= Button(text='-',width=5,height=2,command=lambda:btclick('-'))
b12.place(x=220,y=200)
def clear():
    global operator
    operator=''
 
    var.set(operator)

bc= Button(text='C',width=5,height=2,command=clear)
bc.place(x=55,y=260)

b0= Button(text='0',width=5,height=2,command=lambda:btclick(0))
b0.place(x=110,y=260)
def equal():
    try:
        global operator
        a=eval(operator)
        var.set(a)
        operator=''
    except ZeroDivisionError:
        messagebox.showinfo('Error!!','You are dividing by zero')
    except:
        messagebox.showinfo('Result','Invalid Pattern')
        
    
b13= Button(text='=',width=5,height=2,command=equal)
b13.place(x=165,y=260)


b14= Button(text='+',width=5,height=2,command=lambda:btclick('+'))
b14.place(x=220,y=260)

root.geometry()
