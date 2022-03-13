from email.mime import image
from tkinter import *
from tkinter import messagebox
from turtle import back, right
from tkinter import ttk
import dataBase

def register():
    loginButton.place(x=5000)
    registerButton.place(x=5000)

    nomeLabel = Label(rightFrame, text='Nome', font=('Calibri', 20), bg='#ff8080', fg='white')
    nomeLabel.place(x=5, y=5)
    nomeEntry = ttk.Entry(rightFrame, width=38)
    nomeEntry.place(x=85, y=17)

    emailLabel = Label(rightFrame, text='E-mail', font=('Calibri', 20), bg='#ff8080', fg='white')
    emailLabel.place(x=5, y=42)
    emailEntry = ttk.Entry(rightFrame, width=38)
    emailEntry.place(x=85, y=51)

    userLabel.place(x=5, y=80)
    userEntry.place(x=130, y=91)

    def RegisterDB():
        Nome = nomeEntry.get()
        email = emailEntry.get()
        User = userEntry.get()
        Password = passEntry.get()

        dataBase.cursor.execute("INSERT INTO Users(Name, Email. User, Password) VALUES (?, ?, ?, ?)", (Nome, email, User, Password))

        dataBase.conn.commit() #salvar altercao
        messagebox.showinfo(title='Register Info', message='Registrado com sucesso')

    register = ttk.Button(rightFrame, text='REGISTER', width=10, command=RegisterDB)
    register.place(x=90, y=200)

    backButton = ttk.Button(rightFrame, text='BACK', width=10)
    backButton.place(x=200, y=200)

#--------------------------------------------------
#---tkiner-----------------------------------------

jan = Tk()
jan.title('ACESSO')
jan.geometry('600x300')
jan.configure(background='white')
jan.resizable(width=False, height=False)
#jan.attributes('-alpha', 0.9) = transparencia
jan.iconbitmap(default='icon/icone.ico')

#----images-----------------------------------------
logo = PhotoImage(file="icon/latest.png")

#----whidge-----------------------------------------
leftFrame = Frame(jan, width=200, height=300, bg='#ff8080', relief="raise")
leftFrame.pack(side=LEFT)
rightFrame = Frame(jan, width=395, height=300, bg='#ff8080', relief="raise")
rightFrame.pack(side=RIGHT)

logoLabel = Label(leftFrame, image=logo, bg='#ff8080')
logoLabel.place(x=22, y=30)

#----base-------------------------------------------
userLabel = Label(rightFrame, text='Username', font=('Calibri', 20), bg='#ff8080', fg='white')
userLabel.place(x=5, y=70)

userEntry = ttk.Entry(rightFrame, width=30)
userEntry.place(x=130, y=81)

passLabel = Label(rightFrame, text='Password', font=('Calibri', 20), bg='#ff8080', fg='white')
passLabel.place(x=5, y=120)

passEntry = ttk.Entry(rightFrame, width=30, show='•')
passEntry.place(x=130, y=131)

fanLabel = Label(leftFrame, text='Kirby fan club', font=('Comic Sans MS', 16), bg='#ff8080', fg='white')
fanLabel.place(x=35, y=180)

#----button-------------------------------------------
loginButton = ttk.Button(rightFrame, text='LOGIN', width=10)
loginButton.place(x=90, y=200)

registerButton = ttk.Button(rightFrame, text='REGISTER', width=10, command=register)
registerButton.place(x=200, y=200)


jan.mainloop()