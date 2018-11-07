#imports libraries
from tkinter import *
from tkinter.simpledialog import askstring, askinteger
from tkinter.messagebox import showerror
from tkinter import messagebox

#function that controls the instruction page
def infopage():
    infowindow = Tk()
    infowindow.title("Instructions")
    infowindow.resizable(0,0) #removes the option for the user to resize the window

    Label(infowindow, text="Caesar Cipher Instructions:\n1)Enter text to encrypt.\n2)Enter a numerical key into 'Key 1'.\n3)Press encrypt.\n-\nReverse Cipher Instructions:\n1)Enter text to encrypt.\n2)Click 'Encrypt'.\n3)Result will appear under heading 'Output'.\n-\nTransposition Cipher Instructions: \n1)Enter the text you would like to encrypt.\n2)In the textbox 'Key 1', input the number you would like to encode your string by.\n3)Your result will appear under the heading 'Output'.\n-\nAffine Cipher Instructions: \n1)Enter text to encrypt\n2)Enter two numerical keys which will determine how the text is encrypted\n3)Click 'Encrypt'\n4)Your result will be displayed under the heading 'Output'.").grid(row=1,column=1)

#function that determines the user selected option and runs the correct function
def encrypt(plainText):

    #gets the text the user has inputted and stores it under the variable textbox_input
    textbox_input = TextBox.get("1.0","end-1c")
    selection = int(v.get())
    filler = 0

    #user input validation
    if textbox_input.isalpha() == False:
        showerror(title = "Error", message = "Please enter a string without numbers.")
        TextBox.delete("1.0",END)
        textbox_input = ("")
    else:
        filler = 0
        
    if selection == 1:
        #Calls Reverse Cipher Function
        new_text = reverse_cipher(textbox_input)
        Label(master, text=new_text).grid(row=2, column=1)
    elif selection == 2:
        #Calls Caesar Cipher Function
        new_text = caesar_cypher(textbox_input)
        Label(master, text=new_text).grid(row=2, column=1)
    elif selection == 3:
        #Calls Affine Cipher Function
        new_text = Affine_En(textbox_input)
        Label(master, text=new_text).grid(row=2, column=1)
    elif selection == 4:
        #Calls Transposition Cipher Function
        new_text = Transposition_Cipher(textbox_input)
        Label(master, text=new_text).grid(row=2, column=1)

#function for caesar cipher
def caesar_cypher(textbox_input):
    Key1Input = KeyTextBox1.get("1.0","end-1c")
    Key2Input = KeyTextBox2.get("1.0","end-1c")
            
    while True:
        try:
            Key1Input_int = int(Key1Input)
            break
        except ValueError:
            showerror(title = "Error", message = "Please enter an integer.")
            KeyTextBox1.delete("1.0", END)
            KeyTextBox2.delete("1.0", END)
            return

    if Key2Input != "":
        messagebox.showwarning(title = "Warning", message = "Only 1 input needed.")
        KeyTextBox1.delete("1.0",END)
        KeyTextBox2.delete("1.0",END)

    import string     
    alphabet = string.ascii_lowercase 
    key = Key1Input_int
    textbox_input.lower()       
    shifted_alphabet = (alphabet[key:] + alphabet[:key])
    table = str.maketrans(alphabet, shifted_alphabet)
    cypher_text = textbox_input.translate(table) 
    KeyTextBox1.delete("1.0", END)
    KeyTextBox2.delete("2.0", END)
    return cypher_text

#function for reverse cipher
def reverse_cipher(user_choice):
    Key1Input = KeyTextBox1.get("1.0","end-1c")
    Key2Input = KeyTextBox2.get("1.0","end-1c")

    if Key1Input != "" and Key2Input != "":
        messagebox.showwarning(title = "Warning", message = "No key is needed for this cipher.")
        KeyTextBox1.delete("1.0",END)
        KeyTextBox2.delete("1.0",END)
    elif Key1Input != "":
        messagebox.showwarning(title = "Warning", message = "No key is needed for this cipher.")
        KeyTextBox1.delete("1.0",END)
        KeyTextBox2.delete("1.0",END)
    elif Key2Input != "":
        messagebox.showwarning(title = "Warning", message = "No key is needed for this cipher.")
        KeyTextBox1.delete("1.0",END)
        KeyTextBox2.delete("1.0",END)

    user_list = [] 
    for i in user_choice:
        user_list.insert(0,i)  
    return(''.join(user_list))

