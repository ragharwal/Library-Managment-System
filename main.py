from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os

root = Tk()

root.title("Library Management System")
scr_w = root.winfo_screenwidth()
scr_h = root.winfo_screenheight()
width = 1150
height = 600

x = (scr_w/2) - (width/2)
y = (scr_h/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width,height,x,y))
root.resizable(0,0)

# ADD Book
def addBook():
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()

    if (e1=="" or e2=="" or e3=="" or e4=="" or e5=="" or e6==""):
        tkMessageBox.showerror("Error","Please fill all the entries")

    else:
        result = tkMessageBox.askquestion("Add Book","Are you sure you want to add this Book?")
        entry1.delete(0,END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        if result == "yes":
            with open('book.csv', 'a') as csvfile:
                csvfile.write('{0}, {1}, {2}, {3},{4},{5}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6))
                # csvfile.write(e1+","+e2+","+e3+","+e4+","+e5+","+e6+"\n")
            csvfile.close()
            tkMessageBox.showinfo("Success","Book added successfully")

        else:
            tkMessageBox.showerror("Unsuccess","Book not added")

# DELETE Book
def deleteBook():
    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    e5 = entry5.get()
    e6 = entry6.get()

    if (e1 == "" or e2 == "" or e3 == "" or e4 == "" or e5 == "" or e6 == ""):
        tkMessageBox.showerror("Error", "Please fill all the entries")

    else:
        result = tkMessageBox.askquestion("Delete Book", "Are you sure you want to delete this Book?")
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        if result == "yes":
            with open('book.csv', 'r') as csvfile, open('tempBook.csv', 'w') as tempfile:
                for line in csvfile:
                    if e1 not in line:
                        tempfile.write(line)
            os.remove('book.csv')
            os.rename('tempBook.csv', 'book.csv')
            csvfile.close()
            tempfile.close()
            tkMessageBox.showinfo("Success", "Book deleted successfully")

            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)

        else:
            tkMessageBox.showerror("Unsuccess", "Book not deleted")

# UPDATE Book
def updateBook():
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()

    if (e1=="" or e2=="" or e3=="" or e4=="" or e5=="" or e6==""):
        tkMessageBox.showerror("Error","Please fill all the entries")
    
    else:
        result = tkMessageBox.askquestion("Update Book","Are you sure you want to update this Book?")
        if(result == "yes"):
            with open('book.csv', 'r') as csvfile, open('tempBook.csv', 'w') as tempfile:
                for line in csvfile:
                    if str(e1) not in line:
                        tempfile.write(line)
                    else:
                        tempfile.write('{0}, {1}, {2}, {3},{4} ,{5}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6))
            os.remove('book.csv')
            os.rename('tempBook.csv', 'book.csv')
            csvfile.close()
            tempfile.close()
            tkMessageBox.showinfo("Success","Book updated successfully")

            entry1.delete(0,END)
            entry2.delete(0,END)
            entry3.delete(0,END)
            entry4.delete(0,END)
            entry5.delete(0,END)
            entry6.delete(0,END)

# VIEW Book
def viewBook():
    tree.delete(*tree.get_children())
    with open('book.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            Book_ID = row['Book_ID']
            Book_Name = row['Book_Name']
            Book_Type = row['Book_Type']
            Book_Author = row['Book_Author']
            Book_Publisher = row['Book_Publisher']
            Book_Price = row['Book_Price']
            tree.insert("", "end", values=(Book_ID, Book_Name, Book_Type, Book_Author, Book_Publisher, Book_Price))
    csvfile.close()

# CLEAR Book
def clearBook():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)

Book_ID = StringVar()
Book_Name = StringVar()
Book_Type = StringVar()
Book_Author = StringVar()
Book_Publisher = StringVar()
Book_Price = StringVar()

Top = Frame(root, width=900, height=50, bd=8, relief='raise')
Top.pack(side=TOP)
Left = Frame(root, width=200, height=500, bd=8, relief='raise')
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief='raise')
Right.pack(side=RIGHT)

Buttons = Frame(Left, width=550, height=300, bd=0, relief='raise')
Buttons.pack(side=BOTTOM)
Forms = Frame(Left, width=700, height=650)
Forms.pack(side=TOP)

txt_title = Label(Top, width=1300, text="Library Management System", font=('arial', 25, 'bold'), bd=10, anchor='center')
txt_title.pack()

# FIELDS HEADING
l1 = Label(Forms, text="Book ID:", font=('arial', 15, 'bold'), bd=8)
l1.grid(row=0, stick="e")
l2 = Label(Forms, text="Book Name:", font=('arial', 15, 'bold'), bd=8)
l2.grid(row=1, stick="e")
l3 = Label(Forms, text="Book Type:", font=('arial', 15, 'bold'), bd=8)
l3.grid(row=2, stick="e")
l4 = Label(Forms, text="Book Author:", font=('arial', 15, 'bold'), bd=8)
l4.grid(row=3, stick="e")
l5 = Label(Forms, text="Book Publisher:", font=('arial', 15, 'bold'), bd=8)
l5.grid(row=4, stick="e")
l6 = Label(Forms, text="Book Price:", font=('arial', 15, 'bold'), bd=8)
l6.grid(row=5, stick="e")

txt_result = Label(Buttons)
txt_result.pack(side=TOP)

# FIELDS
entry1 = Entry(Forms, textvariable=Book_ID, font=('arial', 20, 'bold'), bd=6, insertwidth=4, bg="powder blue", justify='left')
entry1.grid(row=0, column=1)
entry2 = Entry(Forms, textvariable=Book_Name, font=('arial', 20, 'bold'), bd=6, insertwidth=4, bg="powder blue", justify='left')
entry2.grid(row=1, column=1)
entry3 = Entry(Forms, textvariable=Book_Type, font=('arial', 20, 'bold'), bd=6, insertwidth=4, bg="powder blue", justify='left')
entry3.grid(row=2, column=1)
entry4 = Entry(Forms, textvariable=Book_Author, font=('arial', 20, 'bold'), bd=6, insertwidth=4, bg="powder blue", justify='left')
entry4.grid(row=3, column=1)
entry5 = Entry(Forms, textvariable=Book_Publisher, font=('arial', 20, 'bold'), bd=6, insertwidth=4, bg="powder blue", justify='left')
entry5.grid(row=4, column=1)
entry6 = Entry(Forms, textvariable=Book_Price, font=('arial', 20, 'bold'), bd=6, insertwidth=4, bg="powder blue", justify='left')
entry6.grid(row=5, column=1)

# BUTTONS
b1 = Button(Buttons, text="Add Book", font=('arial', 13, 'bold'), bd=4, bg="powder blue", command=addBook)
b1.pack(side=LEFT)
b2 = Button(Buttons, text="Update Book", font=('arial', 13, 'bold'), bd=4, bg="powder blue", command=updateBook)
b2.pack(side=LEFT)
b3 = Button(Buttons, text="Delete Book", font=('arial', 13, 'bold'), bd=4, bg="powder blue", command=deleteBook)
b3.pack(side=LEFT)
b4 = Button(Buttons, text="View Book", font=('arial', 13, 'bold'), bd=4, bg="powder blue", command=viewBook)
b4.pack(side=LEFT)
b5 = Button(Buttons, text="Clear Book", font=('arial', 13, 'bold'), bd=4, bg="powder blue", command=clearBook)
b5.pack(side=LEFT)

# SCROLL BAR
scrollBarX = Scrollbar(Right, orient=HORIZONTAL)
scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY = Scrollbar(Right, orient=VERTICAL)
scrollBarY.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(Right, columns=("Book_ID", "Book_Name", "Book_Type", "Book_Author", "Book_Publisher", "Book_Price"), 
    selectmode="extended", height=500, yscrollcommand=scrollBarY.set, xscrollcommand=scrollBarX.set
)

scrollBarX.config(command=tree.xview)
scrollBarY.config(command=tree.yview)

tree.heading('Book_ID', text="Book ID", anchor=W)
tree.heading('Book_Name', text="Book Name", anchor=W)
tree.heading('Book_Type', text="Book Type", anchor=W)
tree.heading('Book_Author', text="Book Author", anchor=W)
tree.heading('Book_Publisher', text="Book Publisher", anchor=W)
tree.heading('Book_Price', text="Book Price", anchor=W)
tree.column('#0', stretch=NO, minwidth=20, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()

if __name__ == '__main__':
    root.mainloop()