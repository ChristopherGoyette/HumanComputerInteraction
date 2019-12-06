from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

cwd = os.path.dirname(os.path.realpath(__file__))

# burger functions
def brgrup():
    global burgerqty
    burgerqty += 1
    burger_qty_lab.set(str(burgerqty))
    calculate_no_change()
def brgrdown():
    global burgerqty
    if burgerqty > 0:
        burgerqty -= 1
        burger_qty_lab.set(str(burgerqty))
        calculate_no_change()
def isCheeseburger():
    global burgerprice
    if(burger_cheese_check_var.get()):
        burgerprice += 0.50
        burger_price_label.set('$' + str(burgerprice) + '0')
        calculate_no_change()
    else:
        burgerprice = 5.00
        burger_price_label.set('$' + str(burgerprice) + '0')
        calculate_no_change()

# pizza functions
def pzaup():
    global pizzaqty
    pizzaqty += 1
    pizza_qty_lab.set(str(pizzaqty))
    calculate_no_change()
def pzadown():
    global pizzaqty
    if pizzaqty > 0:
        pizzaqty -= 1
        pizza_qty_lab.set(str(pizzaqty))
        calculate_no_change()
def pzasm():
    global pizzaprice
    pizzaprice = 10.0
    pizza_price_label.set('$' + str(pizzaprice) + '0')
    calculate_no_change()
def pzamd():
    global pizzaprice
    pizzaprice = 12.0
    pizza_price_label.set('$' + str(pizzaprice) + '0')
    calculate_no_change()
def pzalg():
    global pizzaprice
    pizzaprice = 14.0
    pizza_price_label.set('$' + str(pizzaprice) + '0')
    calculate_no_change()

# fries functions
def friup():
    global friesqty
    friesqty += 1
    fries_qty_lab.set(str(friesqty))
    calculate_no_change()
def fridown():
    global friesqty
    if friesqty > 0:
        friesqty -= 1
        fries_qty_lab.set(str(friesqty))
        calculate_no_change()
def frism():
    global friesprice
    friesprice = 2.0
    fries_price_label.set('$' + str(friesprice) + '0')
    calculate_no_change()
def frimd():
    global friesprice
    friesprice = 3.0
    fries_price_label.set('$' + str(friesprice) + '0')
    calculate_no_change()
def frilg():
    global friesprice
    friesprice = 4.0
    fries_price_label.set('$' + str(friesprice) + '0')
    calculate_no_change()

# fries functions
def drinkup():
    global drinkqty
    drinkqty += 1
    drink_qty_lab.set(str(drinkqty))
    calculate_no_change()
def drinkdown():
    global drinkqty
    if drinkqty > 0:
        drinkqty -= 1
        drink_qty_lab.set(str(drinkqty))
        calculate_no_change()
def drinksm():
    global drinkprice
    drinkprice = 1.0
    drink_price_label.set('$' + str(drinkprice) + '0')
    calculate_no_change()
def drinkmd():
    global drinkprice
    drinkprice = 1.5
    drink_price_label.set('$' + str(drinkprice) + '0')
    calculate_no_change()
def drinklg():
    global drinkprice
    drinkprice = 2.0
    drink_price_label.set('$' + str(drinkprice) + '0')
    calculate_no_change()

def calculate(something):
    global change
    total = (burgerprice * burgerqty) + (pizzaprice * pizzaqty) + (friesprice * friesqty) + (drinkprice * drinkqty)
    m_total_lab_str.set(str("{:.2f}".format(total)))
    tax = total * 0.0625
    m_tax_lab_str.set(str("{:.2f}".format(tax)))
    totalwtax = total + tax
    m_tax_total_lab_str.set(str("{:.2f}".format(totalwtax)))
    change = float(cashtext.get()) - totalwtax
    change_lab_str.set(str("{:.2f}".format(change)))
def calculate_no_change():
    global change
    total = (burgerprice * burgerqty) + (pizzaprice * pizzaqty) + (friesprice * friesqty) + (drinkprice * drinkqty)
    m_total_lab_str.set(str("{:.2f}".format(total)))
    tax = total * 0.0625
    m_tax_lab_str.set(str("{:.2f}".format(tax)))
    totalwtax = total + tax
    m_tax_total_lab_str.set(str("{:.2f}".format(totalwtax)))

def reset():
    global burgerqty, burgerprice, pizzaqty, pizzaprice, friesqty, friesprice, drinkqty, drinkprice, change
    burgerqty = 0
    burgerprice = 5.00
    pizzaqty = 0
    pizzaprice = 10.00
    friesqty = 0
    friesprice = 2.00
    drinkqty = 0
    drinkprice = 1.00
    change = 0

    burger_qty_lab.set(str(burgerqty))
    burger_price_label.set('$' + str(burgerprice) + '0')
    burger_check.deselect()
    pizza_qty_lab.set(str(pizzaqty))
    pizza_price_label.set('$' + str(pizzaprice) + '0')
    pizza_var_str.set(1)
    fries_qty_lab.set(str(friesqty))
    fries_price_label.set('$' + str(friesprice) + '0')
    fries_var_str.set(1)
    drink_qty_lab.set(str(drinkqty))
    drink_price_label.set('$' + str(drinkprice) + '0')
    drink_var_str.set(1)
    m_total_lab_str.set("0")
    m_tax_lab_str.set("0")
    m_tax_total_lab_str.set("0")
    cash_text_var.set('0')
    change_lab_str.set("0")
    
