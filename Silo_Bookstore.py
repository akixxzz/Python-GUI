
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.title("Book Store")
frame.config(bg="pink")
frame.geometry("800x200")


def clear():
    eDayEng.deselect()
    intMath.deselect()
    wonSci.deselect()
    EElvl.set(" ")
    IMlvl.set(" ")
    WSlvl.set(" ")
    EEquantity.delete(0, END)
    IMquantity.delete(0, END)
    WSquantity.delete(0, END)
    lvl1.set("")
    ttl1.set("")
    lvl2.set("")
    ttl2.set("")
    lvl3.set("")
    ttl3.set("")
    ttlAmt.set("")
    EElvl.config(state = DISABLED)
    IMlvl.config(state = DISABLED)
    WSlvl.config(state = DISABLED)
    EEquantity.config(state = DISABLED)
    IMquantity.config(state = DISABLED)
    WSquantity.config(state = DISABLED)


def updateBtn():
    if vars1.get() == 1:
        EElvl.config(state="readonly")
        EEquantity.config(state="normal")
    else:
        EElvl.config(state="disabled")
        EElvl.set(" ")
        lvl1.set("")
        ttl1.set("")
        EEquantity.delete(0, END)
        EEquantity.config(state="disabled")

    if vars2.get() == 1:
        IMlvl.config(state="readonly")
        IMquantity.config(state="normal")
    else:
        IMlvl.config(state="disabled")
        IMlvl.set(" ")
        lvl2.set("")
        ttl2.set("")
        IMquantity.delete(0, END)
        IMquantity.config(state="disabled")

    if vars3.get() == 1:
        WSlvl.config(state="readonly")
        WSquantity.config(state="normal")
    else:
        WSlvl.config(state="disabled")
        WSlvl.set(" ")
        lvl3.set("")
        ttl3.set("")
        WSquantity.delete(0, END)
        WSquantity.config(state="disabled")


def unitPriceUpdate(event):
    if EElvl.get() == 'NURSERY':
        lvl1.set("150.00")
    if EElvl.get() == 'KINDER':
        lvl1.set("200.00")
    if EElvl.get() == 'PREP':
        lvl1.set("250.00")

    if IMlvl.get() == 'NURSERY':
        lvl2.set("150.00")
    if IMlvl.get() == 'KINDER':
        lvl2.set("200.00")
    if IMlvl.get() == 'PREP':
        lvl2.set("250.00")

    if WSlvl.get() == 'NURSERY':
        lvl3.set("150.00")
    if WSlvl.get() == 'KINDER':
        lvl3.set("200.00")
    if WSlvl.get() == 'PREP':
        lvl3.set("250.00")


def compute():
    try:
        subj1 = int(EEquantity.get() or 0) * float(EEunitPrice.get() or 0)
        subj2 = int(IMquantity.get() or 0) * float(IMunitPrice.get() or 0)
        subj3 = int(WSquantity.get() or 0) * float(WSunitPrice.get() or 0)

        if vars1.get() == 1 and EEquantity.get() == "":
            messagebox.showerror("Error!", "Please input valid quantity for Everyday English")
        elif vars2.get() == 1 and IMquantity.get() == "":
            messagebox.showerror("Error!", "Please input valid quantity for Integrated Mathematics")
        elif vars3.get() == 1 and WSquantity.get() == "":
            messagebox.showerror("Error!", "Please input valid quantity for Wonders of Science")
        else:
            ttl1.set(f"{subj1:.2f}" if subj1 else "")
            ttl2.set(f"{subj2:.2f}" if subj2 else "")
            ttl3.set(f"{subj3:.2f}" if subj3 else "")

            totalAmount = subj1 + subj2 + subj3
            ttlAmt.set(f"{totalAmount:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid values for book quantities.")


bookStore = Label(frame, text="MJN Book Store", bg="pink", font = "bold, 12",)
bookStore.grid(row=0, column=3, sticky="n")

# Book title

bookTitle = Label(frame, text="Book Title", bg="pink")
bookTitle.grid(row=1, column=0, sticky="W")

