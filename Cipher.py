import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


''' Class tkinterApp is used to build a container for the windows.  Each window has a grid that governs how widgets
are layed out.  Each time a window is opened, the frame is cleared, and the new frame is built using the show_frame
function.'''
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

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()

'''The mainWindow is the start page.  It navigates the user to the begining of the Cipher, or shows a message box with
information on the ceasar cipher, and this program.'''

class mainWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        imgCaesar = tk.PhotoImage(file='juliusCaesar.gif')
        Caesar = tk.Label(self, image=imgCaesar)
        Caesar.image = imgCaesar
        Caesar.grid(row = 1, column = 0, rowspan = 2)

        imgStandard = tk.PhotoImage(file='RomanStandard.gif')
        Standard = tk.Label(self, image=imgStandard)
        Standard.image=imgStandard
        Standard.grid(row = 1, column = 2, rowspan=2)

        lbl = ttk.Label(self,
                    justify = tk.CENTER,
                    text="Welcome to my Caesar Cipher.  To begin the cipher press start.  To learn more about"
                            " the Caesar Cipher press facts.")
        lbl.grid(column=0, row=0, padx = 10, pady = 10, columnspan=3 )

        factsbtn = ttk.Button(self, text="Facts", command=clickedFacts)
        factsbtn.grid(row=2, column=1, padx=10, pady=10)

        startbtn = ttk.Button(self, text="Start", command=lambda: controller.show_frame(newWindow))
        startbtn.grid(row=1, column=1, padx=10, pady=10)

'''The newWindow is used to take an input, put it through the cipher, display the new text, and then reverse the cipher
into a popup window which shows all of the steps side by side.'''

class newWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global inserttxt
        enterlbl = ttk.Label(self, text="Enter your text below and click Cipher to run the cipher program")
        enterlbl.grid(row=0, column=0, padx = 10, pady = 10, columnspan=2)

        inserttxt = tk.Text(self)
        inserttxt.insert('1.0', 'enter your message here')
        inserttxt.grid(row=1, column=0, padx = 10, pady = 10, columnspan=2)

        cipher = ttk.Button(self, text='Cipher', command=clickedCipher)
        cipher.grid(column=0, row=2, padx = 10, pady = 10)

        decipher = ttk.Button(self, text='Reverse Cipher', command=clickedDecipher)
        decipher.grid(column=1, row=2, padx = 10, pady = 10)

        outputlbl = ttk.Label(self, text="The ciphered text is:")
        outputlbl.grid(row=3, column=0, padx = 10, pady = 10, columnspan=2)

        global ntxtbox

        ntxtbox = tk.Text(self)
        ntxtbox.insert('1.0', 'Ciphered message')
        ntxtbox.grid(column=0, row=4, padx = 10, pady = 10, columnspan=2)

def clickedFacts():
    History='    The Caesar Cipher is an encryption method that dates back to the 1st century B.C.  It is named' \
            ' after Julias Caesar who used it to send military messages across his empire.  It is believed that when' \
            ' his enemies found it, they assumed the messages were written in another language and simply did not try' \
            ' to decipher it.\n \n    My cipher uses an 8 letter shift, meaning an A will be written as an I.  Julius' \
            ' Caesar is believed to have used a shift of 3, while his nephew used a shift of only 1'
    messagebox.showinfo('Facts', History)

def split(word):
    return [char for char in word]


def clickedDecipher():
    global decipher
    decipher = string
    decipher = intoDecipher(decipher)
    decipher = ''.join(decipher)
    Message='The original message being sent:\n' + Ostring + '\nThe ciphered message is: \n' + string + '\nThe deciphered message is: \n' + decipher
    messagebox.showinfo('Cipher', Message)

def intoDecipher(otext):
    arrLow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    arrCap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    ntext = []
    cryptText = []
    i = 0
    for eachLetter in otext:
        if eachLetter in arrCap:
            index = arrCap.index(eachLetter)
            crypting = (index - 8) % 26
            cryptText.append(crypting)
            newLetter = arrCap[crypting]
            ntext.append(newLetter)
        elif eachLetter in arrLow:
            index = arrLow.index(eachLetter)
            crypting = (index - 8) % 26
            cryptText.append(crypting)
            newLetter = arrLow[crypting]
            ntext.append(newLetter)
        else:
            ntext.append(otext[i])
        i += 1

    return ntext

def intoCipher(otext):
    arrLow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    arrCap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ntext = []
    cryptText = []
    i = 0
    for eachLetter in otext:
        if eachLetter in arrCap:
            index = arrCap.index(eachLetter)
            crypting = (index + 8) % 26
            cryptText.append(crypting)
            newLetter = arrCap[crypting]
            ntext.append(newLetter)
        elif eachLetter in arrLow:
            index = arrLow.index(eachLetter)
            crypting = (index + 8) % 26
            cryptText.append(crypting)
            newLetter = arrLow[crypting]
            ntext.append(newLetter)
        else:
            ntext.append(otext[i])
        i += 1
    return ntext

def clickedCipher():
    global Ostring
    global string
    Ostring = inserttxt.get('1.0', tk.END)
    string = split(Ostring)
    string = intoCipher(string)
    string = ''.join(string)
    ntxtbox.delete('1.0', tk.END)
    ntxtbox.insert('1.0', string)

def main():
    app = tkinterApp()
    app.mainloop()

if __name__ == "__main__":
    main()
