from tkinter import *
class Passwords:
    def __init__(self,toplevel):
        self.frame4=Frame(toplevel,pady=10)
        self.frame4.pack()

        # Definindo o título
        self.frame1=Frame(toplevel)
        self.frame1.pack()
        self.titulo=Label(self.frame1)
        self.titulo['text']='ACESSO RESTRITO'
        self.titulo['fg']='darkblue'
        self.titulo['font']=('Verdana','14','bold')
        self.titulo['height']=3
        self.titulo['width']=20
        self.titulo.pack()

        # Definindo o nome e o campo
        self.frame2=Frame(toplevel)
        self.frame2.pack()
        
        self.nome=Label(self.frame2)
        self.nome['text']='Nome: '
        self.nome['font']=('Verdana','10','bold')
        self.nome['width']=8
        self.nome.pack(side=LEFT)

        self.nomeBox=Entry(self.frame2)
        self.nomeBox['font']=('Verdana','10','bold')
        self.nomeBox['width']=10
        self.nomeBox.focus_force()
        self.nomeBox.pack(side=LEFT)

        # Definindo o nome e a senha
        self.frame3=Frame(toplevel)
        self.frame3.pack()
        
        self.senha=Label(self.frame3)
        self.senha['text']='Senha: '
        self.senha['font']=('Verdana','10','bold')
        self.senha['width']=8
        self.senha.pack(side=LEFT)
        
        self.senhaBox=Entry(self.frame3)
        self.senhaBox['font']=('Verdana','10','bold')
        self.senhaBox['width']=10
        self.senhaBox['show']='*'
        self.senhaBox.pack(side=LEFT)

        # Definindo o resultado da nome e senha
        self.frame4=Frame(toplevel,pady=10)
        self.frame4.pack()

        self.confere=Button(self.frame4,command=self.conferir)
        self.confere['text']='Conferir'
        self.confere['font']=('Verdana','10','bold')
        self.confere['bg']='DarkGray'              
        self.confere.pack()

        self.msg=Label(self.frame4)
        self.msg['text']='AGUARDANDO...'
        self.msg['height']=3
        self.msg['font']=('Verdana','10','bold')
        self.msg.pack()

    # Definindo a forma de conferir os dados
    def conferir(self):
        NOME=self.nomeBox.get()
        SENHA=self.senhaBox.get()
        if NOME == SENHA:
            self.msg['text']='ACESSO PERMITIDO'
            self.msg['fg']='Darkgreen'
        else:
            self.msg['text']='ACESSO NEGADO'
            self.msg['fg']='Red'
            self.nomeBox.focus_force()

         
instancia=Tk()
Passwords(instancia)
instancia.mainloop()
