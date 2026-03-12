import tkinter as tk

root = tk.Tk()
root.title('CALCULATOR TEST')
root.config(bg='#121212')
root.attributes('-alpha', 0.8)
root.resizable(width=False, height=False)
root.iconbitmap('C:/Users/Albert/Desktop/calculator_py/assets/icon.ico')

tk.Label(root, text='CALCULATOR').pack

#DISPLAY CALCULATOR

display = tk.Entry(root, font=('Arial', 24), borderwidth = 5, relief=tk.FLAT, justify = 'right')
display.config(bg='light gray',font=('Fixedsys',24))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



#FUNCTIONARE

def btn_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def btn_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, 'Error')

def btn_back():
    current = display.get()
    shortened_string = current[:-1]
    display.delete(0, tk.END)
    display.insert(0, shortened_string)

    

#BUTONUL 9

button_9 = tk.Button(root, text='9',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(9))
button_9.config(bg="gray")
button_9.grid(row=1, column=0)

#BUTONUL 8

button_8 = tk.Button(root, text='8',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(8))
button_8.config(bg="gray")
button_8.grid(row=1, column=1, padx=1, pady=1)

#BUTONUL 7

button_7 = tk.Button(root, text='7',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(7))
button_7.config(bg="gray")
button_7.grid(row=1, column=2)

#BUTONUL 6

button_6 = tk.Button(root, text='6',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(6))
button_6.config(bg="gray")
button_6.grid(row=2, column=0)

#BUTONUL 5

button_5 = tk.Button(root, text='5',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(5))
button_5.config(bg="gray")
button_5.grid(row=2, column=1)

#BUTONUL 4

button_4 = tk.Button(root, text='4',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(4))
button_4.config(bg="gray")
button_4.grid(row=2, column=2)

#BUTONUL 3

button_3 = tk.Button(root, text='3',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(3))
button_3.config(bg="gray")
button_3.grid(row=3, column=0)

#BUTONUL 2

button_2 = tk.Button(root, text='2',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(2))
button_2.config(bg="gray")
button_2.grid(row=3, column=1)

#BUTONUL 1

button_1 = tk.Button(root, text='1',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(1))
button_1.config(bg="gray")
button_1.grid(row=3, column=2)

#BUTONUL 0

button_0 = tk.Button(root, text='0',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click(0))
button_0.config(bg="gray")
button_0.grid(row=4, column=1)

#BUTONUL '+'

button_PLUS = tk.Button(root, text='+',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click('+'))
button_PLUS.config(bg="gray")
button_PLUS.grid(row=4, column=3)

#BUTONUL '-'

button_MINUS = tk.Button(root, text='-',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click('-'))
button_MINUS.config(bg="gray")
button_MINUS.grid(row=4, column=4)

#BUTONUL '='

button_EGAL = tk.Button(root, text='=',font='Fixedsys', padx=40, pady=20, command=btn_equal)
button_EGAL.config(bg="gray")
button_EGAL.grid(row=1, column=4)

#BUTONUL '/'

button_DIVIDE = tk.Button(root, text='/',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click('/'))
button_DIVIDE.config(bg="gray")
button_DIVIDE.grid(row=3, column=4)


#BUTONUL '*'

button_TIMES = tk.Button(root, text='*',font='Fixedsys', padx=40, pady=20, command=lambda: btn_click('*'))
button_TIMES.config(bg="gray")
button_TIMES.grid(row=2, column=4)

#BUTONUL '<-'

button_BACK = tk.Button(root, text='<',font='Fixedsys', padx=40, pady=20, command=btn_back)
button_BACK.config(bg="gray")
button_BACK.grid(row=0, column=4)

root.mainloop()