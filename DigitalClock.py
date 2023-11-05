from tkinter import *

#create a class of the object Tk()
screen=Tk()

#program for the graphics customization
screen.configure(bg='yellow')
screen.geometry("1025x500")
screen.title("The Digital Clock")


#making of the label boxes

#----format-----
#MainLabels : label1 initialized
#             label1 positioned
#SubLabels :  label11 initialized ( we are very sorry as we cannot make it upto the mark as label1.1 as '.' operator has specific significance in the python)
#             label11 positioned

label1=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label1.place(x=40,y=40,height=100,width=200)
label11=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label11.place(x=40,y=40,height=100,width=200)



label2=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label2.place(x=290,y=40,height=100,width=200)
label21=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label21.place(x=40,y=40,height=100,width=200)


label3=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label3.place(x=540,y=40,height=100,width=200)
label31=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label31.place(x=40,y=40,height=100,width=200)


label4=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label4.place(x=790,y=40,height=100,width=200)
label41=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label41.place(x=40,y=40,height=100,width=200)




label5=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label5.place(x=40,y=280,height=100,width=200)
label51=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label51.place(x=40,y=40,height=100,width=200)


label6=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label6.place(x=290,y=280,height=100,width=200)
label61=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label61.place(x=40,y=40,height=100,width=200)


label7=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label7.place(x=540,y=280,height=100,width=200)
label71=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label71.place(x=40,y=40,height=100,width=200)


label8=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label8.place(x=790,y=280,height=100,width=200)
label81=Label(screen,text="20",font=('Arial Narrow',80,"bold"),bg='red',fg='black')
label81.place(x=40,y=40,height=100,width=200)


#the object creates the graphics
#the mainloop() fynction holds it untill closed
screen.mainloop()

