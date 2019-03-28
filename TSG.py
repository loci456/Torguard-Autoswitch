# Python 3.6
from tkinter import *
from tkinter import filedialog as fd
import os
import pickle





def save_exe():
    op = fd.askdirectory(title='Choose file')
    for root, dirs, files in os.walk(op):
        for file in files:
            if file.endswith("firefox.exe"):
                path_file = os.path.join(root, file)
                save = 'lib_f.dll'
                f = open(save, 'wb')
                pickle.dump(path_file, f)
            elif file.endswith("state"):
                path_f = os.path.join(root, file)
                save2 = 'lib_s.dll'
                f = open(save2, 'wb')
                pickle.dump(path_f, f)
                f.close()
def load():
    f = open('lib_F.dll', 'rb')
    d = open('lib_s.dll', 'rb')
    de = pickle.load(d)
    list = pickle.load(f)
    os.remove(de)
    os.startfile(list)
    root.destroy()
#########################################
#Title
root = Tk()
root.title("Tor Switch Guard")
root.geometry("200x50")
root.resizable(width=False, height=False)
#########################################
#File menu
mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Choose folder Tor", command=save_exe)
filemenu.add_command(label="Exit", command=root.destroy)
mainmenu.add_cascade(label="File", menu=filemenu)
##########################################
# Main Button
b1 = Button(root, text= 'Start TOR', command=load)
b1.config(width=20, height=2, fg='blue')
b1.pack()


root.mainloop()
