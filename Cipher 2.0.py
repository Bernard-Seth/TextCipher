import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (mainWindow, newWindow):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(mainWindow)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class mainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self,
                    text="Welcome to my Caesar Cipher.  To begin the cipher press start.\nTo learn more about"
                            " the Caesar Cipher press facts.")
        lbl.grid(column=0, row=0)

        factsbtn = ttk.Button(self, text="Facts", command=clickedFacts)
        factsbtn.grid(row=2, column=1, padx=10, pady=10)

        startbtn = ttk.Button(self, text="Start", command=lambda: controller.show_frame(newWindow))
        startbtn.grid(row=1, column=1, padx=10, pady=10)

class newWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global inserttxt
        enterlbl = ttk.Label(self, text="Enter your text below and click Cipher to run the cipher program")
        enterlbl.grid(row=0)

        inserttxt = tk.Text(self)
        inserttxt.insert('1.0', 'enter your message here')
        inserttxt.grid(row=1)

        cipher = ttk.Button(self, text='Cipher', command= clickedCipher())
        cipher.grid(row=2)

        outputlbl = ttk.Label(self, text="The ciphered text is:")
        outputlbl.grid(row=3)

        global ntxtbox

        ntxtbox = tk.Text(self)
        ntxtbox.insert('1.0', 'Ciphered message')
        ntxtbox.grid(row=4)

def clickedFacts():
    History='    The Caesar Cipher is an encryption method that dates back to the 1st century B.C.  It is named' \
            ' after Julias Caesar who used it to send military messages across his empire.  It is believed that when' \
            ' his enemies found it, they assumed the messages were written in another language and simply did not try' \
            ' to decipher it.\n \n    My cipher uses an 8 letter shift, meaning an A will be written as an I.  Julius' \
            ' Caesar is believed to have used a shift of 3, while his nephew used a shift of only 1'
    messagebox.showinfo('Facts', History)

def split(word):
    return [char for char in word]

def shift(indexes):

    if indexes < 25 - 8:
        indexes += 8
    else:
        indexes -= 17
    return indexes

def intoCipher(otext, p, k):
    arrLow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    arrCap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    indexA = 0
    lowOrUp = '0'
    b = 0
    x = len(otext)
    index = 0
    while index < x:
        while indexA < 25 and lowOrUp == '0':
            if otext[index] == arrLow[indexA]:
                lowOrUp = '1'
                p = indexA
                b = 1
            elif otext[index] == arrCap[indexA] and lowOrUp == '0':
                lowOrUp = '1'
                p = indexA
                b = 2
            indexA += 1
        k = shift(p)
        if b == 1:
            otext[index] = arrLow[k]
        elif b == 2:
            otext[index] = arrCap[k]
        b = 0
        lowOrUp = '0'
        index += 1
        indexA = 0
    return otext

def clickedCipher():
    global string
    string = inserttxt.get('1.0', tk.END)
    string = split(string)
    string = intoCipher(string, 0, 0)
    string = ''.join(string)
    ntxtbox.delete('sel.first', tk.END)
    ntxtbox.insert('sel.first', string)

app = tkinterApp()
app.mainloop()