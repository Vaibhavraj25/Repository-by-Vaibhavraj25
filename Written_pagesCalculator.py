from tkinter import *
root = Tk()
a = 0
b = str(a)
def onclick():
	global a 
	a = a+1
	global b
	b = str(a)
	Label2.configure(text = b)
	
Label1 = Label(root, text = "Pages Calculator", fg = 'red', font = ('Bold' ,20, 'normal'))
Label1.pack()
Label2 = Label(root, text = b , fg = 'green', font = ('Airel', 30, 'normal'))
Label2.pack()
Button1 = Button(root, text = "1 page Completed", fg = "white", bg = 'red', activebackground = 'red', activeforeground = 'white',command = onclick)
Button1.pack()
Label3 = Label(root, text = "MyTarget - 40pages")
Label3.pack()
root.mainloop()
