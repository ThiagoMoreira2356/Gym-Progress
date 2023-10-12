import requests
from tkinter import *
from tkinter import Tk, Label, Entry

"""  INICIO DO LOGIN
#logins
usuario_cadastrado = 'admin' 
senha_cadastrada = 'admin'
usuario = input('Usuário:')
senha = input('Senha:')


#Login
if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print('Login efetuado com sucessso')
else:
    print('Usuário e senha inválidos')


#Menu
print('Bem vindo ao gym progress!')
print('[1]Progressão de carga')
menu_inicial = int(input('Digite uma opção:'))

FINAL DO LOGIN  """


#Janela inicial
janela = Tk()
janela.geometry("500x300")
janela.title('Gym Progress')

texto_oritenção = Label(janela, text='Menu', )
texto_oritenção.grid(column=0,row=0)


#Progressão de carga
def abre_janela_progressao():
    janela_progressao = Tk()
    janela_progressao.geometry("500x300")
    janela_progressao.title('Progressão de carga')

    texto_prog_carga = Label(janela_progressao, text='Qual foi sua última carga?')
    texto_prog_carga.grid(column=0 ,row=0)

    ultimo_peso = Entry(janela_progressao)
    ultimo_peso.grid(column=0,row=1 )
 
    def obter_ultimo_peso():
        try:
            peso = float(ultimo_peso.get())
            peso_sugerido = peso + (peso * 0.2)
            carga_sugerida_texto.config (text=f'Carga sugerida: {peso_sugerido} kg')
        except ValueError:
            carga_sugerida_texto.config(text='Digite um número válido')

    botao_entra_prog_valor = Label(janela_progressao, text='Sugerir próxima carga')
    botao_entra_prog_valor.grid(column=0,row=2)
    botao_entra_prog_valor.bind('<Button-1>', lambda event=None: obter_ultimo_peso())
    
    carga_sugerida_texto = Label(janela_progressao, text="")
    carga_sugerida_texto.grid(column=0, row=3)
    janela_progressao.mainloop()
botao_progressao = Button(janela,text='Progressão de carga', command=abre_janela_progressao)
botao_progressao.grid(column=0,row=1)
# Fim da Janela progressão







janela.mainloop()