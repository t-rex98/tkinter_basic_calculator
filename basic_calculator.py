from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")
    equation.set('enter your expression')

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("simple calculator")
    gui.geometry("265x125")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('enter your expression')

    button1 = Button(gui, text=' 1 ', fg='black', bg='OliveDrab1', command=lambda: press(1), height=1,width=7)
    button2 = Button(gui, text=' 2 ', fg='black', bg='OliveDrab1', command=lambda: press(2), height=1,width=7)
    button3 = Button(gui, text=' 3 ', fg='black', bg='OliveDrab1', command=lambda: press(3), height=1,width=7)
    button4 = Button(gui, text=' 4 ', fg='black', bg='OliveDrab1', command=lambda: press(4), height=1,width=7)
    button5 = Button(gui, text=' 5 ', fg='black', bg='OliveDrab1', command=lambda: press(5), height=1,width=7)
    button6 = Button(gui, text=' 6 ', fg='black', bg='OliveDrab1', command=lambda: press(6), height=1,width=7)
    button7 = Button(gui, text=' 7 ', fg='black', bg='OliveDrab1', command=lambda: press(7), height=1,width=7)
    button8 = Button(gui, text=' 8 ', fg='black', bg='OliveDrab1', command=lambda: press(8), height=1,width=7)
    button9 = Button(gui, text=' 9 ', fg='black', bg='OliveDrab1', command=lambda: press(9), height=1,width=7)
    button0 = Button(gui, text=' 0 ', fg='black', bg='OliveDrab1', command=lambda: press(0), height=1,width=7)
    plus    = Button(gui, text=' + ', fg='black', bg='OliveDrab1', command=lambda: press("+"), height=1,width=7)
    minus   = Button(gui, text=' - ', fg='black', bg='OliveDrab1', command=lambda: press("-"), height=1,width=7)
    multiply= Button(gui, text=' * ', fg='black', bg='OliveDrab1', command=lambda: press("*"), height=1,width=7)
    divide  = Button(gui, text=' / ', fg='black', bg='OliveDrab1', command=lambda: press("/"), height=1,width=7)
    equal   = Button(gui, text=' = ', fg='black', bg='OliveDrab1', command=equalpress, height=1,width=7)
    clear   = Button(gui, text='Clr', fg='black', bg='OliveDrab1', command=clear, height=1,width=7)
    
    button1.grid(row=2, column=0)
    button2.grid(row=2, column=1)
    button3.grid(row=2, column=2)
    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)
    button7.grid(row=4, column=0)
    button8.grid(row=4, column=1)
    button9.grid(row=4, column=2)
    button0.grid(row=5, column=0)
    plus.grid(row=2, column=3)
    minus.grid(row=3, column=3)
    multiply.grid(row=4, column=3)
    divide.grid(row=5, column=3)
    equal.grid(row=5, column=2)
    clear.grid(row=5, column=1)

    # button2 = Button(gui, text=' 2 ', fg='black', bg='OliveDrab1', command=lambda: press(2))
    # button3 = Button(gui, text=' 3 ', fg='black', bg='OliveDrab1', command=lambda: press(3))
    # button1 = Button(gui, text=' 1 ', fg='black', bg='OliveDrab1', command=lambda: press(1))
    # button5 = Button(gui, text=' 5 ', fg='black', bg='OliveDrab1', command=lambda: press(5))
    # button4 = Button(gui, text=' 4 ', fg='black', bg='OliveDrab1', command=lambda: press(4))
    # button6 = Button(gui, text=' 6 ', fg='black', bg='OliveDrab1', command=lambda: press(6))
    # button7 = Button(gui, text=' 7 ', fg='black', bg='OliveDrab1', command=lambda: press(7))
    # button8 = Button(gui, text=' 8 ', fg='black', bg='OliveDrab1', command=lambda: press(8))
    # button9 = Button(gui, text=' 9 ', fg='black', bg='OliveDrab1', command=lambda: press(9))
    # button0 = Button(gui, text=' 0 ', fg='black', bg='OliveDrab1', command=lambda: press(0))
    # plus = Button(gui, text=' + ', fg='black', bg='OliveDrab1', command=lambda: press("+"))
    # minus = Button(gui, text=' - ', fg='black', bg='OliveDrab1', command=lambda: press("-"))
    # multiply = Button(gui, text=' * ', fg='black', bg='OliveDrab1', command=lambda: press("*"))
    # divide = Button(gui, text=' / ', fg='black', bg='OliveDrab1', command=lambda: press("/"))
    # equal = Button(gui, text=' = ', fg='black', bg='OliveDrab1', command=equalpress)
    # clear = Button(gui, text=' Clr ', fg='black', bg='OliveDrab1', command=clear)

    # button1.grid(row=2, column=0, sticky=N+E+S+W)
    # button2.grid(row=2, column=1, sticky=N+E+S+W)
    # button3.grid(row=2, column=2, sticky=N+E+S+W)
    # button4.grid(row=3, column=0, sticky=N+E+S+W)
    # button5.grid(row=3, column=1, sticky=N+E+S+W)
    # button6.grid(row=3, column=2, sticky=N+E+S+W)
    # button7.grid(row=4, column=0, sticky=N+E+S+W)
    # button8.grid(row=4, column=1, sticky=N+E+S+W)
    # button9.grid(row=4, column=2, sticky=N+E+S+W)
    # button0.grid(row=5, column=0, sticky=N+E+S+W)
    # plus.grid(row=2, column=3)
    # minus.grid(row=3, column=3)
    # multiply.grid(row=4, column=3)
    # divide.grid(row=5, column=3)
    # equal.grid(row=5, column=2)
    # clear.grid(row=5, column=1)

    gui.mainloop()