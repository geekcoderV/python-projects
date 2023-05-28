#Download the tkinter package on cmd using 'pip install tkinter'
#Download the turtle package on cmd using 'pip install turtle'




#import files/modules
from tkinter import *
from tkinter import messagebox
import turtle
import time
#main programming session

windows = Tk()
windows.title("Confession")
#windows.geometry("420x200")
windows.configure(background="dark red")

txt = Label(windows, text="I like you, would you like to be my girlfriend?", bg="dark red", fg="black", font=("Arial Bold", 20))
txt.grid(column=0,row=0)

#functioning buttons
def Yes_button():
    messagebox.showinfo("Accepted","I am very glad to have your respond")
    #turtle art code
    pen = turtle.Turtle()

    def curver():
        for i in range(200):
            pen.right(1)
            pen.forward(1)
    def heart():
        pen.fillcolor('red')
        pen.begin_fill()
        pen.left(140)
        pen.forward(113)
        curver()
        pen.left(120)
        curver()
        pen.forward(112)
        pen.end_fill()

    def txt():
        pen.up()
        pen.setpos(-68, 95)
        pen.down()
        pen.color('lightgreen')
        pen.write('I LOVE YOU', font=("Verdana",12,"bold"))

    heart()
    txt()
    pen.ht()
    time.sleep(10)

    
btn = Button(windows, text="Yes", command=Yes_button, font=("Arial Bold", 20))
btn.grid(column=0,row=1)

def No_button():
    messagebox.showinfo("Rejection","Maybe anytime soon, I wont give up")

btn1 = Button(windows, text="No", command=No_button, font=("Arial Bold",20))
btn1.grid(column=0,row=2)

windows.mainloop()
