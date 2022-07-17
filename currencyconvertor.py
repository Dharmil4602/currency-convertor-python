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

        # Creating Convert And Clear Buttons. When they are clicked, respective functions are called.

        btnConvertedAmount = Button(window, text="Convert", command=self.ConvertedAmount, font="Helvetica 12 bold", bg="blue", fg="white").grid(row=4, column=2, sticky=E) # Here in self.ConvertedAmount, ConvertedAmount is the function that is called when the Convert button is clicked.

        btnClear = Button(window, text="Clear", command=self.Clear, font="Helvetica 12 bold", bg="red", fg="white").grid(row=4, column=6, padx=25, pady=25,sticky=E) # Here in self.Clear, Clear is the function that is called when the Clear button is clicked.

        window.mainloop() # This is a function that is used to run the application.

        # Functions to do the conversion. Stores input and performs the conversion.

    def ConvertedAmount(self):
        amt = float(self.conversion_rate.get())
        converted_amount = float(self.amount_to_convert.get()) * amt
        self.converted_amount.set(format(converted_amount, '10.2f'))

        # Functions to do the Clear Input.
    def Clear(self):
        self.amount_to_convert.set("")
        self.conversion_rate.set("")
        self.converted_amount.set("")

CurrencyConvertor()
