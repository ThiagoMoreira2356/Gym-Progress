import requests
import customtkinter
from tkinter import *
from tkinter import Tk, Label, Entry

#Tema do sistema
customtkinter.set_appearance_mode('dark')

#Cor do sistema
customtkinter.set_default_color_theme('dark-blue')


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
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title('Gym Progress')

texto_oritenção = customtkinter.CTkLabel(master=janela, text='Menu Principal')
texto_oritenção.grid(column=0,row=0)


#Progressão de carga
def abre_janela_progressao():
    janela_progressao = customtkinter.CTk()
    janela_progressao.geometry("500x300")
    janela_progressao.title('Progressão de carga')

    texto_prog_carga = customtkinter.CTkLabel(master=janela_progressao, text='Qual foi sua última carga?')
    texto_prog_carga.grid(column=0 ,row=0)

    ultimo_peso = customtkinter.CTkEntry(master=janela_progressao, placeholder_text='KG')
    ultimo_peso.grid(column=0,row=1 )
 
    def obter_ultimo_peso():
        try:
            peso = float(ultimo_peso.get())
            peso_sugerido = peso + (peso * 0.2)
            carga_sugerida_texto.configure (text=f'Carga sugerida: {peso_sugerido} kg')
        except ValueError:
            carga_sugerida_texto.configure(text='Digite um número válido')

    botao_entra_prog_valor = customtkinter.CTkButton(master=janela_progressao,text='Calcular próxima carga', command= obter_ultimo_peso)
    botao_entra_prog_valor.grid(column=0,row=2)
    
    carga_sugerida_texto = customtkinter.CTkLabel(master=janela_progressao, text="")
    carga_sugerida_texto.grid(column=0, row=3)
    janela_progressao.mainloop()

botao_progressao = customtkinter.CTkButton(janela,text='Progressão de carga', command=abre_janela_progressao)
botao_progressao.grid(column=0,row=1)
# Fim da Janela progressão







janela.mainloop()