import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.geometry("300x250")
frame.title("Jolly Mcking")
frame.configure(bg='pink')  # Set the background color to pink

def ok():
    passw = password.get()
    usern = username.get()
    
    if not usern:
        messagebox.showerror("Error!", "Please input valid values")
        return
    
    if not passw:
        messagebox.showerror("Error!", "Please input valid values")
        return
    
    if not usern and passw == "lachee":
        messagebox.showerror("Error!", "Please input valid username credentials")
        return
    
    if not passw == "lachee" and usern:
        messagebox.showerror("Error!", "Please input valid password credentials!" )
        return
                        
    if usern and passw == "lachee":
        chooseOrder.config(state = "normal")
        valueMeal1.config(state = "normal")
        valueMeal2.config(state = "normal")
        valueMeal3.config(state = "normal")
        drinks.config(state = "readonly")
        extraRice.config(state = "normal")
        noExtraRice.config(state = "normal")
        computeButton.config(state = "normal")
        totalbilllabel.config(state = "normal")
        totalBill.config(state = "readonly")
        clearButton.config(state = "normal")

def close():
    if messagebox.askyesno("message", "Are you sure you want to exit?"):
        frame.destroy()

def clear():
    if messagebox.askyesno("message", "Are you sure you want to clear?"):
        valueMeal1.deselect()
        valueMeal2.deselect()
        valueMeal3.deselect()
        drinks.set("")
        rbvar.set(0)
        totalBill.config(state = "normal")
        totalBill.delete(0, END)
        totalBill.config(state = "readonly")
        
def compute():
    try: 
        total = 0
        if var1.get() == 1:
            total += 25.00
        if var2.get() == 1:
            total += 30.00
        if var3.get() == 1:
            total += 35.00
        
        if rbvar.get() == 1:
            total += 25.00
        
        totalBill.config(state = "normal")
        totalBill.delete(0, END)
        totalBill.insert(0, total)
        totalBill.config(state = "readonly")
    except ValueError:
        messagebox.showerror("Error!", "Invalid input!")
        
#GUI
userNameLabel = Label(frame, text = "Username:", bg='pink')
userNameLabel.grid(row = 0, column = 0, sticky = "W")

username = Entry(frame, width = 24)
username.grid(row = 0, column = 0, padx = 65, sticky = "W")

# PASSWORD
passwordLabel = Label(frame, text = "Password:", bg='pink')
passwordLabel.grid(row = 1, column = 0, sticky = "W")

password = Entry(frame, width = 24, show = "*")
password.grid(row = 1, column = 0, padx = 65, sticky = "W")

# ok button
okBUtton = Button(frame, text = "OK", command = ok, bg='pink')
okBUtton.grid(row = 1, column = 0, padx = 214, sticky = "W")

# chose your order
chooseOrder = Label(frame, text = "Choose Your Order", font = "bold, 9", bg='pink')
chooseOrder.grid(row = 2, column = 0, padx = 77, sticky = "W")

#VALUEMEAL

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

valueMeal1 = Checkbutton(frame, text = "Value Meal #1: P25.00", variable = var1, state = "disabled", bg='pink')
valueMeal1.grid(row = 3, column = 0, sticky = "W")

valueMeal2 = Checkbutton(frame, text = "Value Meal #2: P30.00", variable = var2, state = "disabled", bg='pink')
valueMeal2.grid(row = 4, column = 0, sticky = "W")

valueMeal3 = Checkbutton(frame, text = "Value Meal #3: P35.00", variable = var3, state = "disabled", bg='pink')
valueMeal3.grid(row = 5, column = 0, sticky = "W")

#drinks
choices = ["Coke", "Sprite", "Royal"]
drinks = ttk.Combobox(frame, width = 7, values = choices, state = "disabled")
drinks.grid(row = 5, column = 0, padx = 140, sticky = "W")

# rice radiobut
rbvar = IntVar()
extraRice = Radiobutton(frame, text = "Extra Rice", variable = rbvar, value = 1, state = "disabled", bg='pink')
extraRice.grid(row = 6, column = 0, sticky = "W")

noExtraRice = Radiobutton(frame, text = " No Extra Rice", variable = rbvar, value = 2, state = "disabled", bg='pink')
noExtraRice.grid(row = 6, column = 0, padx = 85, sticky = "W")
 
# compute buttpn
computeButton = Button(frame, text = "Compute", state = "disabled", command = compute, bg='pink')
computeButton.grid (row = 6, column = 0, padx = 200)

#total bill 
totalbilllabel = Label(frame, text = "Total Bill is: ", state = "disabled", bg='pink')
totalbilllabel.grid(row = 7, column = 0, sticky = "W")

totalBill = Entry(frame, width = 20, state = "disabled")
totalBill.grid(row = 7, column = 0, padx = 65, sticky = "W")

# buttons
closeButton = Button(frame, text = "Close", width = 5, command = close, bg='pink')
closeButton.grid(row = 8, column=0, padx = 55, sticky = "W")
clearButton = Button(frame, text = "Clear", width = 5, state = "disabled", command=clear, bg='pink')
clearButton.grid(row = 8, column = 0, sticky = "w")

frame.mainloop()