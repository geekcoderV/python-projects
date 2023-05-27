#import files/modules
import time
from tkinter import *
from tkinter import messagebox


#main programming session
window = Tk()
window.title("Confession")
window.configure(background= "dark red")

#Creating a text
txt = Label(window, text="I like you, would you like to be my girl friend?", bg="dark red", fg="black", font=("Arial Bold",20))
txt.grid(column=0,row=0)

#creating a functionning buttons
def Yes_button():
    messagebox.showinfo("Accepted","I am glad to have your respond")

btn = Button(window, text="Yes", command=Yes_button, font=("Arial Bold",20))
btn.grid(column=0,row=1)

def No_button():
    while True:
        messagebox.showinfo("Rejection","PLEASE")
        time.sleep(0.1)
                        
btn1 = Button(window, text='No', command=No_button, font=("Arial Bold",20))
btn1.grid(column=0,row=2)

window.mainloop()