#function for affine cipher
def Affine_En(plainText):
    Key1Input = KeyTextBox1.get("1.0","end-1c")
    Key2Input = KeyTextBox2.get("1.0","end-1c")

    while True:
        try:
            Key1Input_int = int(Key1Input)
            break
        except ValueError:
            showerror(title = "Error", message = "Please enter an integer.")
            KeyTextBox1.delete("1.0", END)
            KeyTextBox2.delete("1.0", END)
            return

    while True:
        try:
            Key2Input_int = int(Key2Input)
            break
        except ValueError:
            showerror(title = "Error", message = "Please enter an integer.")
            KeyTextBox1.delete("1.0", END)
            KeyTextBox2.delete("1.0", END)
            return
        
    AKey = Key1Input_int
    BKey = Key2Input_int
    EnString = []
    numtext = []
    newnum = []
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for i in range (0, len(plainText)):
        for p in range (0,len(alph)+1):
            if p == 26:
                numtext.append(plainText[int(i)])
            elif alph[int(p)] == plainText[int(i)]:
                numtext.append(p)
                break

    for i in range (0, len(numtext)):
        try:
            numtext[i] = (BKey*numtext[i]+AKey) % len(alph)
        except:
            print("")

    for i in range(0, len(numtext)):
        try:
            EnString.append(alph[numtext[i]])
        except:
            try:
                number = numtext[i] - 26
                EnString.append(alph[number])
            except:
                EnString.append(numtext[i])
                
    String = plainText
    "".join(EnString)
    
    KeyTextBox1.delete("1.0",END)
    KeyTextBox2.delete("1.0",END)
    return EnString


#function for transposition cipher
def Transposition_Cipher(string):
    Key1Input = KeyTextBox1.get("1.0","end-1c")
    Key2Input = KeyTextBox2.get("1.0","end-1c")

    while True:
        try:
            Key1Input_int = int(Key1Input)
            break
        except ValueError:
            showerror(title = "Error", message = "Please enter an integer.")
            KeyTextBox1.delete("1.0", END)
            KeyTextBox2.delete("1.0", END)
            return

    if Key2Input != "":
        messagebox.showwarning(title = "Warning", message = "Only 1 input needed.")
        KeyTextBox1.delete("1.0",END)
        KeyTextBox2.delete("1.0",END)

    
    while True:  
       try:  
           key = Key1Input_int
           break
       except ValueError:  
           showerror(title = "Error", message = "Please enter a integer") 
  
 
    String_List = list(string)  
    Cypher_Array = [] 
    temp = [] 
    count = 0 
    tempcount = 0 
  
 
    while count < len(String_List): 
      if tempcount < Key1Input_int: 
          temp.append(string[count]) 
          count += 1 
          tempcount += 1 
      else: 
          Cypher_Array.append(temp) 
          temp = [] 
          tempcount = 0 
            
    if len(temp) < Key1Input_int: 
        while len(temp) < Key1Input_int: 
            temp.append(" ") 
        Cypher_Array.append(temp) 
    elif len(temp) == Key1Input_int: 
      Cypher_Array.append(temp) 
  
 
    x = 0 
    y = 0 
    z = "" 
    new = [] 
    while y < key: 
      while x < len(Cypher_Array): 
        new.append(Cypher_Array[x][y])  
        x += 1 
      x = 0 
      y += 1 
  
 
      
    Encrypted = z.join(new)
    KeyTextBox1.delete("1.0",END)
    KeyTextBox2.delete("1.0",END)
    return Encrypted

#creates the master window for the program
master = Tk()
master.title("Encryption")
master.resizable(0,0)#removes the option for the user to resize the window
frame = Frame(master)
frame.grid()

#creates a variable 'v' which is used in the radiobuttons to determine user selection
v = IntVar()
v.set(1)

#creates 4 radiobuttons and assigns them all different names and values which can be referenced at other points
Label(master,text="Choose a Cipher: ").grid(row=6)
Radiobutton(master, text="Reverse", variable=v, value=1).grid(row=6,column=1,sticky=W)
Radiobutton(master, text="Caesar", variable=v, value=2).grid(row=7,column=1,sticky=W)
Radiobutton(master, text="Affine", variable=v, value=3).grid(row=8,column=1,sticky=W)
Radiobutton(master, text="Transposition", variable=v, value=4).grid(row=9,column=1,sticky=W)

#making selection equal to the variable 'v' so what the user has selected is known
selection = v.get()

#textbox that user types string into
Label(master, text="Text To Encrypt: ").grid(row=1)
TextBox = Text(master, height = 1, width = 20)
TextBox.grid(row=1, column = 1)

#textbox for 1st key
Label(master, text="Key 1: ").grid(row=4)
KeyTextBox1 = Text(master, height = 1, width = 10)
KeyTextBox1.grid(row=4, column = 1)

#textbox for 2nd key
Label(master, text="Key 2: ").grid(row=5)
KeyTextBox2 = Text(master, height = 1, width = 10)
KeyTextBox2.grid(row=5, column = 1)

#takes the input of the textbox and stores it under the variable 'textbox_input'
textbox_input = TextBox.get("1.0","end-1c")

#label for the outputted encrypted text
Label(master, text="Output: ").grid(row=2)
EncryptedText = Label(master, text="").grid(row=2)

#quit button
Button(master, text="Quit", command=master.destroy).grid(row=10,column=1,sticky=E)

#takes the input of the textbox and stores it under the variable 'plainText' which was used for placeholder reasons
plaintext = TextBox.get("1.0","end-1c")

#button that when pressed runs the encrypt function and therefore encrypts the text 
Button(master, text="Encrypt", command= lambda : encrypt(plaintext)).grid(row=10,column=2)

#button to open the instructions window
Button(master, text="Instructions", command= lambda: infopage()).grid(row=10,column=3)

#runs the window
master.mainloop()

