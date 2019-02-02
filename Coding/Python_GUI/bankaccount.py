import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import scrolledtext, messagebox



class Account(tk.Tk):

    def __init__(self, master, balance, irate):
        tk.Tk.__init__(self)

        # initializing input variables
        self.balance = balance
        self.irate = irate

        # variable for holding the Transaction List
        self.transaction_list = []
        # Creating Frame for our Window
        self.frame_top = tk.Frame(master)
        # Packing the Frame in a grid geometry manager
        self.frame_top.grid()


        # FirstLabel : App Name
        lab3 = tk.Label(self.frame_top, text="FedUni Banking")
        # Using grid geometry manager to adjust the app name in its place
        lab3.grid(row=0, columnspan=5, ipady=20)
        # Using the config command to set the Font and FontSize of the app name
        lab3.config(font=("Arial", 32))

        # SecondLabel : Account Number
        lab4 = tk.Label(self.frame_top, text="Account Number")
        # Using grid geometry manager to adjust the app name in its place
        lab4.grid(row=1, column=0, ipadx=25, ipady=10)
        # Using the config command to set the Font and FontSize of the app name
        lab4.config(font=("Arial", 7), anchor='w')

        # ThirdLabel : Balance
        lab5 = tk.Label(self.frame_top, text="Balance")
        # Using grid geometry manager to adjust the app name in its place
        lab5.grid(row=1, column=1, ipadx=25, ipady=10)
        # Using the config command to set the Font and FontSize of the app name
        lab5.config(font=("Arial", 7), anchor='w')

        # LogOut Button
        tk.Button(self.frame_top, text="LogOut") \
            .grid(row=1, column=2, sticky='news', ipadx=51, ipady=10)

        # FourthLabel : Amount($)
        lab6 = tk.Label(self.frame_top, text="Amount($)")
        # Using grid geometry manager to adjust the app name in its place
        lab6.grid(row=2, column=0, ipadx=30, ipady=10)
        # Using the config command to set the Font and FontSize of the app name
        lab6.config(font=("Arial", 10))

        # Entry_Widget_1 : Accepts a numeric Input
        self.amount = tk.Entry(self.frame_top)
        self.amount.grid(row=2, column=1, sticky='news')
        self.amount.config(font=('Arial', 10))
        # Setting the Focus to the Account Input Automatically
        self.amount.focus_set()

        # Creating a Frame for Row 2 column 3 to hold two buttons in a single column
        self.frame_rc = tk.Frame(self.frame_top)

        # Deposit Button
        dp = tk.Button(self.frame_rc, text="Deposit", command=lambda:self.deposit())
        dp.grid(row=0, column=0, ipadx=15, ipady=8)

        # Withdraw Button
        wd = tk.Button(self.frame_rc, text="Withdraw", command=lambda:self.withdraw())
        wd.grid(row=0, column=1, ipadx=15, ipady=8)

        # Packing the Frame in a grid geometry manager
        self.frame_rc.grid(row=2, column=2, sticky="nsew")


        # Text Widget
            # txt = tk.Text(master, width=48, height=10, wrap='word')
            # txt.grid(row=3, column=0)
            # # Creating ScrollBar for The TextWidget
            # scrl = tk.Scrollbar(master, orient= VERTICAL, command = txt.yview)
            # scrl.grid(row=3, column=1, sticky = 'ns')
            # txt.config(yscrollcommand = scrl.set)
        txt = scrolledtext.ScrolledText(master, width=18, height=10)
        txt.grid(row=3, sticky='news')


        # Drawing the Graph
        f = Figure(figsize = (4, 5), dpi=60)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5],[5,6,1,3,8])

        canvas = FigureCanvasTkAgg(f, master=master)
        canvas.draw()
        canvas.get_tk_widget().grid(row=4, sticky='nsew')

    def deposit(self):
        amt = self.amount.get()
        # For Removing the unwanted WhiteSpaces from the Entry Widget
        amt = list(amt.split())
        amt = str(''.join(amt))
        self.transaction_list.append(("Deposit", int(amt)))
        print(self.transaction_list)

    def withdraw(self):
        amt = self.amount.get()
        # For Removing the unwanted WhiteSpaces from the Entry Widget
        amt = list(amt.split())
        amt = str(''.join(amt))
        if int(amt) > self.balance :
            messagebox.showinfo('Overdraft Error', 'Demanded Amount more than current Balance')
        else:
            self.transaction_list.append(("Withdraw", int(amt)))
        print(self.transaction_list)


def main():
    # Creating our Tkinter Window
    root = tk.Tk()
    root.geometry('440x640')
    root.title("FedUni Banking")
    root.resizable(False, False)
    # Passing Balance and interest rate for the User
    bal = 10000
    rate = 33
    Account(root, bal, rate)
    root.mainloop()


if __name__ == '__main__':
    main()