vars1 = IntVar()
eDayEng = Checkbutton(frame, text="Everyday English", variable=vars1, onvalue=1, offvalue=0, command=updateBtn, bg="pink")
eDayEng.grid(row=2, column=0, sticky="W")

vars2 = IntVar()
intMath = Checkbutton(frame, text="Integrated Mathematics", variable=vars2, onvalue=1, offvalue=0, command=updateBtn, bg="pink")
intMath.grid(row=3, column=0, sticky="W")

vars3 = IntVar()
wonSci = Checkbutton(frame, text="Wonders of Science", variable=vars3, onvalue=1, offvalue=0, command=updateBtn, bg="pink")
wonSci.grid(row=4, column=0, sticky="W")

# Level

Level = Label(frame, text="Level", bg="pink")
Level.grid(row=1, column=2, sticky="W")

choices = ["NURSERY", "KINDER", "PREP"]
EElvl = ttk.Combobox(frame, values=choices, state=DISABLED)
EElvl.grid(row=2, column=2, sticky="W")
EElvl.bind("<<ComboboxSelected>>", unitPriceUpdate)

IMlvl = ttk.Combobox(frame, values=choices, state=DISABLED)
IMlvl.grid(row=3, column=2, sticky="W")
IMlvl.bind("<<ComboboxSelected>>", unitPriceUpdate)

WSlvl = ttk.Combobox(frame, values=choices, state=DISABLED)
WSlvl.grid(row=4, column=2, sticky="W")
WSlvl.bind("<<ComboboxSelected>>", unitPriceUpdate)

# unit price
lvl1 = StringVar()
lvl2 = StringVar()
lvl3 = StringVar()
unitPrice = Label(frame, text="Unit Price", bg="pink")
unitPrice.grid(row=1, column=3, sticky="W")

EEunitPrice = Entry(frame, state="readonly", textvariable=lvl1, bg="pink")
EEunitPrice.grid(row=2, column=3, sticky="W")

IMunitPrice = Entry(frame, state="readonly", textvariable=lvl2, bg="pink")
IMunitPrice.grid(row=3, column=3, sticky="W")

WSunitPrice = Entry(frame, state="readonly", textvariable=lvl3, bg="pink")
WSunitPrice.grid(row=4, column=3, sticky="W")

# quantity
quan1 = StringVar()
quan2 = StringVar()
quan3 = StringVar()

quantity = Label(frame, text="Quantity", bg="pink")
quantity.grid(row=1, column=4, sticky="W")

EEquantity = Entry(frame, state=DISABLED, textvariable=quan1)
EEquantity.grid(row=2, column=4, sticky="W")

IMquantity = Entry(frame, state=DISABLED, textvariable=quan2)
IMquantity.grid(row=3, column=4, sticky="W")

WSquantity = Entry(frame, state=DISABLED, textvariable=quan3)
WSquantity.grid(row=4, column=4, sticky="W")

# subtotal

ttl1 = StringVar()
ttl2 = StringVar()
ttl3 = StringVar()

subTotal = Label(frame, text="Sub-total", bg="pink")
subTotal.grid(row=1, column=5, sticky="W")

EEsubTotal = Entry(frame, state="readonly", textvariable=ttl1, bg="pink")
EEsubTotal.grid(row=2, column=5, sticky="W")

IMsubTotal = Entry(frame, state="readonly", textvariable=ttl2, bg="pink")
IMsubTotal.grid(row=3, column=5, sticky="W")

WSsubTotal = Entry(frame, state="readonly", textvariable=ttl3, bg="pink")
WSsubTotal.grid(row=4, column=5, sticky="W")

# Button

computeBtn = Button(frame, text="COMPUTE", command=compute, bg="pink")
computeBtn.grid(row=5, column=1)

clearBtn = Button(frame, text="CLEAR", command=clear, bg="pink")
clearBtn.grid(row=5, column=2)

# Total Amount
totalAmount = Label(frame, text="Total Amount:", bg="pink")
totalAmount.grid(row=5, column=4)

ttlAmt = StringVar()
EtotalAmount = Entry(frame, state="readonly", textvariable=ttlAmt, bg="pink")
EtotalAmount.grid(row=5, column=5)

frame.mainloop()