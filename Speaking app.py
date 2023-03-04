from tkinter import *
#import pyttsx3
from PIL import Image
root=Tk()

root.title('Speaking App')
root.geometry('600x600')


img= PhotoImage(file='C:\\Users\\logo.png')
l2= Label(image=img,width=370,height=200)
l2.pack(side=TOP)
var= StringVar()
def speak():
    friend= pyttsx3.init()
    
    friend.say(e.get())
    friend.runAndWait()
    friend.stop()
    print('Speaked')
    

def refresh():
    var.set('')



    
l= Label(text='Speaking App',font=('Baskerville Old Face',50,'bold'))
l.pack(side=TOP)

form= Frame(root)
form.pack(fill=X)

l1=Label(form,text='Enter Text To Speak',font=('Baskerville Old Face',18,'bold'))
l1.grid(row=0,column=1,padx=10,pady=40)

e= Entry(form,textvariable=var,width=30,bd=4,font=('Baskerville Old Face',16,'bold'))
e.grid(row=0,column=2,padx=10,pady=40)

b= Button(root,text='Speak',fg='White',bg='Green',font=('Baskerville Old Face',18,'bold'),width=7,command=speak)
b.pack()
b1= Button(root,text='Refresh',fg='White',bg='Red',font=('Baskerville Old Face',18,'bold'),width=7,command=refresh)
b1.pack(padx=9,pady=7)

root.mainloop()
