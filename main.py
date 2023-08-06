from customtkinter import *
from tkinter import END, ttk, messagebox

root = CTk()
root.geometry('650x500')
root.resizable(False, False)
root.title('Meu IMC')
root.iconbitmap('icone.ico')

frame = CTkFrame(root, width=650, height=500, fg_color='#e2f4f9')
frame.pack()


def calcular():
    try:
        meupeso = float(pesoentry.get())
        minhaaltura = float(alturaentry.get())
        resu = meupeso / (minhaaltura ** 2)
        if resu < 18.5:
            resulabel.configure(root, text=f'Seu IMC é {resu * 10000:.2f}')
            alturaentry.delete(0, END)
            pesoentry.delete(0, END)
            resulabel.focus()
        if resu < 24.9:
            resulabel.configure(root, text=f'Seu IMC é {resu * 10000:.2f}')
            alturaentry.delete(0, END)
            pesoentry.delete(0, END)
            resulabel.focus()
        elif resu < 29.9:
            resulabel.configure(root, text=f'Seu IMC é {resu * 10000:.2f}')
            alturaentry.delete(0, END)
            pesoentry.delete(0, END)
            resulabel.focus()
        elif resu <= 40:
            resulabel.configure(root, text=f'Seu IMC é {resu * 10000:.2f}')
        else:
            resulabel.configure(root, text=f'Seu IMC é {resu * 10000:.2f}')
    except ValueError:
        messagebox.showerror(title='Erro!', message='Todos os campos devem ser'
                                                    ' preenchidos com valores'
                                                    ' numéricos')


resulabel = CTkLabel(root, text='', font=('Arial', 18, 'bold'),
                     fg_color='#e2f4f9', text_color='#09671f',
                     bg_color='#e2f4f9')
resulabel.place(relx=0.39, rely=0.54)


conceito = CTkLabel(root, text='O IMC (Índice de Massa Corporal) é uma '
                               'medida que calcula a relação entre\n o peso e '
                               'a altura de uma pessoa, com o objetivo de '
                               'determinar\n se ela está dentro de faixas '
                               'consideradas saudáveis.',
                    font=('Arial', 15, 'bold'),
                    fg_color='#e2f4f9',
                    text_color='#003d58')
conceito.place(relx=0.08, rely=0.045)

altura = CTkLabel(root, text='Sua Altura', font=('Arial', 15, 'bold'),
                  fg_color='#e2f4f9', text_color='#003d58')
altura.place(relx=0.35, rely=0.2)

alturaentry = CTkEntry(root, width=70, justify='center',
                       placeholder_text='ex: 170', fg_color='#e2f4f9',
                       font=('Arial', 15, 'bold'),
                       text_color='#09671f')
alturaentry.place(relx=0.35, rely=0.27)

peso = CTkLabel(root, text='Seu Peso', font=('Arial', 15, 'bold'),
                fg_color='#e2f4f9', text_color='#003d58')
peso.place(relx=0.53, rely=0.2)

pesoentry = CTkEntry(root, width=70, justify='center',
                     placeholder_text='ex: 70', font=('Arial', 15, 'bold'),
                     fg_color='#e2f4f9',
                     text_color='#09671f')
pesoentry.place(relx=0.53, rely=0.27)

botao = CTkButton(root, text='Calcular IMC', font=('Arial', 15, 'bold'),
                  fg_color='#52b4ff', text_color='#003d58', bg_color='white',
                  hover_color='#87CEFA', command=calcular)
botao.place(relx=0.39, rely=0.4)

# Criação da lista de dados para inserir na tabela
dados_da_tabela = [
                   ['Menor que 18.5', 'Abaixo do peso', '0'],
                   ['Entre 18.5 e 24.9', 'Peso Ideal', '0'],
                   ['Entre 25.0 e 29.9', 'Sobrepeso', 'I'],
                   ['Entre 30 e 39.9', 'Obesidade', 'II'],
                   ['Maior que 40.0', 'Obesidade Mórbida', 'III']
                  ]

# Criação da tabela
tabela = ttk.Treeview(root, height=5,
                      columns=('coluna1', 'coluna2', 'coluna3'),
                      show='headings')

# Tamanho das colunas
tabela.column('coluna1', width=140, minwidth=140, anchor='center')
tabela.column('coluna2', width=140, minwidth=140, anchor='center')
tabela.column('coluna3', width=150, minwidth=150, anchor='center')

# Cabeçalho das colunas
tabela.heading('coluna1', text='IMC')
tabela.heading('coluna2', text='Classificação')
tabela.heading('coluna3', text='Obesidade (Grau)')

# Estilo do cabeçalho das colunas
estilo = ttk.Style(root)
estilo.configure('Treeview.Heading', font=('Arial', 13, 'bold'),
                 foreground='#003d58')

# Estilo dos itens da tabela
estilo.configure('Treeview', font=('Arial', 11), foreground='#003d58',
                 background='#e2f4f9')

# Inserção da lista dados_da_tabela na tabela
for (imc, classif, obesid) in dados_da_tabela:
    tabela.insert('', 'end', values=(imc, classif, obesid))

tabela.place(relx=0.17, rely=0.68)

root.mainloop()