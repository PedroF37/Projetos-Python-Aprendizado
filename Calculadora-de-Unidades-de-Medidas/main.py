# --------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Frame, Label, Button, Entry, PhotoImage
from tkinter.ttk import Style, Combobox


# --------------------------------------------------------------------------- #
# CONSTANTES


COLOR1 = '#3b3b3b'  # preto? / cinza?
COLOR2 = '#000000'  # preto
COLOR3 = '#ffffff'  # branco
COLOR4 = '#48b3e0'  # azul claro
COLOR5 = '#EEBE0C'  # amarelo

units = {
    'massa': [
        {'kg': 1000},
        {'hg': 100},
        {'dag': 10},
        {'g': 1},
        {'dg': 0.1},
        {'cg': 0.01},
        {'mg': 0.001}
    ],

    'comprimento': [
        {'km': 1000},
        {'hm': 100},
        {'dam': 10},
        {'m': 1},
        {'dm': 0.1},
        {'cm': 0.01},
        {'mm': 0.001}
    ]
}


# --------------------------------------------------------------------------- #
# FUNÇÕES


def show_menu(item):
    """Trata do output frame."""
    from_unit = []
    to_unit = []
    values_unit = []

    for measure in units[item]:
        for key, value in measure.items():
            from_unit.append(key)
            to_unit.append(key)
            values_unit.append(value)

    from_combobox['values'] = from_unit
    to_combobox['values'] = to_unit

    output_label['text'] = item.title()

    # Label, botão e entrada de dados
    number_label = Label(
        output_frame, text='Digite o número abaixo',
        width=17, height=2, padx=5, pady=3,
        relief='flat', anchor='center',
        font=('Carlito 10 bold'),
        bg=COLOR3, fg=COLOR2
    )
    number_label.place(x=40, y=150)

    number_entry = Entry(
        output_frame, width=9,
        font=('Carlito 15 bold'),
        justify='center',
        relief='solid'
    )
    number_entry.place(x=10, y=190)

    caluculate_button = Button(
        output_frame, text='Calcular', width=10, height=1,
        relief='raised', anchor='center', overrelief='ridge',
        font=('Carlito 10 bold'), bg=COLOR5, fg=COLOR2,
        activebackground=COLOR5, activeforeground=COLOR2,
        command=lambda: calculate(
            from_combobox.get(),
            to_combobox.get(),
            float(number_entry.get()),
            from_unit, to_unit,
            result_label
        )
    )
    caluculate_button.place(x=120, y=190)

    result_label = Label(
        output_frame, text='00000000',
        width=18, height=1, pady=3,
        relief='groove', anchor='center',
        font=('Carlito 18 bold'),
        bg=COLOR3, fg=COLOR2
    )
    result_label.place(x=10, y=240)


def calculate(from_value, to_value, number, from_list, to_list, result_label):
    """Calcula as conversões"""
    distance = to_list.index(to_value) - from_list.index(from_value)

    # Multiplicação
    if to_list.index(from_value) <= from_list.index(to_value):
        # Verifica a posição das unidades para pegar
        # o valor da diferença
        distance = to_list.index(to_value) - from_list.index(from_value)
        result = number * (10 ** distance)
        result_label['text'] = result
    else:
        distance = from_list.index(from_value) - to_list.index(to_value)
        result = number * (10 ** distance)
        result_label['text'] = result

     # Divisão
    if to_list.index(from_value) > from_list.index(to_value):
        if to_list.index(from_value) <= from_list.index(to_value):
            # Verifica a posição das unidades para pegar
            # o valor da diferença
            distance = from_list.index(from_value) - to_list.index(to_value)
            result = number / (10 ** distance)
            result_label['text'] = result
        else:
            distance = from_list.index(from_value) - to_list.index(to_value)
            result = number / (10 ** distance)
            result_label['text'] = result


# --------------------------------------------------------------------------- #
# JANELA PRINCIPAL


window = Tk()
window.title('')
window.geometry('750x300')
window.resizable(0, 0)  # ou: (False, False)
window.configure(bg=COLOR1)


# --------------------------------------------------------------------------- #
# FRAMES


title_frame = Frame(
    window, width=500, height=75,
    bg=COLOR3, pady=0, padx=3, relief='flat'
)
title_frame.place(x=2, y=2)

options_frame = Frame(
    window, width=500, height=225,
    bg=COLOR3, pady=0, padx=3, relief='flat'
)
options_frame.place(x=2, y=80)

output_frame = Frame(
    window, width=244, height=300,
    bg=COLOR3, pady=0, padx=3, relief='flat'
)
output_frame.place(x=505, y=2)

