from tkinter import *
from math import sqrt

def roots_finder():

    text1.delete('1.0', END)
    text2.delete('1.0', END)

    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())

    d = b**2-4*a*c

    if d > 0:
        x1 = (-1*b+sqrt(d))/2*a
        x2 = (-1*b - sqrt(d)) / 2 * a
        text1.insert(1.0, f'x1={x1}')
        text2.insert(1.0, f'x2={x2}')

    elif d == 0:
        x = -b/2*a
        text2.insert(1.0, f'x={x}')

    else:
        text1.insert(1.0, '        No')
        text2.insert(1.0, ' Roots')


window = Tk()
window.title('Quadratic equation')
window.geometry('500x450')
window.resizable(False, False)
window.configure(bg='#f8ffbf')

label1 = Label(text='ax^2+bx+c=0', font='Arial 19', bg='#f8ffbf')
label1.place(relx=0.35, rely=0.1)

label2 = Label(text='a=', font='Arial 19', bg='#f8ffbf')
label2.place(relx=0.19, rely=0.27)

entry1 = Entry(window, width=3, font='Arial 19')
entry1.place(relx=0.27, rely=0.27)

label3 = Label(text='b=', font='Arial 19', bg='#f8ffbf')
label3.place(relx=0.39, rely=0.27)

entry2 = Entry(window, width=3, font='Arial 19')
entry2.place(relx=0.47, rely=0.27)

label4 = Label(text='c=', font='Arial 19', bg='#f8ffbf')
label4.place(relx=0.59, rely=0.27)

entry3 = Entry(window, width=3, font='Arial 19')
entry3.place(relx=0.67, rely=0.27)

text1 = Text(window, width=7, height=2, font='Arial 19')
text1.place(relx=0.25, rely=0.55)

text2 = Text(window, width=7, height=2, font='Arial 19')
text2.place(relx=0.55, rely=0.55)

button1 = Button(window, text='Result', width=8, height=2, font='Arial 15', command=roots_finder, bg='#f8ffbf')
button1.place(relx=0.4, rely=0.75)

window.mainloop()
