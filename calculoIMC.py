## Calculo IMC
#teste1 
#importando biblioteca
from tkinter import *
from tkinter import ttk


#cores para o app

co0 = '#ffffff' #branco
co1 = '#444466' #preto
co2 = '#4065a1' #azul

# cores teste 
#co1 = '#11948C' #verde escuro
#co2 = '#57FFF4' #verde claro

#co1 = '#7A694E' #cinza
#co2 = '#4CA3FC' #azul

# janela

janela = Tk()
janela.title('IMC')
janela.geometry('450x350')
janela.configure(bg='white')

# ------ dividindo a janela em duas partes ------

frame_cima= Frame(janela, width=295,height=50,bg='white',pady=0,padx=0,relief='flat')
frame_cima.grid(row=0,column=0,sticky=NSEW)

frame_baixo= Frame(janela, width=295,height=180,bg='white',pady=0,padx=0,relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NSEW)


# ------ Configurando frame cima ------


app_nome = Label(frame_cima,text='Calculadora IMC',width=35,height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'),bg=co0,fg=co1)
app_nome.place (x=0, y=0) 

app_linha = Label(frame_cima,text='',width=450,height=1, padx=5, relief='flat', anchor='center', font=('Ivy 1'),bg=co2,fg=co1)
app_linha.place (x=0, y=35) 

# Função calculos

def calcular():

    peso = float(e_peso.get())
    altura = float (e_altura.get())
    
    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = 'Você está abaixo do peso'
        
    elif resultado >=18.5 and resultado < 25:
        l_resultado_texto['text'] = 'Seu IMC está normal'
        
    elif resultado >= 25 and resultado < 30:
        l_resultado_texto['text'] = 'Você está acima do peso.'
        
    else:         
        l_resultado_texto['text'] = 'Obesidade'

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

    
    
# ------ configurando frame baixo ------

l_usuario = Label(frame_baixo,text='Insira seu nome', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'),bg=co0,fg=co1)
l_usuario.grid(row=0,column=0, sticky=NSEW, pady=10, padx=3) 
e_usuario = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_usuario.grid(row=0,column=1, sticky=NSEW, pady=10, padx=3)

l_peso = Label(frame_baixo,text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'),bg=co0,fg=co1)
l_peso.grid(row=2,column=0, sticky=NSEW, pady=10, padx=3) 
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=2,column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo,text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'),bg=co0,fg=co1)
l_altura.grid(row=3,column=0, sticky=NSEW, pady=10, padx=35) 
e_altura = Entry(frame_baixo, width=15, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=3,column=1, sticky=NSEW, pady=10, padx=3)

#############
l_resultado = Label(frame_baixo,text='---',width=5, height=1, padx=6,pady=32, relief='flat', anchor='center', font=('Ivy 24 bold'),bg=co2,fg=co0)
l_resultado.place(x=330, y=10)

l_resultado_texto = Label(frame_baixo,text='',width=53, height=1, padx=0,pady=50, relief='flat', anchor='center', font=('Ivy 10 bold'),bg=co0,fg=co1)
l_resultado_texto.place(x=0, y=120)

l_enviar_texto = Label(frame_baixo,text='click aqui para exportar',width=53, height=1, padx=0,pady=50, relief='flat', anchor='center', font=('Ivy 10 bold'),bg=co0,fg=co1)
l_enviar_texto.place(x=0, y=200)

b_calcular = Button(frame_baixo, command= calcular,text='Calcular',width=53, height=1,overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'),bg=co2,fg=co0)
b_calcular.grid(row=4,column=0, sticky=NSEW, pady=80, padx=5, columnspan=30)



janela.mainloop()
