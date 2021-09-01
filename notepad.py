from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newFile():
    global file
    root.title("untitled - Notapad")
    file = None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) +" - Notepad")    
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()


def saveFile():
    global file
    if file== None:
        file= asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            # save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
            print("file Save ")
    else:
        # save the file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()       

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by saurabh yadav ")


if __name__ == '__main__':
    # Basic tkinter setup

    root = Tk()
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("1.ico")
    root.geometry("644x650")

    # Add Text Area
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand=True,fill=BOTH)

    # Lats create a menubar
    MenuBar = Menu(root)

    # File Menu starts
    FileMenu = Menu(MenuBar,tearoff=0)

    # To open a new file
    FileMenu.add_command(label="New",command=newFile)
    # To Open already existing file
    FileMenu.add_command(label="Open",command=openFile)
    # to save the current file
    FileMenu.add_command(label="save",command=saveFile)
    # FileMenu.add_seperator()
    FileMenu.add_command(label="Exit",command=quitApp)

    MenuBar.add_cascade(label="File",menu=FileMenu)
    # File Menu Ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar,tearoff=0)

    # to give a feature of cut,copy,paste
    EditMenu.add_command(label='Cut',command=cut)
    EditMenu.add_command(label='Copy',command=copy)
    EditMenu.add_command(label='Paste',command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    # Edit Menu Ends
    # Help Menu starts
    helpMenu = Menu(MenuBar,tearoff=0)
    helpMenu.add_command(label='About Notepad',command=about)
    MenuBar.add_cascade(label="Help",menu=helpMenu)
    # help Menu Ends

    root.config(menu=MenuBar)

    # adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)




root.mainloop()
