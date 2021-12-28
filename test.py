from tkinter import * 

root = Tk()
root.title("Daniel's Casino")
root.geometry('350x200')

Starting_money = Label(root, text= "how much money do you want to enter with? :")
Starting_money.grid()

input_money = Entry(root, width = 10)
input_money.grid(column =1, row = 0)

def clicked():
    res = "The amount of money you have is $" + input_money.get()
    Starting_money.configure(text = res)

button = Button(root, text = "Click me once you have your money", 
                fg = "red", command=clicked)
button.grid(column=2, row=0)

root.mainloop()