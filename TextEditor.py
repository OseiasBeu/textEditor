#Importação de bibliotecas e módulos
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class TextEditor:
    def __init__(self,root):
        '''
        -> Método Construtor: -
        Descrição: Definição do método construtor!

        - Parâmetros: 
            root: Instancia do tkinker

        - Retornos: 
            title: Título da janela
            geometry: Dimensões da Janela
            filename: Tipo de arquivos gerados
        '''

        self.root = root

        #Titulo da Janela
        self.root.title('Beu_IO - Editor de Texto')
        #Dimensões da Janela
        self.root.geometry('1200x700+200+150')
        
        #Inicialização do arquivo
        self.filename = None
        self.title = StringVar()
        self.status = StringVar()

        #Criando barra de título
        self.titlebar = Label(self.root, textvariable=self.title, font=("times new roman",15,"bold"), bd=2,relief=GROOVE)

        #Posicionando a barra de título na janela
        self.titlebar.pack(side=TOP, fill=BOTH)
        self.settitle()

        #Criado barra de status
        self.statusbar = Label(self.root, textvariable=self.title, font=("times new roman",15,"bold"), bd=2,relief=GROOVE)
        #Posicionando a barra de status na janela
        self.titlebar.pack(side=TOP, fill=BOTH)
        #Iniciando o status
        self.status.set("Bem Vindo ao meu Editor de Texto!")

        #Criando o menu
        self.menubar = Menu(self.root, font=("times new roman",15,"bold"),activebackground="skyblue")

        #Configuração do menu na janela
        self.root.config(menu=self.menubar)

        #Criando a opção arquivo no menu
        self.filemenu = Menu(self.menubar, font=("times new roman",12,"bold"),activebackground="skyblue", tearoff=0)

        # Adicionando novo arquivo no menu
        self.filemenu.add_command(label='Novo Arquivo',accelerator='Ctrl+N', command=self.novoArquivo)

        # Adicioanndo abertura de arquivos
        self.filemenu.add_command(label='Abrir Arquivo',accelerator='Ctrl+O', command=self.abrirArquivo)

        #Adicionamdo separacao de opções
        self.filemenu.add_separator()

        #Cascateando o menu em subopções
        self.menubar.add_cascade(label='Arquivo', menu=self.filemenu)

    




    #Definição da função  de configuração do titulo
    def settitle(self):
        '''
        -> Método Settitle
            - Descrição: Responsável por manter um título no arquivo!
            - parâmetros: 
                self: --

            - Retornos:
                self.filename: titulo da janela/arquivo
        '''
        if self.filename:
            self.title.set(self.filename)
        else:
            self.title.set('Sem título!')


    # Definição da funnção novo arquivo
    def novoArquivo(self,*args):
        '''
        -> Método novoArquivo
        - Descrição: Responsável pela criação de um novo arquivo!
        
        - Parâmetros: 
            self

        - Retornos:
             - Status com a criação de um novo arquivo

        '''
        self.txtarea.delete("1.0",END)
        self.filename = None
        self.settitle()
        self.status.set('Novo Arquivo Criado!')


#Criação da instância do tkinker
root = Tk()
TextEditor(root)
root.mainloop()