from tkinter import *
from tkinter import ttk
from math import *

bw = 7
bh = 3

WindowFrame = Tk()
WindowState = "Menu"
btbgcolor = "light grey"
outbgcolor = "powder blue"

OptionList = {"":"light grey","Light":"light grey","Dark":"white"}

options = StringVar(WindowFrame)
options.set(OptionList[""])

def ButtonPressed(num):
    global operator
    operator = operator + str(num)
    text_Input.set(operator)
    print(operator)

def MenuButtonPressed():
    print("Al menú")
    WindowState = "Menu"
    DeleteCalculator()
    CreateStartMenu()
    return WindowState

def MenuExitButtonPressed():
    print("Salir de la App")
    quit()

def MenuLaunchButtonPressed():
    print("A la calculadora")
    WindowState = "Launch"
    DeleteStartMenu()
    CreateCalculatorMenu()
    return WindowState

def resultado():
    global operator
    try:
        opera=eval(str(operator))
        text_Input.set(opera)
    except:
        text_Input.set("ERROR")
    operator = ""

def clear():
    global operator
    operator=("")
    text_Input.set("0")


text_Input=StringVar()
operator = ""

ExitButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="Exit", font=(18), width=25, height=5, anchor="center", relief="groove", command= MenuExitButtonPressed)
LaunchButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="Launch", font=(18), width=25, height=5, anchor="center", relief="groove", command= MenuLaunchButtonPressed)
MenuButton = Button(WindowFrame, cursor="hand2", borderwidth=5, text="Menu", font=(18), width=10, height=5, anchor="center", relief="groove", command= MenuButtonPressed)

Output = Entry(WindowFrame,font=('arial',20,'bold'),width=22,textvariable=text_Input,bd=20,insertwidth=4,bg="powder blue", justify="right")

#NUMBERS BUTTONS
OneButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="1", font=(1), width=bw, height=bh, anchor="center",bg=options.get(), relief="groove", command= lambda:ButtonPressed(1))
TwoButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="2", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(2))
ThreeButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="3", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(3))
FourButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="4", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(4))
FiveButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="5", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(5))
SixButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="6", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(6))
SevenButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="7", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(7))
EightButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="8", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(8))
NineButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="9", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(9))
ZeroButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="0", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed(0))
DotButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text=".", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed("."))

#OPERATORS BUTTONS
PlusButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="+", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed("+"))
MinusButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="-", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed("-"))
MultiplyButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="*", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed("*"))
DivideButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="/", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= lambda:ButtonPressed("/"))
EqualButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="=", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= resultado)
ClearButton = Button(WindowFrame, cursor="hand2", borderwidth=10, text="C", font=(1), width=bw, height=bh, anchor="center", bg=options.get(), relief="groove", command= clear)

def CreateStartMenu():
    LaunchButton.grid(row=1, column=0, padx=10, pady=10)

    ExitButton.grid(row=3, column=0, padx=10, pady=10)

def DeleteStartMenu():
    LaunchButton.grid_remove()

    ExitButton.grid_remove()

def CreateCalculatorMenu():
    MenuButton.grid(row=0, column=0, padx=10, pady=10)
    Output.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

    OneButton.grid(row=2, column=1, padx=10, pady=10)
    TwoButton.grid(row=2, column=2, padx=10, pady=10)
    ThreeButton.grid(row=2, column=3, padx=10, pady=10)
    FourButton.grid(row=3, column=1, padx=10, pady=10)
    FiveButton.grid(row=3, column=2, padx=10, pady=10)
    SixButton.grid(row=3, column=3, padx=10, pady=10)
    SevenButton.grid(row=4, column=1, padx=10, pady=10)
    EightButton.grid(row=4, column=2, padx=10, pady=10)
    NineButton.grid(row=4, column=3, padx=10, pady=10)
    ZeroButton.grid(row=5, column=2, padx=10, pady=10)
    DotButton.grid(row=5, column=1, padx=10, pady=10)

    PlusButton.grid(row=2, column=4, padx=10, pady=10)
    MinusButton.grid(row=3, column=4, padx=10, pady=10)
    MultiplyButton.grid(row=4, column=4, padx=10, pady=10)
    DivideButton.grid(row=5, column=4, padx=10, pady=10)
    EqualButton.grid(row=5, column=3, padx=10, pady=10)
    ClearButton.grid(row=6, column=2, padx=10, pady=10)

def DeleteCalculator():
    MenuButton.grid_remove()
    Output.grid_remove()

    OneButton.grid_remove()
    TwoButton.grid_remove()
    ThreeButton.grid_remove()
    FiveButton.grid_remove()
    FourButton.grid_remove()
    SixButton.grid_remove()
    SevenButton.grid_remove()
    EightButton.grid_remove()
    NineButton.grid_remove()
    ZeroButton.grid_remove()
    DotButton.grid_remove()

    PlusButton.grid_remove()
    MinusButton.grid_remove()
    MultiplyButton.grid_remove()
    DivideButton.grid_remove()
    EqualButton.grid_remove()
    ClearButton.grid_remove()