# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


# tkinter
from tkinter import Tk, Frame, Label, Button, Entry, StringVar, messagebox
from tkinter.ttk import Style, Separator, Combobox

# re
from re import fullmatch


# -------------------------------------------------------------------------- #
# CORES E CONSTANTES


COLOR1 = '#feffff'  # Branco
COLOR2 = '#403d3d'  # Cinza Escuro??
COLOR3 = '#e89613'  # Laranja
COLOR4 = '#808080'  # Cinza
COLOR5 = '#0d9618'  # Verde


# Padrão para números
NUMBER_PATTERN = r'^\d+$'


# -------------------------------------------------------------------------- #
# FUNÇÕES


def convert(unit, number):
    """Cuida das conversões."""

    # Validamos o input
    if number == '':
        messagebox.showerror(
            'Erro',
            'Tem que inserir número para converter'
        )
        return

    if fullmatch(NUMBER_PATTERN, number) is None:
        messagebox.showerror('Erro', 'Aceita apenas digitos')
        return

    # Temos que saber a base.
    # unit[0] == 'B' de Binário, 'O' de Octal etc..
    if unit[0] == 'B':
        base = 2
    elif unit[0] == 'O':
        base = 8
    elif unit[0] == 'D':
        base = 10
    else:
        base = 16

    # Preenchemos os labels
    binary_number_label['text'] = f'{bin(int(number, base))[2:]}'
    octal_number_label['text'] = f'{oct(int(number, base))[2:]}'
    decimal_number_label['text'] = f'{int(number, base)}'
    hexadecimal_number_label['text'] = f'{hex(int(number, base))[2:].upper()}'


# -------------------------------------------------------------------------- #
# JANELA


window = Tk()
window.title('')
window.geometry('400x310')
window.resizable(False, False)
window.configure(bg=COLOR2)


style = Style(window)
style.theme_use('clam')

Separator(
    window,
    orient='horizontal'
).grid(
    row=0,
    columnspan=1,
    ipadx=190
)


# -------------------------------------------------------------------------- #
# FRAMES


title_frame = Frame(window, width=400, height=50, bg=COLOR2)
title_frame.grid(row=1, column=0, sticky='nsew', pady=10)

operation_frame = Frame(window, width=400, height=260, bg=COLOR2)
operation_frame.grid(row=2, column=0, sticky='nsew', pady=10)


# -------------------------------------------------------------------------- #
# CONFIGURANDO TITLE_FRAME


title_label = Label(
    title_frame, text='Conversor de base numérica',
    font=('Roboto 22 bold'), anchor='center',
    justify='center', bg=COLOR2, fg=COLOR1,
)
title_label.place(x=10, y=10)


# -------------------------------------------------------------------------- #
# CONFIGURANDO OPERATION_FRAME


unit = StringVar()
unit_combo = Combobox(
    operation_frame, width=11,
    font=('Roboto 12'),
    values=(
        'Binário', 'Octal',
        'Decimal', 'Hexadecimal'
    ), textvariable=unit
)
unit_combo.set('Binário')
unit_combo.place(x=25, y=0)

number_entry = Entry(
    operation_frame, width=11,
    font=('Roboto 13'), relief='flat',
    bd=0, borderwidth=0
)
number_entry.place(x=150, y=0)

convert_button = Button(
    operation_frame, width=11, text='Converter',
    font=('Roboto 9 bold'), relief='raised', bg=COLOR5, fg=COLOR1,
    anchor='center', justify='center', overrelief='ridge',
    bd=0, borderwidth=0, activebackground=COLOR5,
    activeforeground=COLOR1, command=lambda: convert(
        unit.get(),
        number_entry.get()
    )
)
convert_button.place(x=270, y=0)

# Binário
binary_label = Label(
    operation_frame, text='BINÁRIO',
    width=14, font=('Roboto 12'),
    anchor='nw', justify='left',
    bg=COLOR3, fg=COLOR1
)
binary_label.place(x=25, y=60)

binary_number_label = Label(
    operation_frame, text='',
    width=23, font=('Roboto 12'),
    anchor='center', justify='center',
    bg=COLOR4, fg=COLOR1
)
binary_number_label.place(x=160, y=60)

# Octal
octal_label = Label(
    operation_frame, text='OCTAL',
    width=14, font=('Roboto 12'),
    anchor='nw', justify='left',
    bg=COLOR3, fg=COLOR1
)
octal_label.place(x=25, y=100)

octal_number_label = Label(
    operation_frame, text='',
    width=23, font=('Roboto 12'),
    anchor='center', justify='center',
    bg=COLOR4, fg=COLOR1
)
octal_number_label.place(x=160, y=100)

# Decimal
decimal_label = Label(
    operation_frame, text='DECIMAL',
    width=14, font=('Roboto 12'),
    anchor='nw', justify='left',
    bg=COLOR3, fg=COLOR1
)
decimal_label.place(x=25, y=140)

decimal_number_label = Label(
    operation_frame, text='',
    width=23, font=('Roboto 12'),
    anchor='center', justify='center',
    bg=COLOR4, fg=COLOR1
)
decimal_number_label.place(x=160, y=140)

# Hexadecimal
hexadecimal_label = Label(
    operation_frame, text='HEXADECIMAL',
    width=14, font=('Roboto 12'),
    anchor='nw', justify='left',
    bg=COLOR3, fg=COLOR1
)
hexadecimal_label.place(x=25, y=180)

hexadecimal_number_label = Label(
    operation_frame, text='',
    width=23, font=('Roboto 12'),
    anchor='center', justify='center',
    bg=COLOR4, fg=COLOR1
)
hexadecimal_number_label.place(x=160, y=180)


# -------------------------------------------------------------------------- #
# LOOP


window.mainloop()


# -------------------------------------------------------------------------- #
