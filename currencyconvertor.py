# Tkinter widget provides various controls for eg:
# buttons, labels, text boxes, etc. for our GUI Applications.
# Tkinter is a Python module for creating GUI applications.

from tkinter import *
class CurrencyConvertor: # Creat Class
    def __init__(self): #Here self is a variable which represents the instance of the object itself. __init__ special method in python which is to be declared in the class constructor.

        window = Tk() # Creates Application Window
        window.title("Currency Convertor")
        window.configure(bg="yellow")
        Label(window, font="Helvetica 12 bold",bg="yellow", text="Amount To Convert").grid(row=1, column=1, sticky=W) # Here sticky=W means that the window is sticky in the West(W)

        Label(window, font="Helvetica 12 bold",bg="yellow", text="Conversion Rate").grid(row=2, column=1, sticky=W) # Here sticky=W means that the window is sticky in the West(W)

        Label(window, font="Helvetica 12 bold",bg="yellow", text="Converted Amount").grid(row=3, column=1, sticky=W) # Here sticky=W means that the window is sticky in the West(W)

        # Create Objects And Add Entry Functions
        self.amount_to_convert = StringVar() # StringVar is class from Tkinter which is used to monitor changes to string variables.
        Entry(window, textvariable=self.amount_to_convert, justify= RIGHT).grid(row=1, column=2) # Entry() funtion/method is used to create a text entry field, which is used to take input from the user.

        self.conversion_rate = StringVar()
        Entry(window, textvariable=self.conversion_rate, justify= RIGHT).grid(row=2, column=2)

        self.converted_amount = StringVar()
        lblConvertAmount = Label(window, textvariable=self.converted_amount, font="Helvetica 12 bold",bg="yellow").grid(row=3, column=2, sticky=E)