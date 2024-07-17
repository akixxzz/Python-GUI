from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.title("Travel and Tours")
frame.geometry("600x300")
frame.configure(bg='pink')  # Set the background color to pink

def clear():
    guestNameEntry.delete(0, END)
    contactNoEntry.delete(0, END)
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    boraPaxEntry.delete(0, END)
    iloPaxEntry.delete(0, END)
    cebuPaxEntry.delete(0, END)
    cebuBoholPaxEntry.delete(0, END)
    ilocosPaxEntry.delete(0, END)
    boraDateEntry.delete(0, END)
    iloDateEntry.delete(0, END)
    cebuBoholDateEntry.delete(0, END)
    cebuDateEntry.delete(0, END)
    ilocosDateEntry.delete(0, END)
    totalAmount.delete(0, END)

def validate_contactnum():
    contactnum = contactNoEntry.get()
    if not contactnum.isdigit():
        messagebox.showerror("Error!", "Please input numeric values")
        return   

def compute():
    contactnum = contactNoEntry.get()
    if not contactnum.isdigit():
        messagebox.showerror("Error!", "Please input numeric values in Contact Number")
        return
    
    total = 0
    try:
        if var1.get() == 1:
            boratotal = 4599 * int(boraPaxEntry.get())
            total += boratotal
        if var2.get() == 1:
            ilototal = 2999 * int(iloPaxEntry.get())
            total += ilototal 
        if var3.get() == 1:
            cebutotal = 1999 * int(cebuPaxEntry.get())   
            total += cebutotal 
        if var4.get() == 1:
            cebuboholtotal = 3599 * int(cebuBoholPaxEntry.get()) 
            total += cebuboholtotal 
        if var5.get() == 1:
            ilocostotal = 2999 * int(ilocosPaxEntry.get())   
            total += ilocostotal 
    except ValueError: 
         messagebox.showerror("Error!", "Please input valid PAX value")
        
    totalAmount.config(state="normal")
    totalAmount.delete(0, END)
    totalAmount.insert(0, total)
    totalAmount.config(state="readonly")
    
# GUI
abcPhTravel = Label(frame, text="ABC PH TRAVEL AND TOURS", font="BOLD, 10", bg='pink')
abcPhTravel.grid(row=0, column=1, sticky="W", padx=2, pady=2)

# GuestName and Contact Number
guestName = Label(frame, text="Guest Name:  ", bg='pink')
guestName.grid(row=1, column=0, sticky="W", padx=2, pady=2)

guestNameEntry = Entry(frame, width=30)
guestNameEntry.grid(row=1, column=1, sticky="W", padx=2, pady=2)

contactNo = Label(frame, text="Contact Number: ", bg='pink')
contactNo.grid(row=2, column=0, sticky="W", padx=2, pady=2)

contactNoEntry = Entry(frame, width=30)
contactNoEntry.grid(row=2, column=1, sticky="W", padx=2, pady=2)

# Tour Packages
tourPackages = Label(frame, text="Tour Packages:", bg='pink')
tourPackages.grid(row=3, column=0, sticky="W", padx=2, pady=2)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

# Boracay
boracay = Checkbutton(frame, text="Boracay Trip", variable=var1, bg='pink')
boracay.grid(row=4, column=0, sticky="W")

lbora = Label(frame, text="PAX", bg='pink')
lbora.grid(row=4, column=1, sticky="W", padx=2, pady=2)

boraPaxEntry = Entry(frame, width=3)
boraPaxEntry.grid(row=4, column=1, sticky="W", padx=40, pady=2)

lboraDate = Label(frame, text="Desired Date: ", bg='pink')
lboraDate.grid(row=4, column=1, sticky="W", padx=70, pady=2)

boraDateEntry = Entry(frame, width=20)
boraDateEntry.grid(row=4, column=1, sticky="W", padx=150, pady=2)

