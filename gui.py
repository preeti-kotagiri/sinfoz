import tkinter
window = tkinter.Tk()
window.geometry('300x400')
name_label = tkinter.Label(window,text = "user name")
name_label.grid(0,0)

name_entry = tkinter.Entry(window)
name_entry.pack()
window.mainloop()
