from tkinter import *
from math import sqrt



#main window

window = Tk()
window.title("Calculator")
window.resizable(width=False,height=False)
window.geometry("320x433")
window.tk.call("tk",'scaling', 3.0)

numbers=""
history=[]

#creating the functions for each button

def Calculate():
    global numbers
    try:
        result = str(eval(numbers))
        history.append(f"{numbers} = {result}")
        numbers = result
        entry.delete(0, "end")
        entry.insert(0, numbers)
    
        
    except ZeroDivisionError: # zerodiv error
        clear_screen()
        entry.insert(0,"Cannot Divide by 0")
                
    except:
        clear_screen()
        entry.insert(0, "Error")
        
  
def add_to_screen(symbol):
    #adding numbers or symbols to screen
    global numbers
    numbers += str(symbol)
    entry.delete(0,"end")
    entry.insert(0,numbers)
    
def num_squared():
    #calculates the number in the power of 2
    global numbers
    numbers= str(eval(numbers)**2)
    entry.delete(0,"end")
    entry.insert(0,numbers)

def num_fraction():
    #converts the number into a fraction
    global numbers
    numbers= str(1/eval(numbers)) 
    entry.delete(0,"end")
    entry.insert(0,numbers)

def convert_percent():
    #converts the number into %
    global numbers
    numbers = str(eval(numbers)/100)
    entry.delete(0,"end")
    entry.insert(0,numbers)

def clear_screen():
    #clears the screen ( del everything )
    global numbers
    numbers=""
    entry.delete(0,"end")
    entry.insert(0,numbers)
    
def delete_one():
    #deleting the last char from the numbers ( backspace )
    global numbers
    numbers=numbers[:-1]    
    entry.delete(0,"end")
    entry.insert(0,numbers)
    
def square_root():
    #calculates the square root of the number
    global numbers
    numbers= str(sqrt(eval(numbers)))
    entry.delete(0,"end")
    entry.insert(0,numbers)

def key_press(event):
    #handeling keyboard imports ---- break ensures no duplicates  ( eixa thema xwris to break .. ekamne m ta dipla j tripla )
    if event.char.isdigit() or event.char in '+-*/().':
        add_to_screen(event.char)
        return "break"
    elif event.keysym == 'Return':  
        Calculate()
        return "break"
    elif event.keysym == 'BackSpace':  
        delete_one()
        return "break"
    

def show_history():
    #creates a new window showing all the items in the list stored after every "=" or keyEnter in new window
    history_window = Toplevel(window)
    history_window.title("History")
    history_window.geometry("320x200")
    history_text = Text(history_window, width=40, height=10, state=DISABLED)
    history_text.pack()
    history_text.config(state=NORMAL)
    history_text.delete(1.0, END)
    for item in history:
        history_text.insert(END, item + "\n")
    history_text.config(state=DISABLED)
    
    
#input field 

entry=Entry(window,width=12,font=("arial",12))
entry.grid(column=0,row=0,columnspan=3,ipady=28)
entry.bind('<KeyPress>', key_press)
entry.focus_set()

#numeric buttons and their position


num0 = Button(window,text="0",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("0"))
num1 = Button(window,text="1",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("1"))
num2 = Button(window,text="2",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("2"))
num3 = Button(window,text="3",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("3"))
num4 = Button(window,text="4",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("4"))
num5 = Button(window,text="5",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("5"))
num6 = Button(window,text="6",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("6"))
num7 = Button(window,text="7",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("7"))
num8 = Button(window,text="8",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("8"))
num9 = Button(window,text="9",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("9"))

num0.grid(column=1,row=8)
num1.grid(column=0,row=7)
num2.grid(column=1,row=7)
num3.grid(column=2,row=7)
num4.grid(column=0,row=6)
num5.grid(column=1,row=6)
num6.grid(column=2,row=6)
num7.grid(column=0,row=5)
num8.grid(column=1,row=5)
num9.grid(column=2,row=5)


# sign buttons and positions

plus = Button(window,text="+",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("+"))
minus = Button(window,text="-",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("-"))
multiply = Button(window,text="*",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("*"))
divide = Button(window,text="/",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("/"))
equal = Button(window,text="=",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=Calculate)
clear = Button(window,text="CE",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=clear_screen)
dot = Button(window,text="•",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("."))
square = Button(window,text="x2",width=10,height=3,fg="black",bg="white",font=("arial",4),command=num_squared)
percent = Button(window,text="%",width=10,height=3,fg="black",bg="white",font=("arial",4),command=convert_percent)
fraction = Button(window,text="1/x",width=10,height=3,fg="black",bg="white",font=("arial",4),command=num_fraction)
minus_one = Button(window,text="",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=delete_one)
open_brac = Button(window,text="(",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen("("))
close_brac = Button(window,text=")",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=lambda:add_to_screen(")"))
root = Button(window,text="√",width=10,height=3,fg="black",bg="white",font=("arial",4,"bold"),command=square_root)
history_btn = Button(window,text="\u231A",width=3,height=1,fg="black",bg="white",font=("arial",10,"bold"),command=show_history)

equal.grid(column=3,row=8)
plus.grid(column=3,row=7)
minus.grid(column=3,row=6)
multiply.grid(column=3,row=5)
divide.grid(column=3,row=4)
clear.grid(column=0,row=8)
dot.grid(column=2,row=8)
square.grid(column=1,row=3)
percent.grid(column=2,row=3)
fraction.grid(column=0,row=3)
minus_one.grid(column=3,row=3)
open_brac.grid(column=1,row=4)
close_brac.grid(column=2,row=4)
root.grid(column=0,row=4)
history_btn.grid(column=3,row=0)





window.mainloop()