# Iloilo
iloilo = Checkbutton(frame, text="Iloilo Trip", variable=var2, bg='pink')
iloilo.grid(row=5, column=0, sticky="W")

lilo = Label(frame, text="PAX", bg='pink')
lilo.grid(row=5, column=1, sticky="W", padx=2, pady=2)

iloPaxEntry = Entry(frame, width=3)
iloPaxEntry.grid(row=5, column=1, sticky="W", padx=40, pady=2)

liloDate = Label(frame, text="Desired Date: ", bg='pink')
liloDate.grid(row=5, column=1, sticky="W", padx=70, pady=2)

iloDateEntry = Entry(frame, width=20)
iloDateEntry.grid(row=5, column=1, sticky="W", padx=150, pady=2)

# Cebu City
cebu = Checkbutton(frame, text="Cebu City Tour", variable=var3, bg='pink')
cebu.grid(row=6, column=0, sticky="W")

lcebu = Label(frame, text="PAX", bg='pink')
lcebu.grid(row=6, column=1, sticky="W", padx=2, pady=2)

cebuPaxEntry = Entry(frame, width=3)
cebuPaxEntry.grid(row=6, column=1, sticky="W", padx=40, pady=2)

lcebuDate = Label(frame, text="Desired Date: ", bg='pink')
lcebuDate.grid(row=6, column=1, sticky="W", padx=70, pady=2)

cebuDateEntry = Entry(frame, width=20)
cebuDateEntry.grid(row=6, column=1, sticky="W", padx=150, pady=2)

# Cebu City + Bohol Tour
cebuBohol = Checkbutton(frame, text="Cebu City + Bohol Tour", variable=var4, bg='pink')
cebuBohol.grid(row=7, column=0, sticky="W")

lcebuBohol = Label(frame, text="PAX", bg='pink')
lcebuBohol.grid(row=7, column=1, sticky="W", padx=2, pady=2)

cebuBoholPaxEntry = Entry(frame, width=3)
cebuBoholPaxEntry.grid(row=7, column=1, sticky="W", padx=40, pady=2)

lcebuBoholate = Label(frame, text="Desired Date: ", bg='pink')
lcebuBoholate.grid(row=7, column=1, sticky="W", padx=70, pady=2)

cebuBoholDateEntry = Entry(frame, width=20)
cebuBoholDateEntry.grid(row=7, column=1, sticky="W", padx=150, pady=2)

# Ilocos
ilocos = Checkbutton(frame, text="Ilocos Tour", variable=var5, bg='pink')
ilocos.grid(row=8, column=0, sticky="W")

lilocos = Label(frame, text="PAX", bg='pink')
lilocos.grid(row=8, column=1, sticky="W", padx=2, pady=2)

ilocosPaxEntry = Entry(frame, width=3)
ilocosPaxEntry.grid(row=8, column=1, sticky="W", padx=40, pady=2)

lilocosDate = Label(frame, text="Desired Date: ", bg='pink')
lilocosDate.grid(row=8, column=1, sticky="W", padx=70, pady=2)

ilocosDateEntry = Entry(frame, width=20)
ilocosDateEntry.grid(row=8, column=1, sticky="W", padx=150, pady=2)

# Buttons
clearButton = Button(frame, text="CLEAR", width=10, command=clear, bg='pink')
clearButton.grid(row=9, column=0, sticky="W", padx=2, pady=2)

computeButton = Button(frame, text="COMPUTE", command=compute, bg='pink')
computeButton.grid(row=9, column=0, sticky="W", padx=89, pady=2)

# Total amount
LtotalAmount = Label(frame, text="TOTAL AMOUNT", bg='pink')
LtotalAmount.grid(row=9, column=1, sticky="W", padx=2, pady=2)

totalAmount = Entry(frame, width=30, state="readonly")
totalAmount.grid(row=9, column=1, sticky="W", padx=100, pady=2)

frame.mainloop()