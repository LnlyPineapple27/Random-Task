from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Fuck yeah!')
root.geometry("400x400")

def selected(event):
    print("No")
    myLabel = Label(root, text = clicked.get()).pack()
    if clicked.get() == "Fri":
        myLabel = Label(root, text = "Oh yeah! It's Friday!").pack()
    else:
        myLabel = Label(root, text = "Oh noooo! It's " + str(clicked.get())).pack()

def comboclick(event):
    print(myCombo.get())
    myLabel = Label(root, text = myCombo.get()).pack()



option = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
clicked = StringVar()
clicked.set(option[0]) # Set default item

drop = OptionMenu(root, clicked, *option, command = selected) # get intuitive of option
drop.pack(pady = 20) # căn lề ngang


myCombo = ttk.Combobox(root, value = option)
myCombo.current(0)
myCombo.bind("<<Combo selected>>", comboclick)
myCombo.pack()

# myButton = Button(root, text = "Select from list", command = selected)# This Button shall call function 'selected'
# myButton.pack()


root.mainloop()
