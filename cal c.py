from tkinter import *
form1= Tk()
form1.title("Simple Calculator")
form1.geometry("280x440")

txt1=Entry(form1, width=40, justify=CENTER)
txt1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add():
	first_number = txt1.get()
	global f_num
	global we_do
	we_do = "addition"
	f_num = int(first_number)
	txt1.delete(0, END)

def button_clear():
    txt1.delete(0, END)

def button_equal():
	second_number = txt1.get()
	txt1.delete(0, END)
	
	if we_do == "addition":
		txt1.insert(0, f_num + int(second_number))

	if we_do == "subtraction":
		txt1.insert(0, f_num - int(second_number))

	if we_do == "multiplication":
		txt1.insert(0, f_num * int(second_number))

	if we_do == "division":
		txt1.insert(0, f_num / int(second_number))
		
def button_subtract():
	first_number = txt1.get()
	global f_num
	global we_do
	we_do = "subtraction"
	f_num = int(first_number)
	txt1.delete(0, END)

def button_multiply():
	first_number = txt1.get()
	global f_num
	global we_do
	we_do = "multiplication"
	f_num = int(first_number)
	txt1.delete(0, END)

def button_divide():
	first_number = txt1.get()
	global f_num
	global we_do
	we_do = "division"
	f_num = int(first_number)
	txt1.delete(0, END)


def button_click(number):
        c = txt1.get()
        txt1.delete(0, END)
        txt1.insert(0, c + number)

b_0 = Button(form1, text="0", padx=30, pady=20, command=lambda: button_click("0"))
b_1 = Button(form1, text="1", padx=30, pady=20, command=lambda: button_click("1"))
b_2 = Button(form1, text="2", padx=30, pady=20, command=lambda: button_click("2"))
b_3 = Button(form1, text="3", padx=30, pady=20, command=lambda: button_click("3"))
b_4 = Button(form1, text="4", padx=30, pady=20, command=lambda: button_click("4"))
b_5 = Button(form1, text="5", padx=30, pady=20, command=lambda: button_click("5"))
b_6 = Button(form1, text="6", padx=30, pady=20, command=lambda: button_click("6"))
b_7 = Button(form1, text="7", padx=30, pady=20, command=lambda: button_click("7"))
b_8 = Button(form1, text="8", padx=30, pady=20, command=lambda: button_click("8"))
b_9 = Button(form1, text="9", padx=30, pady=20, command=lambda: button_click("9"))

button_add = Button(form1, text="+", padx=30, pady=20, command=button_add)
button_equal = Button(form1, bg="light blue", text="=", padx=80, pady=20, command=button_equal)
button_clear = Button(form1, text="Clear", padx=70, pady=20, command=button_clear)
button_subtract = Button(form1, text="-", padx=31, pady=20, command=button_subtract)
button_multiply = Button(form1, text="*", padx=30, pady=20, command=button_multiply)
button_divide = Button(form1, text="/", padx=30, pady=20, command=button_divide)

b_0.grid(row=4, column=0)
b_1.grid(row=3, column=0)
b_2.grid(row=3, column=1)
b_3.grid(row=3, column=2)
b_4.grid(row=2, column=0)
b_5.grid(row=2, column=1)
b_6.grid(row=2, column=2)
b_7.grid(row=1, column=0)
b_8.grid(row=1, column=1)
b_9.grid(row=1, column=2)

button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
form1.mainloop()