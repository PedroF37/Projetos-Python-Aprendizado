# --------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Frame, Label, Button, Entry, messagebox
from tkinter.ttk import Style, Scrollbar, Treeview
from tkcalendar import DateEntry
from view import show_all, insert_data, update_data, delete_data


# --------------------------------------------------------------------------- #
# CONSTANTES E GLOBAIS

COLOR0 = "#f0f3f5"  # Branco
COLOR1 = "#feffff"  # Branco
COLOR2 = "#4fa882"  # Verde
COLOR3 = "#38576b"  # Valor
COLOR4 = "#403d3d"  # Letra
COLOR5 = "#e06636"  # - Profit
COLOR6 = "#038cfc"  # Azul
COLOR7 = "#ef5350"  # Vermelho
COLOR8 = "#263238"  # + verde
COLOR9 = "#e9edf5"  # Sky Blue?? Branco kk

global tree


# --------------------------------------------------------------------------- #
# FUNÇÕES


def show_table():
    """Função para mostrar dados da tabela."""
    global tree
    datalist = show_all()

    # Cabeçalho para a tabela
    table_header = [
        'ID', 'Nome',
        'email', 'telefone',
        'Data', 'Estado', 'Sobre'
    ]

    tree = Treeview(
        output_frame, selectmode='extended',
        columns=table_header, show='headings'
    )

    # Vertical Scrollbar
    vsb = Scrollbar(output_frame, orient='vertical', command=tree.yview)

    # Horizontal Scrollbar
    hsb = Scrollbar(output_frame, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    output_frame.grid_rowconfigure(0, weight=12)

    hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'center', 'center']
    h = [30, 170, 140, 100, 120, 50, 100]
    n = 0

    for col in table_header:
        tree.heading(col, text=col.title(), anchor='center')
        # Ajusta a largura da coluna para a string no header
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in datalist:
        tree.insert('', 'end', value=item)


def insert():
    """Função que pega os valores para inserir na tabela."""
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    date = date_entry.get()
    state = state_entry.get()
    extra_info = extra_info_entry.get()

    data = [name, email, phone, date, state, extra_info]

    if name == '':
        messagebox.showerror('Erro', 'O nome não pode ser vazio.')
    else:
        insert_data(data)
        messagebox.showinfo('Sucesso', 'Informações inseridas com sucesso.')

        # Limpa os campos depois dos dados serem inseridos.
        name_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        date_entry.delete(0, 'end')
        state_entry.delete(0, 'end')
        extra_info_entry.delete(0, 'end')

    for info in output_frame.winfo_children():
        info.destroy()

    show_table()


def update():
    """Função que atualiza os dados."""
    global tree
    try:
        tree_data = tree.focus()
        tree_dict = tree.item(tree_data)
        tree_list = tree_dict['values']

        # O id
        value = tree_list[0]

        name_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        date_entry.delete(0, 'end')
        state_entry.delete(0, 'end')
        extra_info_entry.delete(0, 'end')

        name_entry.insert(0, tree_list[1])
        email_entry.insert(0, tree_list[2])
        phone_entry.insert(0, tree_list[3])
        date_entry.insert(0, tree_list[4])
        state_entry.insert(0, tree_list[5])
        extra_info_entry.insert(0, tree_list[6])

        def update_record():
            name = name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            date = date_entry.get()
            state = state_entry.get()
            extra_info = extra_info_entry.get()

            data = [name, email, phone, date, state, extra_info, value]

            if name == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio.')
            else:
                update_data(data)
                messagebox.showinfo(
                    'Sucesso', 'Dados atualizados com sucesso.'
                )

                # Limpa os campos depois dos dados serem inseridos.
                name_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                phone_entry.delete(0, 'end')
                date_entry.delete(0, 'end')
                state_entry.delete(0, 'end')
                extra_info_entry.delete(0, 'end')

                for info in output_frame.winfo_children():
                    info.destroy()

                show_table()
                confirmation_button.destroy()

        confirmation_button = Button(
            input_frame, text='Confirmar', width=10,
            bg=COLOR2, fg=COLOR1, font=('Roboto 8 bold'),
            anchor='center', relief='raised', overrelief='ridge',
            activebackground=COLOR2, activeforeground=COLOR1,
            command=update_record
        )
        confirmation_button.place(x=113, y=390)


    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma entrada para atualizar.')


def delete():
    """Função que deleta dados na tabela."""
    global tree
    try:
        tree_data = tree.focus()
        tree_dict = tree.item(tree_data)
        tree_list = tree_dict['values']

        # O id
        value = [tree_list[0]]  # ou: str(tree_list[0])

        delete_data(value)
        messagebox.showinfo('Sucesso', 'Dados deletados com sucesso.')

        for info in output_frame.winfo_children():
            info.destroy()

        show_table()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione uma entrada para deletar.')


