from tkinter import *
import backend
window = Tk()

window.wm_title("Quick Definations and Dictionary app")
#functions
def find():
    try:
        word = backend.findWord(e1_value.get())
        t1.insert(END, word)
    except TclError:
        t1.insert(END, "You have entered a wrong word. Please re-check the word")
#label
l1 = Label(window, text="Enter the word")
l1.grid(row=0,column=0)
#input text box
e1_value = StringVar()
e1 = Entry(window,width=30,textvariable=e1_value)
e1.grid(row=0,column=2)

#button
b1 = Button(window, text="Find", width=12, command=find)
b1.grid(row=2,column=4)
b2 = Button(window, text="About", width=12)
b2.grid(row=3,column=4)
b3 = Button(window, text="Close", width=12, command=window.destroy)
b3.grid(row=4,column=4)

#output text box
t1 = Text(window, height=9, width=38)
t1.grid(row=2, column=0, rowspan=30, columnspan=3)
window.mainloop()