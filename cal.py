from tkinter import *

class Calculator:
    def __init__(self, master):
        # Lazy global variable

        self.master = master
        master.title("Calculator")
        self.equationComplete=False
        self.S = StringVar(master=self.master)
        self.e = Entry(master, textvariable=self.S, width="30")
        self.e.grid(columnspan=4,row=0)

        self.clear = Button(master, text="C",  command = self.clear, fg="blue4", bg ="gray80", width="5")
        self.clear.grid(column=1,row=4)

        self.equal = Button(master, text="=",  command = self.equal, fg="blue4", bg ="gray80", width="5")
        self.equal.grid(column=3,row=4)

        self.divide = Button(master, text="/",  command=lambda: self.press('/'), fg="blue4", bg ="gray80", width="5")
        self.divide.grid(column=0,row=3)

        self.multiply = Button(master, text="x",  command=lambda: self.press('*'), fg="blue4", bg ="gray80", width="5")
        self.multiply.grid(column=0,row=4)
        
        self.add = Button(master, text="+",  command=lambda: self.press('+'), fg="blue4", bg ="gray80", width="5")
        self.add.grid(column=0,row=2)

        self.subtract = Button(master, text="-", command=lambda: self.press('-'), fg="blue4", bg ="gray80", width="5")
        self.subtract.grid(column=0,row=1)

        
        self.zero = Button(master, text="0", command=lambda: self.press("0"), fg="blue4", bg ="gray80", width="5")
        self.one = Button(master, text="1", command=lambda: self.press("1"), fg="blue4", bg ="gray80", width="5")
        self.two = Button(master, text="2", command=lambda: self.press("2"), fg="blue4", bg ="gray80", width="5")
        self.three = Button(master, text="3", command=lambda: self.press("3"), fg="blue4", bg ="gray80", width="5")
        self.four = Button(master, text="4", command=lambda: self.press("4"), fg="blue4", bg ="gray80", width="5")
        self.five = Button(master, text="5", command=lambda: self.press("5"), fg="blue4", bg ="gray80", width="5")
        self.six = Button(master, text="6", command=lambda: self.press("6"), fg="blue4", bg ="gray80", width="5")
        self.seven = Button(master, text="7", command=lambda: self.press("7"), fg="blue4", bg ="gray80", width="5")
        self.eight = Button(master, text="8", command=lambda: self.press("8"), fg="blue4", bg ="gray80", width="5")
        self.nine = Button(master, text="9", command=lambda: self.press("9"), fg="blue4", bg ="gray80", width="5")

        self.zero.grid(column=2,row=4)
        self.one.grid(column=1,row=3)
        self.two.grid(column=2,row=3)
        self.three.grid(column=3,row=3)
        self.four.grid(column=1,row=2)
        self.five.grid(column=2,row=2)
        self.six.grid(column=3,row=2)
        self.seven.grid(column=1,row=1)
        self.eight.grid(column=2,row=1)
        self.nine.grid(column=3,row=1)


    def press(self,symbol):
        if (self.equationComplete):
            prior=self.S.get()
            self.S.set(symbol)
            self.equationComplete=FALSE
        else:
            prior=self.S.get()
            self.S.set(prior+symbol)


    def equal(self):
        try:
            ans=eval(self.S.get())
            self.S.set(str(ans)+"="+self.S.get())
            self.equationComplete=True
        except:
            self.S.set("ERROR")
            self.equationComplete=True
            
        
    
    def clear(self):
        self.S.set("")
        self.equationComplete=False



root = Tk()
my_gui = Calculator(root)
root.mainloop()