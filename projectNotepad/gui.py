from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import time
import tkinter.messagebox
import os
import tkinter.scrolledtext as scrolledtext

root = Tk()
root.title('Untitled - Notepad (Beta)')


global open_status_name
global fileName
fileName = None
open_status_name = False


def show():
    a = mytxt1.get("1.0", "end-1c")
    print(a)

def check_textbox(e):
    global fileName
    if mytxt1.get("1.0", "end-1c") != "":
        if fileName != None:
            root.title(f'*{fileName} - Notepad')
        else:
            root.title('*Untitled - Notepad')
    else:
        if fileName != None:
            root.title(f'{fileName} - Notepad')
        else:
            root.title('Untitled - Notepad')

def open_file():
    file = [('All Files', '*.*'),
            ('Python Files', '*.py'),
            ('Text Document', '*.txt')]
    mytxt1.delete('1.0', END)
    txt_file = askopenfile(mode='r', filetypes=file)
    if txt_file:
        global open_status_name
        global fileName
        content = txt_file.read()
        mytxt1.insert('end-1c', content)

        x1 = str(txt_file).split()
        x2 = x1[1]
        open_status_name = x2[6:len(x2)-1]
        name = open_status_name.split('/')
        fileName = name[-1]
        # print('x2: ', x2[6:len(x2)-1])
        # print('Name: ', open_status_name)
        # print('read success')
        root.title(open_status_name)
        time.sleep(0.1)
        root.title(fileName)

def open_file2(e):
    file = [('All Files', '*.*'),
            ('Python Files', '*.py'),
            ('Text Document', '*.txt')]
    mytxt1.delete('1.0', END)
    txt_file = askopenfile(mode='r', filetypes=file)
    if txt_file:
        global open_status_name
        global fileName
        content = txt_file.read()
        mytxt1.insert('end-1c', content)

        x1 = str(txt_file).split()
        x2 = x1[1]
        open_status_name = x2[6:len(x2)-1]
        name = open_status_name.split('/')
        fileName = name[-1]
        # print('x2: ', x2[6:len(x2)-1])
        # print('Name: ', open_status_name)
        # print('read success')
        root.title(open_status_name)
        time.sleep(0.1)
        root.title(fileName)

def save_file():
    global open_status_name
    global fileName
    if open_status_name:
        txt_file = open(open_status_name, 'w')
        txt_file.write(mytxt1.get("1.0", "end-1c"))
        txt_file.close()
        root.title(open_status_name)
        root.title(fileName)
    else:
        save_as()

def save_file_2(e):
    global open_status_name
    global fileName
    if open_status_name:
        txt_file = open(open_status_name, 'w')
        txt_file.write(mytxt1.get("1.0", "end-1c"))
        txt_file.close()
        root.title(open_status_name)
        root.title(fileName)
    else:
        save_as()

def save_as():
    global open_status_name
    global fileName
    file = [('All Files', '*.*'),
            ('Python Files', '*.py'),
            ('Text Document', '*.txt')]
    f = asksaveasfile(initialfile = '*.txt', filetypes=file, defaultextension=file)
    if f == None:
        return
    file_name = str(f).split()
    # print(file_name[1].split('/'))
    file_name_final = file_name[1].split('/')
    xx = file_name_final[-1]
    aa = xx[:len(xx) - 1]
    path1 = file_name[1]
    open_status_name = path1[6:len(path1)-1]
    fileName = aa
    txtsave=str(mytxt1.get("1.0", "end-1c"))
    f.write(txtsave)
    f.close
    root.title(f'{open_status_name}')
    root.title(f'{fileName}')

def exitt():
    global fileName
    if mytxt1.get("1.0", "end-1c") != "":
        if fileName != None:
            ans = tkinter.messagebox.askyesnocancel(title='Notepad', message=f"Do you want to save changes to {fileName}?")
            if ans == None:
                pass
            elif ans == True:
                save_file()
                root.destroy()
            elif ans == False:
                root.destroy()
        else:
            ans = tkinter.messagebox.askyesnocancel(title='Notepad', message="Do you want to save changes to Untitled?")
            if ans == None:
                pass
            elif ans == True:
                save_file()
                root.destroy()
            elif ans == False:
                root.destroy()
    else:
        root.destroy() 

