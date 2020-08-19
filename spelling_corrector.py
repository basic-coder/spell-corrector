#import all function /classes from tkinter
from tkinter import *
from textblob import TextBlob

#function to clear both the text entry box
def clearALL():

    #whole content of the text entry is deleted
    word1_field.delete(0,END)
    word2_field.delete(0,END)

#function to get a correct word
def correction():

    #get a content from entry box
    input_word = word1_field.get()

    #create a TextBlob object
    blob_obj = TextBlob(input_word)

    #get a correct word
    corrected_word = str(blob_obj.correct())

    #insert method inserting the 
    #value in the text entry box
    word2_field.insert(10, corrected_word)

#Driver code

if __name__ == "__main__":

    #Create a GUI window
    root = Tk()

    #set the background color of GUI window
    root.configure(background = 'black')

    #set the configuration of GUI window (WidthxHeight)
    root.geometry('600x400')

    #set the name of tkinter on GUI window
    root.title("Spell Corrector")

    #Create Welcome to Spelling Corrector Application label1
    headlabel = Label(root, text = " Welcome to spell Corrector Application",font=("arial",15,"bold"),
                    fg = 'black', bg = 'red')

    #Create a "Input Word":label
    label1 = Label(root, text="Input Word", font=("arial",10,"bold"),
                fg="black", bg="green")

    #Create a "Corrected word": label
    label2 =Label(root, text = "Corrrected word", font=("arial",10,"bold"),
                fg='black', bg = 'green')

    #grid method is used to placing
    #the widget at the respective position
    #in table like structure
    headlabel.grid(row = 0,column = 1)
    label1.grid(row = 2,column = 0,padx= 20, pady=20)
    label2.grid(row = 4, column = 0 ,padx = 20,pady=20)

    #Create a text entry box
    #for filling or typing the information
    word1_field = Entry()
    word2_field = Entry()

    #padx keyword argument used to get padding along x-axis . 
    #pady keyword argument used to set padding along y-axis .

    word1_field.grid(row = 2, column=1, padx=10, pady = 10)
    word2_field.grid(row = 4,column=1,padx=10, pady = 10)


    #Create a Correction button and attached
    #with correction function
    button1 = Button(root, text = "Correction",font=("arial",10,"bold") , bg="red", fg="black"
                ,command = correction)

    button1.grid(row = 3, column = 1,pady=10)

    #Create a Clear Button and attacked
    #with clearAll function

    button2 = Button(root, text="Clear", bg="red",font=("arial",10,"bold"),
                fg="black", command = clearALL)

    button2.grid(row=5, column = 1,pady=10)

    #start the GUI
    root.mainloop()