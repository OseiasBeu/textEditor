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

        # Adicioando opção de salvar
        self.filemenu.add_command(label='Salvar',accelerator='Ctrl+S', command=self.salvar)

        # Adicioando opção de salvar como
        self.filemenu.add_command(label='Salvar Como',accelerator='Ctrl+A', command=self.salvarComo)

        #Adicionamdo separacao de opções
        self.filemenu.add_separator()

        # Adicioando opção de SAIR
        self.filemenu.add_command(label='Sair',accelerator='Ctrl+E', command=self.sair)

        #Cascateando o menu em subopções de arquivo
        self.menubar.add_cascade(label='Arquivo', menu=self.filemenu)

        #Criando a opção Editar no menu 
        self.editmenu = Menu(self.menubar, font=("times new roman",12,"bold"),activebackground="skyblue", tearoff=0)

        #Adicioandno a função cortar
        self.editmenu.add_command(label='Cortar',accelerator='Ctrl+X', command=self.cortar)

        #Adicioandno a função cortar
        self.editmenu.add_command(label='Copiar',accelerator='Ctrl+C', command=self.copiar)       

        #Adicioandno a função cortar
        self.editmenu.add_command(label='Colar',accelerator='Ctrl+V', command=self.colar)

        #Adicionamdo separacao de opções
        self.editmenu.add_separator()

        #Adicioanndo a Opção de desfazer
        self.editmenu.add_command(label='Desfazer',accelerator='Ctrl+U', command=self.desfazer)

        #Cascateando o menu em subopções de editar
        self.menubar.add_cascade(label='Editar', menu=self.editmenu)

        #Criando a opção Ajuda no menu 
        self.helpmenu = Menu(self.menubar, font=("times new roman",12,"bold"),activebackground="skyblue", tearoff=0)

        #Adicioanndo a Opção de sobre
        self.helpmenu.add_command(label='Sobre',accelerator='Ctrl+U', command=self.sobre)
        #Cascateando o menu em subopções de editar
        self.menubar.add_cascade(label='Ajuda', menu=self.helpmenu)

        scrol_y = Scrollbar(self.root,orient=VERTICAL)
        self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",15,"bold"),state="normal",relief=GROOVE)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        self.atalhos()



    # Definição da função  de configuração do titulo
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
    
    # Definição abrir aquivo
    def abrirArquivo(self, *args):
        '''
        -> Método abrirArquivo
         - Descrição: Responsável por abrir arquivos já existentes no computador
         - Parâmetros:
            caminhos: Caminhos de arquivos existentes no computador
        
         - Retorno:
            Seu retorno é o arquivo aberto na text area.
        '''
        # tratando possíveis erros
        try:
            self.filename = filedialog.askopenfilename(title='Escolha um arquivo', filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            if self.filename:
                #Abrindo arquivo no modo de leitura
                infile = open(self.filename,'r')
                
                #Limpando a area de texto
                self.txtarea.delete("1.0",END)

                #Inserindo linhas na area de texto
                for line in infile:
                    self.txtarea.insert(END,line)
                
                #Fechadno arquivo
                infile.close()

                #Alterando o nome da janela
                self.settitle()

                #Atualizando o staus
                self.status.set("Arquivo aberto com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro:",e)

    # Definindo função de salvar
    def salvar(self, *args):
        '''
        -> Método Salvar
        - Descrição: Responsável por salvar os arquivos em edição!
        
        - Parâmetros: 
            self 

        - Retornos:
             - Arquivo de edição salvo

        '''
        # Tratando possíveis erros
        try:
            # Verificando se o arquivo está vazio
            if self.filename:
                data = self.txtarea.get("1.0",END)

                #abrindo arquivo no modo de escrita
                outfile = open(self.filename,"w")

                #Escrevendo dentro do arquivo
                outfile.write(data)
                outfile.close()
                #chamando a função de título
                self.settitle()

                #Atualizando o status
                self.status.set("Salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro:",e)
   
    # Definindo função de salvar como
    def salvarComo(self, *args):
        '''
        -> Método salvarComo
        - Descrição: Responsável por salvar novos arquivos com extenções específicas, podendo ser incluídas novas extenções.
            Exemplo de extenções: 
                Padrão: "sem titulo.txt",
                Outros tipos: ("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")
        
        - Parâmetros: 
            self

        - Retornos:
             - Arquivo novo com um extenção .
        '''
        # Tratando possíveis erros
        try:
            #Perguntando o nome e o tipo do arquivo
            untitledfile = filedialog.asksaveasfilename(title = "Salvar Arquivo como",defaultextension=".txt",initialfile = "sem titulo.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            data = self.txtarea.get("1.0",END)

            #abrindo arquivo no modo de escrita
            outfile = open(untitledfile,"w")

            #Escrevendo dentro do arquivo
            outfile.write(data)
            outfile.close()

            # Atualizando o titulo da pagina
            self.filename = untitledfile
            #chamando a função de título
            self.settitle()
            #Atualizando o status
            self.status.set("Salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro:",e)

    #Definição da função sair
    def sair(self,*args):
        '''
        -> Método sair
        - Descrição: Responsável por sair do editor de texto
        
        - Parâmetros: 
            self

        - Retornos:
             - Fechamento do programa!
        '''
        op = messagebox.askyesno("ATENÇÃO",'Você deseja mesmo sair?')
        if op >0:
            self.root.destroy()
        else:
            return

    #Definição da função cortar:
    def cortar(self,*args):
        '''
        -> Método cortar
        - Descrição: Responsável por cortar textos dentro do editor de texto.
        
        - Parâmetros: 
            self

        - Retornos:
             - textos removidos da tela armazenados na memória do teclado.
        '''
        self.txtarea.event_generate("<<Cut>>")

    #Definição da função copiar:
    def copiar(self,*args):
        '''
        -> Método sair
        - Descrição: Responsável por copiar palavras e frases do editor de texto.
        
        - Parâmetros: 
            self

        - Retornos:
             - textos copiados da tela armazenados na memória do teclado.
        '''
        self.txtarea.event_generate("<<Copy>>")

    #Definição da função colar:
    def colar(self,*args):
        '''
        -> Método colar
        - Descrição: Responsável por colar textos e frases na memória do teclado
        
        - Parâmetros: 
            self

        - Retornos:
             - textos inseridos na area de texto.
        '''
        self.txtarea.event_generate("<<Paste>>")

    #Definição da função desfazer
    def desfazer(self, *args):
        '''
        -> Método desfazr
        - Descrição: Responsável desfazer alterações feitas na area de texto
        
        - Parâmetros: 
            self

        - Retornos:
             - Alterações feitas dentro da ara de texto sendo desfeitas.
        '''
        #Tratando qualquer eventualidade
        try:
            if self.filename:
                self.txtarea.delete('1.0',END)
                #Arbrindo arquivo no modo leitura
                infile = open(self.filename,"r")

                #Inserindo lina a lina na area de texto
                for line in infile:
                    self.txtarea.insert(END,line)
                
                # Fechando o arquivo
                infile.close()
                self.settitle()
                self.status.set('Desfeito com sucesso!')
            else:
                self.txtarea.delete('1.0',END)
                self.filename = None
                self.settitle()
                self.status.set('Desfeito com sucesso!')
        except Exception as e:
            messagebox.showerror('Erro:',e)

    def sobre(self):
        '''
        -> Método sobre
        - Descrição: Responsável por indicar ao usuário informações do desenvolvedor
        
        - Parâmetros: 
            self

        - Retornos:
             - text box com uma mensagem
        '''
        messagebox.showinfo("Sobre o Text Editor","Um editor de texto simples criado com Python \n, Acesse: https://github.com/OseiasBeu/textEditor para mais! ")

    def atalhos(self):
        '''
        -> Método atalhos
        - Descrição: Responsável por implementar todos os atalhos de teclado para as funcionalidades do menu.
        
        - Parâmetros: 
            self

        - Retornos:
             - Execução das funcionalidades do menu atravéz do teclado!
        '''        
        self.txtarea.bind("<Control-n>",self.novoArquivo)
        self.txtarea.bind("<Control-o>",self.abrirArquivo)
        self.txtarea.bind("<Control-s>",self.salvar)
        self.txtarea.bind("<Control-a>",self.salvarComo)
        self.txtarea.bind("<Control-e>",self.sair)
        self.txtarea.bind("<Control-x>",self.cortar)
        self.txtarea.bind("<Control-c>",self.copiar)
        self.txtarea.bind("<Control-v>",self.colar)
        self.txtarea.bind("<Control-u>",self.desfazer)


#Criação da instância do tkinker
root = Tk()
TextEditor(root)
root.mainloop()