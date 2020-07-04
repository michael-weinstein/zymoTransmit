import os
try:
    import tkinter
    active = True
except [ImportError, ModuleNotFoundError]:
    active = False


defaultDirectory = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]


def selectFileForOpening(prompt:str, defaultDirectory:str=defaultDirectory, fileTypes=(("All Files", "*.*"))):
    if not active:
        raise RuntimeError("Attempted to use GUI while not active")
    import tkinter.filedialog
    file = tkinter.filedialog.askopenfilename(initialdir=defaultDirectory, title=prompt, filetypes=fileTypes)
    return file


def textEditFile(filePath:str):
    class _Window(tkinter.Frame):
        def __init__(self, master, filePath: str, title: str = "Text Editor"):
            if not os.path.isfile(filePath):
                raise FileNotFoundError("Unable to find file %s" % filePath)
            self.filePath = filePath
            tkinter.Frame.__init__(self, master)
            self.master = master
            self.master.title(title)
            self.pack(fill=tkinter.BOTH, expand=1)
            menu = tkinter.Menu(topWindow)
            topWindow.config(menu=menu)
            self.fileMenu = tkinter.Menu(menu)
            menu.add_cascade(label="Save", menu=self.fileMenu)
            self.text = tkinter.Text(topWindow, height=200, width=200)
            self.fileMenu.add_command(label="Save", command=self.saveFile)
            self.text.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=True)
            self.scrollbar = tkinter.Scrollbar(topWindow, orient="vertical")
            self.scrollbar.config(command=self.text.yview)
            self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y, expand=True)
            self.text.config(yscrollcommand=self.scrollbar.set)
            file = open(self.filePath, 'r')
            for line in file:
                self.text.insert(tkinter.END, line)
            file.close()

        def saveFile(self):
            text = self.text.get(1.0, tkinter.END)
            file = open(self.filePath, 'w')
            file.write(text)
            file.close()

    topWindow = tkinter.Tk()
    topWindow.geometry("400x400")
    editor = _Window(topWindow, filePath, "Editing %s. Save and quit when done." %filePath)
    topWindow.mainloop()


def promptForCertPassword():
    def onPasswordEntry(event):
        password = passwordBox.get()
        topWindow.destroy()
    def onOKClick():
        password = passwordBox.get()
        topWindow.destroy()
    password = ""
    topWindow = tkinter.Tk()
    passwordBox = tkinter.Entry(topWindow, show = "*")
    tkinter.Label(topWindow, text = "Enter certificate password, if there is one.").pack(side = 'top')
    passwordBox.pack(side = 'top')
    passwordBox.bind("<Return>", onPasswordEntry)
    tkinter.Button(topWindow, command=onOKClick, text = "OK").pack(side = 'top')
    topWindow.mainloop()
    return password
