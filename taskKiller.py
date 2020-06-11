from tkinter import messagebox
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import Pack
from os import system

def TaskKill(event):
	task = entry.get()
	rtrn = os.system('taskkill /f /im ' + entry.get())
	if rtrn == 1:
		messagebox.showinfo("OK!", "Completed! Successfully taskkilled " + task + "!")
	elif rtrn == 128:
		messagebox.showerror("OOPS!!!", "Oops! Process not found!")
	else:
		messagebox.showerror("OOPS!!!", "Oops! Something went wrong! There is a status code: " + str(rtrn))
	entry.delete(0, 'end')

MainWindow = Tk()

MainWindow.geometry("24x65")

MainWindow.title("Task Killer")

label  = Label(text="Like \"cmd.exe\"", width=12)
entry  = Entry(MainWindow, width=12)
button = Button(MainWindow, text="Kill task!", width=20, height=1)

button.bind('<Button-1>', TaskKill)
MainWindow.bind('<Return>', TaskKill)

label.pack()
entry.pack()
button.pack()

MainWindow.mainloop()