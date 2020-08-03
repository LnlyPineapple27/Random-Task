from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('dat Testzone')
# root.iconbitmap('D:/pic/dicpic.ico')
root.geometry("400x400")

# Drop down boxes
def show():
    myLabel = Label(root, text = clicked.get()).pack() # print out to frame the input of 'clicked'
    # print("Mlem " +  str(clicked.get()))

option = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
clicked = StringVar()
clicked.set(option[0]) # Set default item

drop = OptionMenu(root, clicked, *option) # get intuitive of option
drop.pack()

myButton = Button(root, text = "Show selection", command = show).pack()
root.mainloop()
