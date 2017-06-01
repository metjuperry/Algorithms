from Tkinter import *
import time

import tkMessageBox # if you want pop ups


class Gui:
    def __init__(self, master):
        topframe = Frame(master)
        bottomframe = Frame(master)

        topframe.pack()
        bottomframe.pack(side=BOTTOM)

        self.button1 = Button(topframe, text="Button 1", command=lambda: self.recog(1))
        self.button2 = Button(topframe, text="Button 2", command=lambda: self.recog(2))
        self.button3 = Button(bottomframe, text="Button 3", command=lambda: self.recog(3))

        self.button1.pack(side=LEFT)
        self.button2.pack(side=LEFT)
        self.button3.pack()

    @staticmethod
    def recog(n):
        print "This is button", n


def click():
    print "Not doing anything just yet"


blank = Tk()
blank.geometry("500x300")

# Top Menu
menu = Menu(blank)
blank.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New file", command=click)
subMenu.add_command(label="Save file", command=click)
subMenu.add_command(label="Load file", command=click)
subMenu.add_separator()
subMenu.add_command(label="Settings", command=click)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=blank.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Edit", command=click)

# Toolbar

toolbar = Frame(blank)

insertButt = Button(toolbar, text="Insert", command=click)
insertButt.pack(side=LEFT, padx=2, pady=2)

printButt = Button(toolbar, text="Print", command=click)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# Status bar

statusBar = Label(blank, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

b = Gui(blank)

# Message boxes - this currently kinda breaks the program.

tkMessageBox.showinfo('Window Title', "This is a bunch of text")

# answer = tkMessageBox.askquestion('Question 1', 'Do you like silly faces?')

# if answer == 'yes':
#     print "Zdenda"

# Shapes and graphics

canvas = Canvas(blank, width=200, height=100)
canvas.pack()

blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill="red")
middle = canvas.create_text(0 + (200 - 0)/3, 100 + (50 - 100)/3,text="Middle?")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

# canvas.delete(redline)
# canvas.delete(ALL)

# Images - works on gifs, not pngs.

# Photo = PhotoImage(file="print.png")
# label = Label(blank, image=Photo)

# label.pack()

canvas = Canvas(blank)
canvas.pack()

circleX = (25, 25)
circleY = (35, 35)

circle = canvas.create_oval(circleX, circleY, fill="red")
label = canvas.create_text(35, 45, text="Bitch")


def move():
    for step in range(50):
        x = 5
        time.sleep(0.0025)
        canvas.move(circle, x, 0)
        canvas.move(label, x, 0)
        canvas.update()


button = Button(blank, text="MOVE BITCH", command=move)
button.pack(side=BOTTOM)

blank.mainloop()