def submit():
    global ordernumberint, change
    calculate(change)
    if (change < 0):
        messagebox.showerror("Error", "Insufficient funds")
        return
    else:
        messagebox.showerror("Change", "Change back: " + str("{:.2f}".format(change)))
    ordernumberint += 1
    ordernum.set(str(ordernumberint))
    reset()



burgerqty = 0
burgerprice = 5.00
pizzaqty = 0
pizzaprice = 10.00
friesqty = 0
friesprice = 2.00
drinkqty = 0
drinkprice = 1.00
ordernumberint = 1
change = 0

################### make the main window
root = Tk()
root.title("Restaurant Management System")

################### order number
ordernumlab = Label(root, text = "Order number: ").grid(row = 0, column = 0, columnspan = 2, sticky = W)
ordernum = StringVar()
ordernum.set(str(ordernumberint))
ordernumaslabel = Label(root, textvariable = ordernum).grid(row = 0, column = 2, sticky = W)

#################### burger
root.grid_rowconfigure(1, minsize = 25) # put a space at the top
root.grid_columnconfigure(0, minsize = 25) # put a space at the top
burgerimg = PhotoImage(file = cwd+"/burger.ppm") # init the img
burgerlabel = Label(root, image = burgerimg, relief = "solid").grid(row = 2, column = 1, columnspan = 3, rowspan = 3)
# up button
upimg = PhotoImage(file = cwd+"/up.ppm") # init the img
upbutton = Button(root, image = upimg, background = "light green", command = brgrup).grid(row = 2, column = 4)
# qty
burger_qty_lab = StringVar()
burger_qty_lab.set("0")
burgerqtylabel = Label(root, textvariable = burger_qty_lab).grid(row = 3, column = 4)
# down button
downimg = PhotoImage(file = cwd+"/down.ppm") # init the img
downbutton = Button(root, image = downimg, background = "red", command = brgrdown).grid(row = 4, column = 4)
# check button
burger_cheese_check_var = IntVar()
burger_check = Checkbutton(root, command = isCheeseburger, variable = burger_cheese_check_var, text = "Cheese")
burger_check.grid(row = 2, column = 0, sticky = "E")
# price
burger_price_label = StringVar()
burger_price_label.set('$' + str(burgerprice) + '0')
burgerpricelabel = Label(root, textvariable = burger_price_label).grid(row = 2, column = 5)

#################### pizza
root.grid_rowconfigure(5, minsize = 25) # put a space at the top
pizzaimg = PhotoImage(file = cwd+"/pizza.ppm") # init the img
pizzalabel = Label(root, image = pizzaimg, relief = "solid").grid(row = 6, column = 1, columnspan = 3, rowspan = 3)
# up button
upimg_pizza = PhotoImage(file = cwd+"/up.ppm") # init the img
upbutton_pizza = Button(root, image = upimg_pizza, background = "light green", command = pzaup).grid(row = 6, column = 4)
# qty
pizza_qty_lab = StringVar()
pizza_qty_lab.set("0")
burgerqtylabel = Label(root, textvariable = pizza_qty_lab).grid(row = 7, column = 4)
# down button
downimg_pizza = PhotoImage(file = cwd+"/down.ppm") # init the img
downbutton_pizza = Button(root, image = downimg_pizza, background = "red", command = pzadown).grid(row = 8, column = 4)
# radio button
pizza_var_str = StringVar()
pizza_var_str.set(1)
pizza_radio1 = Radiobutton(root, text = "small", value = 1, variable = pizza_var_str, command = pzasm).grid(row = 6, column = 0, sticky = "E")
pizza_radio2 = Radiobutton(root, text = "medium", value = 2, variable = pizza_var_str, command = pzamd).grid(row = 7, column = 0, sticky = "E")
pizza_radio3 = Radiobutton(root, text = "large", value = 3, variable = pizza_var_str, command = pzalg).grid(row = 8, column = 0, sticky = "E")
# price
pizza_price_label = StringVar()
pizza_price_label.set('$' + str(pizzaprice) + '0')
pizzapricelabel = Label(root, textvariable = pizza_price_label).grid(row = 7, column = 5)

