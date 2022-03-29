#Importação de bibliotecas e módulos
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import logging

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
        self.log = logging.getLogger(__name__)
        self.log.info('Editor de Texto Inicializado!')

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
        self.log.info('Chamada da função settitle')
        '''
        -> Método Settitle
            - Descrição: Responsável por manter um título no arquivo!
            - parâmetros: 
                self: --

            - Retornos:
                self.filename: titulo da janela/arquivo
        '''
        try:
            if self.filename:
                self.log.info(f'Arquivo com título:{self.filename} gerado!')
                self.title.set(self.filename)
            else:
                self.log.info(f'Arquivo sem título gerado!')
                self.title.set('Sem título!')
        except Exception as e:
            self.log.erro(f'Erro: Função settitle: {e}')

    # Definição da funnção novo arquivo
    def novoArquivo(self,*args):
        self.log.info('Chamada da função novoArquivo!')
        '''
        -> Método novoArquivo
        - Descrição: Responsável pela criação de um novo arquivo!
        
        - Parâmetros: 
            self

        - Retornos:
             - Status com a criação de um novo arquivo

        '''
        try:
            self.txtarea.delete("1.0",END)
            self.filename = None
            self.settitle()
            self.log.info(f'Novo arquivo: {self.filename} Criado com sucesso!')
            self.status.set('Novo Arquivo Criado!')
        except Exception as e:
            self.log.erro(f'Erro: Função novoArquivo: {e}')

    # Definição abrir aquivo
    def abrirArquivo(self, *args):
        self.log.info('Chamada da função abrirArquivo!')
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
            self.log.info('Abrindo menu de procura e escolha')
            self.filename = filedialog.askopenfilename(title='Escolha um arquivo', filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            if self.filename:
                #Abrindo arquivo no modo de leitura
                self.log.info('Abrindo arquivo no modo de leitura')
                infile = open(self.filename,'r')
                
                #Limpando a area de texto
                self.txtarea.delete("1.0",END)

                #Inserindo linhas na area de texto
                for line in infile:
                    self.txtarea.insert(END,line)
                
                #Fechadno arquivo
                infile.close()
                self.log.info('Fechadno arquivo!')

                #Alterando o nome da janela
                self.settitle()

                #Atualizando o staus
                self.log.info('Arquivo Aberto com sucesso!')
                self.status.set("Arquivo aberto com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro:",e)
            self.log.error(f'Erro: Função Abrir Arquivo: {e}')

    # Definindo função de salvar
    def salvar(self, *args):
        self.log.info('Chamada da função salvar!')
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
            self.log.info('Verificando se o arquivo está vazio!')
            if self.filename:
                data = self.txtarea.get("1.0",END)

                #abrindo arquivo no modo de escrita
                outfile = open(self.filename,"w")
                self.log.info('Abrindo o arquivo no modo de escrita!')

                #Escrevendo dentro do arquivo
                outfile.write(data)
                self.log.info('Escrevendo dentro do arquivo')
                outfile.close()
                #chamando a função de título
                self.log.info('Fechando o arquivo!')
                self.settitle()

                #Atualizando o status
                self.log.info('Arquivo salvo com sucesso!')
                self.status.set("Salvo com sucesso!")
        except Exception as e:
            self.log.error(f'Função salvar: Erro:{e}!')
            messagebox.showerror("Erro:",e)
   
    # Definindo função de salvar como
    def salvarComo(self, *args):
        self.log.info('Chamada da função salvarComo!')
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
            self.log.info('Perguntando o nome e o tipo do arquivo')
            untitledfile = filedialog.asksaveasfilename(title = "Salvar Arquivo como",defaultextension=".txt",initialfile = "sem titulo.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            data = self.txtarea.get("1.0",END)

            #abrindo arquivo no modo de escrita
            self.log.info('abrindo arquivo no modo de escrita')
            outfile = open(untitledfile,"w")

            #Escrevendo dentro do arquivo
            outfile.write(data)
            self.log.info('Escrevendo dentro do arquivo')
            outfile.close()

            # Atualizando o titulo da pagina
            self.filename = untitledfile
            #chamando a função de título
            self.settitle()
            #Atualizando o status
            self.log.info('Arquivo salvo com sucesso!')
            self.status.set("Salvo com sucesso!")
        except Exception as e:
            self.log.error(f'Função salvarComo: {e}')
            messagebox.showerror("Erro:",e)

    #Definição da função sair
    def sair(self,*args):
        self.log.info('Chamada da função sair!')
        '''
        -> Método sair
        - Descrição: Responsável por sair do editor de texto
        
        - Parâmetros: 
            self

        - Retornos:
             - Fechamento do programa!
        '''
        try:
            self.log.info('Exibindo mensagem de saida!')
            op = messagebox.askyesno("ATENÇÃO",'Você deseja mesmo sair?')
            if op >0:
                self.log.info('Fechando o programa!')
                self.root.destroy()
            else:
                self.log.info('Fechando o programa!')
                return
        except Exception as e:
            self.log.erro(f'Erro: Função sair: {e}')

    #Definição da função cortar:
    def cortar(self,*args):
        self.log.info('Chamada da função cortar!')
        
        '''
        -> Método cortar
        - Descrição: Responsável por cortar textos dentro do editor de texto.
        
        - Parâmetros: 
            self

        - Retornos:
             - textos removidos da tela armazenados na memória do teclado.
        '''
        try:
            self.log.info('Texto salvo na area de transferência!')
            self.txtarea.event_generate("<<Cut>>")
        except Exception as e:
            self.log.erro(f'Erro: Função cortar: {e}')

    #Definição da função copiar:
    def copiar(self,*args):
        self.log.info('Chamada da função copiar!')
        '''
        -> Método sair
        - Descrição: Responsável por copiar palavras e frases do editor de texto.
        
        - Parâmetros: 
            self

        - Retornos:
             - textos copiados da tela armazenados na memória do teclado.
        '''
        try:
            self.log.info('Texto copiado para a area de transferência')
            self.txtarea.event_generate("<<Copy>>")
        except Exception as e:
            self.log.erro(f'Erro: Função copiar: {e}')
    #Definição da função colar:
    def colar(self,*args):
        self.log.info('Chamada da função colar!')
        '''
        -> Método colar
        - Descrição: Responsável por colar textos e frases na memória do teclado
        
        - Parâmetros: 
            self

        - Retornos:
             - textos inseridos na area de texto.
        '''
        try:
            self.log.info('Texto colado na text area!')
            self.txtarea.event_generate("<<Paste>>")
        except Exception as e:
            self.log.erro(f'Erro: Função colar: {e}')
    #Definição da função desfazer
    def desfazer(self, *args):
        self.log.info('Chamada da função desfazer!')
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
                self.log.info('Desfeito com sucesso!')
                self.status.set('Desfeito com sucesso!')
            else:
                self.txtarea.delete('1.0',END)
                self.filename = None
                self.settitle()
                self.log.info('Desfeito com sucesso!')
                self.status.set('Desfeito com sucesso!')
        except Exception as e:
            self.log.info(f'Função desfazer: ERRO: {e}')
            messagebox.showerror('Erro:',e)

    def sobre(self):
        self.log.info('Chamada da função sobre!')
        '''
        -> Método sobre
        - Descrição: Responsável por indicar ao usuário informações do desenvolvedor
        
        - Parâmetros: 
            self

        - Retornos:
             - text box com uma mensagem
        '''
        try:
            self.log.info('Abrindo caixa de dialogo!')
            messagebox.showinfo("Sobre o Text Editor","Um editor de texto simples criado com Python \n, Acesse: https://github.com/OseiasBeu/textEditor para mais! ")
        except Exception as e:
            self.log.erro(f'Erro: Função sobre: {e}')

    def atalhos(self):
        self.log.info('Chamada da função atalhos!')
        '''
        -> Método atalhos
        - Descrição: Responsável por implementar todos os atalhos de teclado para as funcionalidades do menu.
        
        - Parâmetros: 
            self

        - Retornos:
             - Execução das funcionalidades do menu atravéz do teclado!
        '''    
        try:
            self.log.info('Atalho executado com sucesso!')
            self.txtarea.bind("<Control-n>",self.novoArquivo)
            self.txtarea.bind("<Control-o>",self.abrirArquivo)
            self.txtarea.bind("<Control-s>",self.salvar)
            self.txtarea.bind("<Control-a>",self.salvarComo)
            self.txtarea.bind("<Control-e>",self.sair)
            self.txtarea.bind("<Control-x>",self.cortar)
            self.txtarea.bind("<Control-c>",self.copiar)
            self.txtarea.bind("<Control-v>",self.colar)
            self.txtarea.bind("<Control-u>",self.desfazer)
        except Exception as e:
            self.log.erro(f'Erro: Função atalhos: {e}')



if __name__ == '__main__':
    #Criação da instância do tkinker
    LOG_FILENAME = './logs/textEditor.log'
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        filename = LOG_FILENAME,
        format=FORMAT,
        level=logging.INFO,
        filemode ='a+',
        encoding='UTF-8'
    )

    root = Tk()
    TextEditor(root)
    root.mainloop()