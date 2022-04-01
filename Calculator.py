# CREATED BY RANJAN KUMAR
# LINKEDIN : -- https://www.linkedin.com/in/ranjan1560
# GITHUB : -- https://github.com/ranjan1560


from tkinter import *

# for calculator window

window = Tk()
window.geometry("280x450")
window.title("CALCULATOR")
window.config(bg="#074f8a")
window.iconbitmap("calc.ico")

# created 2 frame in window ,for expression and button

expression_frame = Frame(window, bg="#e0e3e1")
button_frame = Frame(window, bg="#e97f40")
expression_frame.pack()
button_frame.pack()

# function define
expression = ''

def press(n):
    global expression
    expression += str(n)
    equation.set(expression)


def clear():
    global expression
    expression = ''
    equation.set('0')


def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set("ERROR")
        expression = ''


# defined variable for storing expression

font_entry = ('Roboto', 22)
equation = StringVar()
equation.set("0")

equation_field = Entry(expression_frame, textvariable=equation, font=font_entry, justify='right', bg='#bff000')
equation_field.pack(ipadx=100, ipady=25)

font_entry1 = ('hack', 20)

# button

button1 = Button(button_frame, text='1', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(1))
button2 = Button(button_frame, text='2', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(2))
button3 = Button(button_frame, text='3', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(3))
plus = Button(button_frame, text='+', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
              height=3, command=lambda: press('+'))


button4 = Button(button_frame, text='4', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(4))
button5 = Button(button_frame, text='5', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(5))
button6 = Button(button_frame, text='6', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(6))
minus = Button(button_frame, text='-', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
               height=3, command=lambda: press('-'))


button7 = Button(button_frame, text='7', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(7))
button8 = Button(button_frame, text='8', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(8))
button9 = Button(button_frame, text='9', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                 height=3, command=lambda: press(9))
multiply = Button(button_frame, text='*', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                  height=3, command=lambda: press('*'))


dot = Button(button_frame, text='.', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
             height=3, command=lambda: press('.'))
zero = Button(button_frame, text='0', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
              height=3, command=lambda: press(0))
clear = Button(button_frame, text='AC', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
               height=3, command=clear)
divide = Button(button_frame, text='/', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                height=3, command=lambda: press('/'))


equal = Button(button_frame, text='=', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
               height=3, command=equal)
backspace = Button(button_frame, text='⌫', font=font_entry1, relief='ridge', bg='#e97f40', borderwidth=1, width=5,
                   height=3, command=backspace)


button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
plus.grid(row=0, column=3)


button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
minus.grid(row=1, column=3)


button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
multiply.grid(row=2, column=3)


dot.grid(row=4, column=0)
zero.grid(row=4, column=1)
clear.grid(row=4, column=2)
divide.grid(row=4, column=3)


equal.grid(row=5, column=0, columnspan=3, sticky='news')
backspace.grid(row=5, column=3)


window.mainloop()