#################### fries
root.grid_rowconfigure(9, minsize = 25) # put a space at the top
friesimg = PhotoImage(file = cwd+"/fries.ppm") # init the img
frieslabel = Label(root, image = friesimg, relief = "solid").grid(row = 10, column = 1, columnspan = 3, rowspan = 3)
# up button
upimg_fries = PhotoImage(file = cwd+"/up.ppm") # init the img
upbutton_fries = Button(root, image = upimg_fries, background = "light green", command = friup).grid(row = 10, column = 4)
# qty
fries_qty_lab = StringVar()
fries_qty_lab.set("0")
friesqtylabel = Label(root, textvariable = fries_qty_lab).grid(row = 11, column = 4)
# down button
downimg_fries = PhotoImage(file = cwd+"/down.ppm") # init the img
downbutton_fries = Button(root, image = downimg_fries, background = "red", command = fridown).grid(row = 12, column = 4)
# radio button
fries_var_str = StringVar()
fries_var_str.set(1)
fries_radio1 = Radiobutton(root, text = "small", value = 1, variable = fries_var_str, command = frism).grid(row = 10, column = 0, sticky = "E")
fries_radio2 = Radiobutton(root, text = "medium", value = 2, variable = fries_var_str, command = frimd).grid(row = 11, column = 0, sticky = "E")
fries_radio3 = Radiobutton(root, text = "large", value = 3, variable = fries_var_str, command = frilg).grid(row = 12, column = 0, sticky = "E")
# price
fries_price_label = StringVar()
fries_price_label.set('$' + str(friesprice) + '0')
friespricelabel = Label(root, textvariable = fries_price_label).grid(row = 10, column = 5)

#################### drink
root.grid_rowconfigure(13, minsize = 25)
drinkimg = PhotoImage(file = cwd+"/soda.ppm")
drinklabel = Label(root, image = drinkimg, relief = "solid").grid(row = 14, column = 1, columnspan = 3, rowspan = 3)
# up button
upimg_drink = PhotoImage(file = cwd+"/up.ppm")
upbutton_drink = Button(root, image = upimg_drink, background = "light green", command = drinkup).grid(row = 14, column = 4)
# qty
drink_qty_lab = StringVar()
drink_qty_lab.set("0")
drinkqtylabel = Label(root, textvariable = drink_qty_lab).grid(row = 15, column = 4)
# down button
downimg_drink = PhotoImage(file = cwd+"/down.ppm")
downbutton_drink = Button(root, image = downimg_drink, background = "red", command = drinkdown).grid(row = 16, column = 4)
# radio button
drink_var_str = StringVar()
drink_var_str.set(1)
drink_radio1 = Radiobutton(root, text = "small", value = 1, variable = drink_var_str, command = drinksm).grid(row = 14, column = 0, sticky = "E")
drink_radio2 = Radiobutton(root, text = "medium", value = 2, variable = drink_var_str, command = drinkmd).grid(row = 15, column = 0, sticky = "E")
drink_radio3 = Radiobutton(root, text = "large", value = 3, variable = drink_var_str, command = drinklg).grid(row = 16, column = 0, sticky = "E")
# price
drink_price_label = StringVar()
drink_price_label.set('$' + str(drinkprice) + '0')
drinkpricelabel = Label(root, textvariable = drink_price_label).grid(row = 14, column = 5)
root.grid_rowconfigure(17, minsize = 25) # put a space at the bottom

# prices
ttk.Separator(root, orient = "vertical").grid(row = 0, column = 6, rowspan = 18, sticky='ns')
root.grid_columnconfigure(6, minsize = 25)
root.grid_columnconfigure(8, minsize = 10)
root.grid_columnconfigure(10, minsize = 25)
#   total
totallabel = Label(root, text = "Total: ").grid(row = 2, column = 7, sticky = W)
m_total_lab_str = StringVar()
m_total_lab_str.set("0")
mtotallabstr = Label(root, textvariable = m_total_lab_str).grid(row = 2, column = 9)
#   tax
taxlabel = Label(root, text = "Tax: ").grid(row = 3, column = 7, sticky = W)
m_tax_lab_str = StringVar()
m_tax_lab_str.set("0")
mtaxlabstr = Label(root, textvariable = m_tax_lab_str).grid(row = 3, column = 9)
#   total with tax
totalwithtaxlabel = Label(root, text = "Total with tax: ", font = "Helvetica 12 bold").grid(row = 4, column = 7, sticky = W)
m_tax_total_lab_str = StringVar()
m_tax_total_lab_str.set("0")
mtaxtotallabstr = Label(root, textvariable = m_tax_total_lab_str, font = "Helvetica 12 bold").grid(row = 4, column = 9)
#   cash
cashlabel = Label(root, text = "Cash: ").grid(row = 6, column = 7, sticky = W)
cash_text_var = StringVar()
cash_text_var.set('0')
cashtext = Entry(root, textvariable = cash_text_var, width = 10, justify = "center")
cashtext.grid(row = 6, column = 9)
root.bind('<Return>', calculate)
# change
changelabel = Label(root, text = "Change: ").grid(row = 7, column = 7, sticky = W)
change_lab_str = StringVar()
change_lab_str.set("0")
changelabstr = Label(root, textvariable = change_lab_str).grid(row = 7, column = 9)

# submit and reset buttons
submitbutton = Button(root, text = "Submit", background = "light green", command = submit).grid(row = 17, column = 9, rowspan = 3)
resetbutton = Button(root, text = "Reset", background = "red", command = reset).grid(row = 17, column = 13, rowspan = 3)


# do stuff ???
root.mainloop()