def new():
    global fileName
    global open_status_name
    if mytxt1.get("1.0", "end-1c") != "" and fileName != None:
        ans = tkinter.messagebox.askyesnocancel(title='Notepad', message=f"Do you want to save changes to {fileName}?")
        if ans == None:
            pass
        elif ans == True:
            save_file()
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
        elif ans == False:
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
    elif mytxt1.get("1.0", "end-1c") != "" and fileName != None:
        ans = tkinter.messagebox.askyesnocancel(title='Notepad', message=f"Do you want to save changes to Untitled?")
        if ans == None:
            pass
        elif ans == True:
            save_file()
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
        elif ans == False:
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
    else:
        mytxt1.delete('1.0', END)
        fileName = None
        open_status_name = False
        root.title('Untitled - Notepad')

def new2(e):
    global fileName
    global open_status_name
    if mytxt1.get("1.0", "end-1c") != "" and fileName != None:
        ans = tkinter.messagebox.askyesnocancel(title='Notepad', message=f"Do you want to save changes to {fileName}?")
        if ans == None:
            pass
        elif ans == True:
            save_file()
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
        elif ans == False:
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
    elif mytxt1.get("1.0", "end-1c") != "" and fileName != None:
        ans = tkinter.messagebox.askyesnocancel(title='Notepad', message=f"Do you want to save changes to Untitled?")
        if ans == None:
            pass
        elif ans == True:
            save_file()
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
        elif ans == False:
            mytxt1.delete('1.0', END)
            fileName = None
            open_status_name = False
            root.title('Untitled - Notepad')
    else:
        mytxt1.delete('1.0', END)
        fileName = None
        open_status_name = False
        root.title('Untitled - Notepad')

def printer2(e):
    global open_status_name
    os.startfile(open_status_name, 'print')

def printer():
    global open_status_name
    os.startfile(open_status_name, 'print')

# txt_ip = StringVar()
mytxt1 = scrolledtext.ScrolledText(root, font=("TkDefaultFont", 18))
mytxt1.pack(fill='both')
mytxt1.bind('<Key>', check_textbox)


# Menu
myMenu = Menu()
root.config(menu=myMenu)

# Items Menu(File)
menuItem = Menu(tearoff=0)
menuItem.add_command(label='New         Crtl+N', command=new)
menuItem.add_command(label='Open...    Crtl+O', command=open_file)
menuItem.add_command(label='Save...      Crtl+S', command=save_file)
menuItem.add_command(label='Save as...      ', command=save_as)
menuItem.add_separator()
menuItem.add_command(label='Print...      Crtl+P', command=printer)
menuItem.add_separator()
menuItem.add_command(label='Exit', command=exitt)

helpMenuItem1 = Menu(tearoff=0)
helpMenuItem1.add_command(label="Phone: 00x-xxx-xxxx")
helpMenuItem1.add_command(label="Gmail: test@gmail.com")
helpMenuItem1.add_command(label="Git: Test")

helpMenu = Menu(tearoff=0)
helpMenu.add_cascade(label='About Me', menu=helpMenuItem1)

# Container Menu
myMenu.add_cascade(label='File', menu=menuItem)
myMenu.add_cascade(label='Edit')
myMenu.add_cascade(label='Format')
myMenu.add_cascade(label='View')
myMenu.add_cascade(label='Help', menu=helpMenu)

#shortCut
root.bind('<Key>', check_textbox)
root.bind('<Control-s>', save_file_2)
root.bind('<Control-o>', open_file2)
root.bind('<Control-n>', new2)
root.bind('<Control-p>', printer2)

root.protocol("WM_DELETE_WINDOW", exitt)
root.resizable(True, True)
root.geometry(f'{800}x{600}+400+100')
root.mainloop()