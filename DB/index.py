from tkinter import *
from tkinter import ttk
import database

root = Tk()
root.title("ACESSO")
root.geometry("300x130")
root.attributes('-alpha', 0.9)
root.resizable(width=False, height=False)
root.iconbitmap(default='icon/buraco-negro.ico')

frame = Frame(root, width=300, height=300, bg='#003989', relief="raise")
frame.pack(side=TOP)

usuarioLabel = Label(root, text='Usuário:', bg='#003989', font=('Calibri', 12), fg='white')
usuarioLabel.place(x=10, y=10)
usuarioEntry = ttk.Entry(root, width=30)
usuarioEntry.place(x=80, y=13)

senhaLabel = Label(root, text='Senha:', bg='#003989', font=('Calibri', 12), fg='white')
senhaLabel.place(x=10, y=40)
senhaEntry = ttk.Entry(root, width=30)
senhaEntry.place(x=80, y=43)

def db():
        Nome = usuarioEntry.get()
        Password = senhaEntry.get()

        database.cursor.execute("INSERT INTO Users(Name, Password) VALUES (?, ?)", (Nome, Password))
        database.conn.commit()

enviaButton = ttk.Button(root, text='ENVIA')
enviaButton.place(x=80, y=80)

registrarButton = ttk.Button(root, text='REGISTRAR', command=db)
registrarButton.place(x=190, y=80)

root.mainloop()