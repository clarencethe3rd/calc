from tkinter import*

gui = Tk()
gui.title("Calculator")
gui.geometry("800x500")
display = ""
display2 = StringVar()
entry = Entry(textvariable=display2,width=14,font=("",26))
entry.place(x=0,y=0)
num = 0
grid1 = Frame(gui)
grid1.place(x=0,y=47)

def press(n):
    global display,entry,display2
    display +=str(n)
    print(display)
    display2.set(display)
    
def result():
    global display,num
    num = eval(display)
    display = str(num)
    print(num)
    display2.set(num)

"""    str_num = str(num)
    num1 = len(str_num)
    num1-=12
    num = round(num,num1)
    print(num)"""
    
def dele():
    global display,display2
    print(display.rstrip(display[-1]))
#Buttons

button_0 = Button(grid1,text= "0", font=("",25),command=lambda: press(0))
button_1 = Button(grid1,text= "1", font=("",25),command=lambda: press(1))
button_2 = Button(grid1,text= "2", font=("",25),command=lambda: press(2))
button_3 = Button(grid1,text= "3", font=("",25),command=lambda: press(3))
button_4 = Button(grid1,text= "4", font=("",25),command=lambda: press(4))
button_5 = Button(grid1,text= "5", font=("",25),command=lambda: press(5))
button_6 = Button(grid1,text= "6", font=("",25),command=lambda: press(6))
button_7 = Button(grid1,text= "7", font=("",25),command=lambda: press(7))
button_8 = Button(grid1,text= "8", font=("",25),command=lambda: press(8))
button_9 = Button(grid1,text= "9", font=("",25),command=lambda: press(9))
button_x = Button(grid1,text= "x", font=("",25),command=lambda: press("*"))
button_div = Button(grid1,text= "÷", font=("",25),command=lambda: press("/"))
button_add = Button(grid1,text= "+", font=("",25),command=lambda: press("+"))
button_min = Button(grid1,text= "-", font=("",25),command=lambda: press("-"))
button_equal = Button(grid1,text= "=", font=("",25),command=result)
button_del = Button(grid1,text="Del", font=("",25),command=dele)
button_dec = Button(grid1,text=".", font=("",25),command=lambda: press("."))
button_per = Button(grid1,text="%", font=("",25),command=lambda: press("%"))
button_neg = Button(grid1,text="+/-", font=("",25))

#Button placement

button_0.grid(column=2,row=5)
button_1.grid(column=1,row=4)
button_2.grid(column=2,row=4)
button_3.grid(column=3,row=4) 
button_4.grid(column=1,row=3)
button_5.grid(column=2,row=3)
button_6.grid(column=3,row=3) 
button_7.grid(column=1,row=2)
button_8.grid(column=2,row=2)
button_9.grid(column=3,row=2) 
button_x.grid(column=4,row=2) 
button_div.grid(column=4,row=1) 
button_add.grid(column=4,row=4) 
button_min.grid(column=4,row=3) 
button_equal.grid(column=4,row=5)
button_del.grid(column=1,row=1)
button_dec.grid(column=3,row=5)
button_neg.grid(column=2,row=1)
button_per.grid(column=3,row=1)

gui.mainloop()
