# Importing Matplotlib modules
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Importing whole tkinter package
import tkinter as tk
from tkinter import messagebox, scrolledtext
from random import randint

# Creating global lists to hold the account number and pin number entered by the user
acc = []
pin = []


def generate_user():
    account_num = randint(100000, 800000)
    pin_num = randint(1000, 8000)
    r_bal = randint(5000, 100000)
    r_ir = randint(1, 6)
    return account_num, pin_num, r_bal, r_ir

# Class that holds all the Details of the user and Various Methods(Functions) for Ex:(deposit, withdraw,
# get_transition_string())
class BankAccount:

    # Constructor for the Class
    def __init__(self, master):

        self.master = master

        # Creating a Variable that converts anything into String
        self.acc_input = tk.StringVar()
        self.pin_input = tk.StringVar()

        # Creating Frame for our Window
        self.frame_top = tk.Frame(master)
        # Packing the Frame in a grid geometry manager
        self.frame_top.grid()
        
        
        # FirstLabel : App Name
        lab1 = tk.Label(self.frame_top, text="FedUni Banking")
        # Using grid geometry manager to adjust the app name in its place
        lab1.grid(row=0, columnspan=3, ipadx=40, ipady=40)
        # Using the config command to set the Font and FontSize of the app name
        lab1.config(font=("Arial", 32))
        
        # SecondLabel : Account Number / PIN
        lab2 = tk.Label(self.frame_top, text="Account Number / PIN")
        # Using grid geometry manager to adjust the app name in its place
        lab2.grid(row=2, column=0, sticky='news', padx=13, pady=30)
        # Using the config command to set the Font and FontSize of the app name
        lab2.configure(font=("Arial", 9, 'bold'))

        # Entry_Widget_1 : Displays AccountId and simultaneously using grid geometry manager
        self.account_id = tk.Entry(self.frame_top, textvariable = self.acc_input)
        self.account_id.grid(row=2, column=1, sticky='news')
        self.account_id.config(font=('Arial', 10))
        # # Setting the Focus to the Account Input Automatically
        # self.account_id.focus_set()

        # Entry_Widget_2 : Displays PinNumber and simultaneously using grid geometry manager
        self.pin_number = tk.Entry(self.frame_top, textvariable = self.pin_input)
        self.pin_number.grid(row=2, column=2, sticky='news')
        self.pin_number.config(show = '*', font=('Arial', 10))

        #######  INPUT BUTTONS #######
        tk.Button(self.frame_top, text="1", command = lambda:self.check(1))\
            .grid(row=3, column=0, sticky='news', ipadx=40, ipady=40)
        tk.Button(self.frame_top, text="2", command = lambda:self.check(2))\
            .grid(row=3, column=1, sticky='news')
        tk.Button(self.frame_top, text="3", command = lambda:self.check(3))\
            .grid(row=3, column=2, sticky='news')
        tk.Button(self.frame_top, text="4", command = lambda:self.check(4))\
            .grid(row=4, column=0, sticky='news', ipadx=40, ipady=40)
        tk.Button(self.frame_top, text="5", command = lambda:self.check(5))\
            .grid(row=4, column=1, sticky='news')
        tk.Button(self.frame_top, text="6", command = lambda:self.check(6))\
            .grid(row=4, column=2, sticky='news')
        tk.Button(self.frame_top, text="7", command = lambda:self.check(7))\
            .grid(row=5, column=0, sticky='news', ipadx=40, ipady=40)
        tk.Button(self.frame_top, text="8", command = lambda:self.check(8))\
            .grid(row=5, column=1, sticky='news')
        tk.Button(self.frame_top, text="9", command = lambda:self.check(9))\
            .grid(row=5, column=2, sticky='news')
        tk.Button(self.frame_top, text="Cancel / Clear", bg="red", fg="black", command = lambda:self.clear())\
            .grid(row=6, column=0, sticky='news')
        tk.Button(self.frame_top, text="0", command = lambda:self.check(0))\
            .grid(row=6, column=1, sticky='news', ipadx=40, ipady=40)
        tk.Button(self.frame_top, text="Log In", bg="green", fg="black", command = lambda:self.signin())\
            .grid(row=6, column=2, sticky='news')

        # Asking whether to Create New User or not
        if messagebox.askyesno("Register", "Want to Create new User??"):
            an, pn, r_b, r_p = generate_user()
            with open(str(an) + ".txt", 'w') as f:
                f.write(str(an))
                f.write('\n')
                f.write(str(pn))
                f.write('\n')
                f.write(str(r_b))
                f.write('\n')
                f.write(str(r_p))
            self.acc_input.set(str(an))
            self.pin_input.set(str(pn))


    def check(self, num):
        e1 = str(self.account_id.focus_get())
        e2 = str(self.pin_number.focus_get())
        # Checking Which of the Inputs is Focused and Printing the Key Strokes to it
        if e1 == '.!frame.!entry':
            acc.append(str(num))
            self.acc_input.set(acc)
        elif e2 == '.!frame.!entry2':
            pin.append(str(num))
            self.pin_input.set(pin)

    def clear(self):
        e1 = str(self.account_id.focus_get())
        e2 = str(self.pin_number.focus_get())
        # print("ACC :", e1)
        # print("PIN :", e2)
        if e1 == '.!frame.!entry' and acc != []:
            acc.pop()
            self.acc_input.set(acc)
        elif e2 == '.!frame.!entry2' and pin != []:
            pin.pop()
            self.pin_input.set(pin)

    def signin(self):
        # Storing the Entries in variables
        ee = (self.account_id.get())
        ff = (self.pin_number.get())

        # For Removing the unwanted WhiteSpaces from the Entry Widget
        ee = list(ee.split())
        ff = list(ff.split())
        ee = ''.join(ee)
        ff = ''.join(ff)
        print("Your Account id :",ee)
        print("Your Pin No. :",ff)

        # Temporary variable to hold the file contents
        temp = []
        # Trying to open a file names acc_id.txt
        try:
            with open(ee + ".txt", "r") as f:
                l = []
                for line in f:
                    if '\n' in line:
                        l = list(line)
                        l.pop()
                        l = ''.join(l)
                    else:
                        l = line
                    temp.append(l)
            accnt_id = temp[0]
            p_num = temp[1]
            bl = temp[2]
            ir = temp[3]
            t1 = []
            for i in range(4, len(temp)):
                t1.append(temp[i].split())

            # print("Temp List :",temp)
            # print("Transactions_List",t1)
            # Checking if the Pin Matches
            if p_num == ff:
                # If Pin Matches
                print("Success!")
                # Withdrawing the current Window
                self.master.withdraw()
                # Calling the Account Class
                self.newWindow = tk.Toplevel(self.master)
                bb = Account(self.newWindow, accnt_id, p_num, bl, ir, t1)
            else:
                # if Credentials doesn't match
                print("Failed!")
                # Displaying the Error message using Tkinter's MessageBox
                messagebox.showinfo('Login Error', 'Invalid Credentials')
                global acc, pin
                acc = []
                pin = []
                self.acc_input.set(acc)
                self.pin_input.set(pin)
        except IOError:
            messagebox.showinfo("Login Error!!", "Invalid account id!! Try Again")
            acc = []
            pin = []
            self.acc_input.set(acc)
            self.pin_input.set(pin)