# Estilo da janela
style = Style(window)
style.theme_use('clam')


# --------------------------------------------------------------------------- #
# LABELS


title_label = Label(
    title_frame, text='Calculadora de Unidades de Medidas',
    height=1, padx=0, relief='flat', anchor='center',
    font=('Carlito 15 bold'), bg=COLOR3, fg=COLOR4
)
title_label.place(x=65, y=25)

output_label = Label(
    output_frame, text='---', height=3, width=25,
    padx=0, pady=3, relief='groove', anchor='center',
    font=('Carlito 15 bold'), bg=COLOR3, fg=COLOR2
)
output_label.place(x=0, y=0)

from_label = Label(
    output_frame, text='De', height=1,
    padx=3, relief='groove', anchor='center',
    font=('Carlito 12 bold'), bg=COLOR3, fg=COLOR2
)
from_label.place(x=15, y=95)

to_label = Label(
    output_frame, text='Para', height=1,
    padx=3, relief='groove', anchor='center',
    font=('Carlito 12 bold'), bg=COLOR3, fg=COLOR2
)
to_label.place(x=110, y=95)


# --------------------------------------------------------------------------- #
# COMBOBOX


from_combobox = Combobox(
    output_frame, width=5,
    justify=('center'), font=('Carlito 10 bold')
)
from_combobox.place(x=43, y=95)

to_combobox = Combobox(
    output_frame, width=5,
    justify=('center'), font=('Carlito 10 bold')
)
to_combobox.place(x=150, y=95)

# --------------------------------------------------------------------------- #
# BOTÕES


# Botão Massa
button1_image = PhotoImage(file='imagens/weight.png')
button1 = Button(
    options_frame, text='Massa', width=125, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button1_image, compound='left',
    command=lambda: show_menu('massa')
)
button1.grid(row=0, column=0, sticky='nsew', pady=5, padx=5)

# Botão Tempo
button2_image = PhotoImage(file='imagens/time.png')
button2 = Button(
    options_frame, text='Tempo', width=125, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button2_image, compound='left',
    # command=lambda: show_menu('tempo')
)
button2.grid(row=0, column=1, sticky='nsew', pady=5, padx=5)

# Botão Comprimento
button3_image = PhotoImage(file='imagens/length.png')
button3 = Button(
    options_frame, text='Comprimento', width=125, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button3_image, compound='left',
    command=lambda: show_menu('comprimento')
)
button3.grid(row=0, column=2, sticky='nsew', pady=5, padx=5)

# Botão Area
button4_image = PhotoImage(file='imagens/square.png')
button4 = Button(
    options_frame, text='Area', width=125, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button4_image, compound='left',
    # command=lambda: show_menu('area')
)
button4.grid(row=1, column=0, sticky='nsew', pady=5, padx=5)

# Botão Quantidade
button5_image = PhotoImage(file='imagens/volume.png')
button5 = Button(
    options_frame, text='Quantidade', width=125, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button5_image, compound='left',
    # command=lambda: show_menu('quantidade')
)
button5.grid(row=1, column=1, sticky='nsew', pady=5, padx=5)

# Botão Velocidade
button6_image = PhotoImage(file='imagens/speed.png')
button6 = Button(
    options_frame, text='Velocidade', width=125, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button6_image, compound='left',
    # command=lambda: show_menu('velocidade')
)
button6.grid(row=1, column=2, sticky='nsew', pady=5, padx=5)

# Botão Temperatura
button7_image = PhotoImage(file='imagens/temperature.png')
button7 = Button(
    options_frame, text='Temperatura', width=125, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button7_image, compound='left',
    # command=lambda: show_menu('temperatura')
)
button7.grid(row=2, column=0, sticky='nsew', pady=5, padx=5)

# Botão Energia
button8_image = PhotoImage(file='imagens/energy.png')
button8 = Button(
    options_frame, text='Energia', width=127, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button8_image, compound='left',
    # command=lambda: show_menu('energia')
)
button8.grid(row=2, column=1, sticky='nsew', pady=5, padx=5)

# Botão Pressão
button9_image = PhotoImage(file='imagens/pressure.png')
button9 = Button(
    options_frame, text='Pressao', width=127, height=50,
    relief='flat', anchor='nw', overrelief='solid',
    font=('Carlito 10 bold'), bg=COLOR4, fg=COLOR2,
    activebackground=COLOR4, activeforeground=COLOR2,
    image=button9_image, compound='left',
    # command=lambda: show_menu('pressao')
)
button9.grid(row=2, column=2, sticky='nsew', pady=5, padx=5)


# --------------------------------------------------------------------------- #
# LOOP PRINCIPAL


window.mainloop()
