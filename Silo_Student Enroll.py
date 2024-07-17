import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.geometry("300x270")
frame.title("Student Enroll")
frame.configure(bg='pink')  

def clear():
    studNameEntry.delete(0, END)
    unitsEnrolledEntry.delete(0, END)
    YearLevel.set("")
    labFee.deselect()
    regiCard.deselect()
    catalyst.deselect()
    studentCouncil.deselect()
    studentID.deselect()
    otherMisc.deselect()
    rbvar.set(value=1)
    totalAmountEntry.config(state="normal")
    totalAmountEntry.delete(0, END)
    totalAmountEntry.config(state="readonly")

def compute():
    global scholarship
    if rbvar.get() == 1: 
        scholarship = "Non-scholar"
    elif rbvar.get() == 2: 
        scholarship = "Full Scholar"
    else:
        scholarship = "Partial Scholar"

    year_level = YearLevel.get() 
    YearLevelFee = {"1st Year": 100, "2nd Year": 200, "3rd Year": 300, "4th Year": 400, "5th Year": 50}
    
    stuname = studNameEntry.get()
    if not stuname.isalpha():
        messagebox.showerror("Error!", "Please input alphanumeric characters")
        return
    try:
        units = int(unitsEnrolledEntry.get())
        if units <= 0:
            messagebox.showerror("Error!", "Input must be a positive integer")
            return
    except ValueError:
        messagebox.showerror("Error!", "Please input a positive integer")
        return
    
    if year_level not in YearLevelFee:
        messagebox.showerror("Year Level Error", "Please choose a valid year")
        return
    
    otherFeesTotal = 0
    if vars1.get() == 1:
        otherFeesTotal += 200
    if vars2.get() == 1:
        otherFeesTotal += 50
    if vars3.get() == 1:
        otherFeesTotal += 50
    if vars4.get() == 1:
        otherFeesTotal += 50
    if vars5.get() == 1:
        otherFeesTotal += 50
    if vars6.get() == 1:
        otherFeesTotal += 100    
    
    yearfee = YearLevelFee[year_level]      
    if scholarship == "Non-scholar":
        total = (units * 10) + otherFeesTotal + yearfee
    elif scholarship == "Full Scholar":
        total = 0
    elif scholarship == "Partial Scholar":
        total = ((units * 10) + otherFeesTotal + yearfee) / 2

    totalAmountEntry.config(state="normal")
    totalAmountEntry.delete(0, END)
    totalAmountEntry.insert(0, total)
    totalAmountEntry.config(state="readonly")

# GUI components
        
# Student Name
studName = Label(frame, text="Student Name: ", bg='pink')  # Set header color to pink
studName.grid(row=0, column=0, sticky="W")
studNameEntry = Entry(frame, width=23)
studNameEntry.grid(row=0, column=1, sticky="W")

# Units Enrolled
unitsEnrolled = Label(frame, text="Units Enrolled: ", bg='pink')  # Set header color to pink
unitsEnrolled.grid(row=1, column=0, sticky="W")
unitsEnrolledEntry = Entry(frame, width=23)
unitsEnrolledEntry.grid(row=1, column=1, sticky="W")

# YearLevel
level = ["1st Year", "2nd Year", "3rd Year", "4th Year", "5th Year"]
YearLevelLabel = Label(frame, text="Year Level: ", bg='pink')  # Set header color to pink
YearLevelLabel.grid(row=3, column=0, sticky="W")
YearLevel = ttk.Combobox(frame, values=level)
YearLevel.grid(row=3, column=1, sticky="W")

# Other Fees
otherFees = Label(frame, text="Other Fees: ", bg='pink')  # Set header color to pink
otherFees.grid(row=3, column=0, sticky="W")
vars1 = IntVar()
vars2 = IntVar()
vars3 = IntVar()
vars4 = IntVar()
vars5 = IntVar()
vars6 = IntVar()

labFee = Checkbutton(frame, text="Laboratory Fee", variable=vars1, bg='pink')
labFee.grid(row=4, column=0, sticky="W")

regiCard = Checkbutton(frame, text="Registration Card", variable=vars2, onvalue=1, offvalue=0, bg='pink')
regiCard.grid(row=5, column=0, sticky="W")

catalyst = Checkbutton(frame, text="Catalyst", variable=vars3, onvalue=1, offvalue=0, bg='pink')
catalyst.grid(row=6, column=0, sticky="W")

studentCouncil = Checkbutton(frame, text="Student Council", variable=vars4, onvalue=1, offvalue=0, bg='pink')
studentCouncil.grid(row=4, column=1, sticky="W")

studentID = Checkbutton(frame, text="Student ID", variable=vars5, onvalue=1, offvalue=0, bg='pink')
studentID.grid(row=5, column=1, sticky="W")

otherMisc = Checkbutton(frame, text="Other Miscellaneous", variable=vars6, onvalue=1, offvalue=0, bg='pink')
otherMisc.grid(row=6, column=1, sticky="W")

# Scholarship Grants
scholarGrants = Label(frame, text="Scholarship Grants: ", bg='pink')  # Set header color to pink
scholarGrants.grid(row=7, column=0, sticky="W")

rbvar = IntVar(value=1)
nonScholar = Radiobutton(frame, text="Non-Scholar", variable=rbvar, value=1, bg='pink')
nonScholar.grid(row=7, column=1, sticky="W")
fullScholar = Radiobutton(frame, text="Full Scholar", variable=rbvar, value=2, bg='pink')
fullScholar.grid(row=8, column=1, sticky="W")
partialScholar = Radiobutton(frame, text="Partial Scholar", variable=rbvar, value=3, bg='pink')
partialScholar.grid(row=9, column=1, sticky="W")

# Total Amount
totalAmount = Label(frame, text="Total Amount: ", bg='pink')  # Set header color to pink
totalAmount.grid(row=10, column=0, sticky="W")
totalAmountEntry = Entry(frame, state="readonly")
totalAmountEntry.grid(row=10, column=1, sticky="W")

# Buttons
compute = Button(frame, text="COMPUTE", command=compute, bg='pink')
compute.grid(row=12, column=1, sticky="W")
clear = Button(frame, text="CLEAR", command=clear, bg='pink')
clear.grid(row=12, column=1, padx=75, sticky="W")

frame.mainloop()