# --------------------------------------------------------------------------- #
# JANELA


window = Tk()
window.title('')
window.resizable(0, 0)

style = Style(window)
style.theme_use('clam')


# --------------------------------------------------------------------------- #
# FRAMES


title_frame = Frame(
    window, width=320, height=60,
    bg=COLOR2, relief='flat'
)
title_frame.grid(row=0, column=0, sticky='nsew')

input_frame = Frame(
    window, width=320, height=420,
    bg=COLOR1, relief='flat'
)
input_frame.grid(row=1, column=0, sticky='nsew', padx=0, pady=1)

output_frame = Frame(
    window, width=800, height=420,
    bg=COLOR1, relief='flat'
)
output_frame.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky='nsew')


# --------------------------------------------------------------------------- #
# LABELS


title_label = Label(
    title_frame, text='Formulário de Consultoria',
    bg=COLOR2, fg=COLOR1, font=('Roboto 13 bold'),
    anchor='center', justify='center', relief='flat'
)
title_label.place(x=35, y=15)

name_input_label = Label(
    input_frame, text='Nome *',
    bg=COLOR1, fg=COLOR4, font=('Roboto 10 bold'),
    anchor='nw', relief='flat'
)
name_input_label.place(x=5, y=10)

email_input_label = Label(
    input_frame, text='email *',
    bg=COLOR1, fg=COLOR4, font=('Roboto 10 bold'),
    anchor='nw', relief='flat'
)
email_input_label.place(x=5, y=80)

phone_input_label = Label(
    input_frame, text='Telefone *',
    bg=COLOR1, fg=COLOR4, font=('Roboto 10 bold'),
    anchor='nw', relief='flat'
)
phone_input_label.place(x=5, y=150)

date_input_label = Label(
    input_frame, text='Data da Consulta *',
    bg=COLOR1, fg=COLOR4, font=('Roboto 10 bold'),
    anchor='nw', relief='flat'
)
date_input_label.place(x=7, y=220)

state_input_label = Label(
    input_frame, text='Estado da Consulta *',
    bg=COLOR1, fg=COLOR4, font=('Roboto 10 bold'),
    anchor='nw', relief='flat'
)
state_input_label.place(x=180, y=220)

extra_info_input_label = Label(
    input_frame, text='Informação extra',
    bg=COLOR1, fg=COLOR4, font=('Roboto 10 bold'),
    anchor='nw', relief='flat'
)
extra_info_input_label.place(x=5, y=290)


# --------------------------------------------------------------------------- #
# ENTRIES


name_entry = Entry(input_frame, width=33, justify='left', relief='solid')
name_entry.place(x=7, y=40)

email_entry = Entry(input_frame, width=33, justify='left', relief='solid')
email_entry.place(x=7, y=110)

phone_entry = Entry(input_frame, width=33, justify='left', relief='solid')
phone_entry.place(x=7, y=180)

date_entry = DateEntry(
    input_frame, width=12,
    background='darkgray',
    foreground='white', borderwidth=2,
    year=2022
)
date_entry.place(x=7, y=250)

state_entry = Entry(input_frame, width=13, justify='left', relief='solid')
state_entry.place(x=180, y=250)

extra_info_entry = Entry(
    input_frame, width=33,
    justify='left', relief='solid'
)
extra_info_entry.place(x=7, y=320)


# --------------------------------------------------------------------------- #
# BOTÕES


insert_button = Button(
    input_frame, text='Inserir', width=10,
    bg=COLOR6, fg=COLOR1, font=('Roboto 8 bold'),
    anchor='center', relief='raised', overrelief='ridge',
    activebackground=COLOR6, activeforeground=COLOR1,
    command=insert
)
insert_button.place(x=7, y=360)

update_button = Button(
    input_frame, text='Atualizar', width=10,
    bg=COLOR2, fg=COLOR1, font=('Roboto 8 bold'),
    anchor='center', relief='raised', overrelief='ridge',
    activebackground=COLOR2, activeforeground=COLOR1,
    command=update
)
update_button.place(x=113, y=360)

delete_button = Button(
    input_frame, text='Deletar', width=10,
    bg=COLOR7, fg=COLOR1, font=('Roboto 8 bold'),
    anchor='center', relief='raised', overrelief='ridge',
    activebackground=COLOR7, activeforeground=COLOR1,
    command=delete
)
delete_button.place(x=221, y=360)


# --------------------------------------------------------------------------- #
# LOOP

show_table()
window.mainloop()
