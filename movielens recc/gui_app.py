# GUI - Graphical User Interface

# Libraries
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()
app.title('My App')
app.geometry('600x400')

ttk.Label(app, text = 'A simple text Label').place(x=50 , y=50)
ttk.Label(app, text = "hello bro").place(x= 1 , y = 1)

app.mainloop()