class Account(tk.Tk):

    def __init__(self, master, accnt_id, p_num, bl, ir, tl):
        tk.Tk.__init__(self)

        # Initializing the Input Variables
        self.master = master
        self.accnt_id = accnt_id
        self.p_num = p_num
        self.bl = bl
        self.ir = ir
        self.tl = tl

        # variable to store the length of the Transaction_List
        self.lp = len(self.tl)

        # variable for holding the Transaction List
        # self.transaction_list = []
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
        # Showing the Current Account Number
        an = "Account Number :" + self.accnt_id
        lab4 = tk.Label(self.frame_top, text=an)
        # Using grid geometry manager to adjust the app name in its place
        lab4.grid(row=1, column=0, ipadx=20, ipady=10)
        # Using the config command to set the Font and FontSize of the app name
        lab4.config(font=("Arial", 10), anchor='w')

        # ThirdLabel : Balance
        # Showing the retrieved Balance
        ba = "Balance :" + str(self.bl)
        lab5 = tk.Label(self.frame_top, text=ba)
        # Using grid geometry manager to adjust the app name in its place
        lab5.grid(row=1, column=1, ipadx=20, ipady=10)
        # Using the config command to set the Font and FontSize of the app name
        lab5.config(font=("Arial", 10), anchor='w')

        # LogOut Button
        tk.Button(self.frame_top, text="LogOut", command = lambda:self.logout()) \
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
        # self.amount.focus_set()

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


        # Frame for Text Widget
        # self.frame_tw = tk.Frame(self.master)
        # self.frame_tw.grid(row=3, sticky='news')
        # TextWidget

        # scrollbar = tk.Scrollbar(self.frame_top, orient="vertical")
        # scrollbar.grid(row=3, column=2, sticky='news')

        txt = tk.scrolledtext.ScrolledText(master, width=18, height=10)
        for item in self.tl:
            for i in item:
                txt.insert('insert', i+'\n')
        # txt = tk.Listbox(self.frame_top, width=48, height=10)
        # txt.config(yscrollcommand=scrollbar.set)
        txt.grid(row=3, columnspan=2, sticky='news')
        # scrollbar.config(command=txt.yview)


        # Preparing Data for Plotting the Graph
        c = 1 + float(self.ir)/1200
        x = []
        y = [x for x in range(2, 14)]
        for i in range(12):
            bal = float(self.bl)
            bal *= c
            self.bl = bal
            x.append(bal)
        # print(x)

        # Drawing the Graph
        f = Figure(figsize = (3, 4), dpi=80)
        a = f.add_subplot(111)
        a.set_title("Cumulative Interest 12 Months", fontsize=18)
        a.plot(y, x, marker='o', markerfacecolor='blue')

        canvas = FigureCanvasTkAgg(f, master=master)
        canvas.get_tk_widget().grid(row=4, sticky='nsew')
        canvas.draw()

    def deposit(self):
        amt = self.amount.get()
        # For Removing the unwanted WhiteSpaces from the Entry Widget
        amt = list(amt.split())
        amt = str(''.join(amt))
        self.tl.append(("Deposit", int(amt)))
        self.bl += int(amt)
        print(self.tl)
        # print(self.bal)

    def withdraw(self):
        amt = self.amount.get()
        # For Removing the unwanted WhiteSpaces from the Entry Widget
        amt = list(amt.split())
        amt = str(''.join(amt))
        if int(amt) > self.bl :
            messagebox.showinfo('Overdraft Error', 'Demanded Amount more than current Balance')
        else:
            self.tl.append(("Withdraw", int(amt)))
            self.bl -= int(amt)
        print(self.tl)

    def logout(self):
        # Checking if User has Made any transactions or not before updating the File
        if len(self.tl) > self.lp:
            # Updating the File
            with open(self.accnt_id + ".txt", 'w') as f:
                f.write(self.accnt_id + '\n')
                f.write(self.p_num + '\n')
                f.write(str(self.bl) + '\n')
                f.write(self.ir)
                for item in self.tl:
                    for j in item:
                        f.write("\n"+str(j))
        # Clearing the Transaction_List
        self.tl = []
        root.destroy()
        main()





def main():
    # Creating our Tkinter Window
    global root
    root = tk.Tk()
    root.title("FedUni Banking")
    root.geometry('440x640')
    root.minsize(440, 640)
    root.maxsize(440, 640)
    root.resizable(False, False)
    bank = BankAccount(root)
    root.mainloop()



if __name__ == '__main__':
    main()