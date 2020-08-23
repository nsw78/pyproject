import tkinter
from tkinter import Label

def GET():
    global userbox,passbox,error
    pass

    error=tkinter.Label(bottomframe,text="FAVOR DIGITAR NOME DE USUÁRIO SENHA CORRETAS.!",fg='red',font='bolt')
    error.pack()
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("280x250")
    topframe = tkinter.Frame(root)
    topframe.pack()

    bottomframe = tkinter.Frame(root)
    bottomframe.pack()

    heading: Label = tkinter.Label(topframe, text =" SISTEMA HOSPITALAR", bg='white', fg='orange', font='Times 16 bold italic')

    username = tkinter.Label(topframe, text =" Usuário :")
    userbox = tkinter.Entry(topframe)

    password = tkinter.Label(bottomframe, text =" Senha :")
    passbox = tkinter.Entry(bottomframe)

    login = tkinter.Button(bottomframe, text=' LOGIN',font='arial 9 bold', command=GET)
    root.wm_iconbitmap(r'C:\Users\sprov\PycharmProjects\pyproject\Project_01\icons\login.jpg')
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("Sistema Hospitalar : LOGIN :")
    root.mainloop()
Entry()

