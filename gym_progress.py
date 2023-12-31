import requests
import customtkinter
from tkinter import *
from tkinter import Tk, Label, Entry

#Tema do sistema
customtkinter.set_appearance_mode('dark')

#Cor do sistema
customtkinter.set_default_color_theme('dark-blue')


#Janela inicial
janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title('Gym Progress')

texto_oritenção = customtkinter.CTkLabel(master=janela, text='Menu Principal', font= ('Helvetica',18))
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

#Botão progressão de carga da tela inicial
botao_progressao = customtkinter.CTkButton(janela,text='Progressão de carga', command=abre_janela_progressao)
botao_progressao.grid(column=0,row=1, padx = 5)
# Fim da Janela progressão


#Calculadora de IMC
def abre_janela_calculadora():
    janela_calculadora = customtkinter.CTk()
    janela_calculadora.geometry('500x300')
    janela_calculadora.title('Calculadora de IMC')
    texto_calculadoraimc = customtkinter.CTkLabel(master=janela_calculadora, text='Calculadora de IMC')
    texto_calculadoraimc.grid(column=0,row= 0)

    imc_idade_texto = customtkinter.CTkLabel(master=janela_calculadora, text='Idade:')
    imc_idade_texto.grid(column= 0, row=1)
    imc_idade = customtkinter.CTkEntry(master=janela_calculadora)
    imc_idade.grid(column=1, row=1)

    imc_peso_texto = customtkinter.CTkLabel(master=janela_calculadora, text='Peso:')
    imc_peso_texto.grid(column= 0, row=2)
    imc_peso = customtkinter.CTkEntry(master=janela_calculadora, placeholder_text='KG')
    imc_peso.grid(column=1, row=2)
    
    imc_altura_texto = customtkinter.CTkLabel(master=janela_calculadora, text='Altura:')
    imc_altura_texto.grid(column= 0, row=3)
    imc_altura = customtkinter.CTkEntry(master=janela_calculadora, placeholder_text='M')
    imc_altura.grid(column=1, row=3)

    imc_genero_texto = customtkinter.CTkLabel(master=janela_calculadora, text='Gênero:')
    imc_genero_texto.grid(column= 0, row= 4)
    imc_genero = customtkinter.CTkOptionMenu(master=janela_calculadora,values=['Homem', 'Mulher'])
    imc_genero.grid(column= 1, row=4)

    def calcula_imc():
        peso = float(imc_peso.get())
        altura = float(imc_altura.get())
        valor_imc = float(peso / (altura*altura))
        valor_imc_formatado_texto.configure (text=f'Seu IMC é: {valor_imc:.2f}')

        #Tabela de referência para comparação do IMC e informar o estado atual em relação ao peso do usuário

        #Tabela usuário Homem abaixo dos 65 anos 
        if round(valor_imc, 2) < 18.5:
            resultado_imc_texto.configure(text = 'Você está abaixo do Peso')
        elif round(valor_imc,2) > 18.6 and round(valor_imc,2) < 24.9:
            resultado_imc_texto.configure(text = 'Você está no Peso ideal!')
        elif round(valor_imc,2) > 25.0 and round(valor_imc,2) < 29.9:
            resultado_imc_texto.configure(text = 'Você está levemente acima do peso')
        elif round(valor_imc,2) > 30.0 and round(valor_imc,2) < 34.9:
            resultado_imc_texto.configure(text = 'Você está com Obesidade grau I')
        elif round(valor_imc,2) > 35.0 and round(valor_imc,2) < 39.9:
            resultado_imc_texto.configure(text = 'Você está com Obesidade grau II (severa)!')
        else:
            resultado_imc_texto.configure(text = 'Você está com Obesidade grau III (mórbida)!')

    


    imc_botao_calcular = customtkinter.CTkButton(master=janela_calculadora, text='Calcular IMC', command=calcula_imc)
    imc_botao_calcular.grid(column=1, row=5)
    valor_imc_formatado_texto = customtkinter.CTkLabel(master=janela_calculadora, text='')
    valor_imc_formatado_texto.grid(column=1, row=6)
    resultado_imc_texto = customtkinter.CTkLabel(master=janela_calculadora, text='')
    resultado_imc_texto.grid(column= 1, row = 7)

    janela_calculadora.mainloop()


#Botão calculadora imc da tela inicial
botao_calculadora = customtkinter.CTkButton(master=janela, text='Calculadora de IMC', command=abre_janela_calculadora, border_spacing= 5)
botao_calculadora.grid(column=2, row=1, padx = 5)







janela.mainloop()