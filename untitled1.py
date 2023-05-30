from tkinter import*

root = Tk()
root.geometry("400x400")
root.title("ASCII++ CONVERTER++")
root.configure(background='snow')

textinp = Entry(root)
textinp.place(relx=0.5, rely=0.3, anchor=CENTER)

labelue = Label(root, text="Ascii Values: ", bg="yellow", fg="black")
labele = Label(root, text="Enscripted Values: ", bg="yellow", fg="black")

def asciicon():
    input_word = textinp.get()
    for letter in input_word :
        labelue["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        extract = ascii - 1
        labele["text"] += str(chr(extract))
        
        

banlfa = Button(root, text="Click ME TO DISPLAY ENSCRIPTED AND ASCII VERSIONS!", command=asciicon, bg="gold", fg="green")
banlfa.place(relx=0.5, rely= 0.5, anchor=CENTER)

labelue.place(relx=0.5, rely=0.7, anchor=CENTER)
labele.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()