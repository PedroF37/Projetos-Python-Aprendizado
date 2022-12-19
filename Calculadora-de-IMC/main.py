# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Label, Frame, Button, Entry


# ---------------------------------------------------------------------------#
# CONSTANTES


COLOR0 = '#ffffff'  # Branco
COLOR1 = '#444466'  # Roxo?
COLOR2 = '#4065a1'  # Azul


# -------------------------------------------------------------------------- #
# FUNÇÕES


def calculate(weight, height):
    """Calcula o IMC e mostra no label."""
    result_imc = weight / height ** 2

    if result_imc < 18.5:
        imc = 'Abaixo do peso'
    elif result_imc < 25:
        imc = 'Normal'
    elif result_imc < 30:
        imc = 'Sobrepeso'
    else:
        imc = 'Obesedade'

    result_label['text'] = f'{result_imc:.2f}'
    imc_label['text'] = f'O seu IMC é: {imc}'


# -------------------------------------------------------------------------- #
# JANELA PRINCIPAL


window = Tk()
window.title('')
window.geometry('295x230')
window.resizable(0, 0)
window.configure(bg=COLOR0)


# -------------------------------------------------------------------------- #
# FRAMES


upper_frame = Frame(
    window, width=295, height=50,
    bg=COLOR0, pady=0, padx=0, relief='flat'
)
upper_frame.grid(row=0, column=0, sticky='nsew')

lower_frame = Frame(
    window, width=295, height=180,
    bg=COLOR0, pady=0, padx=0, relief='flat'
)
lower_frame.grid(row=1, column=0, sticky='nsew')


# -------------------------------------------------------------------------- #
# LABELS


app_label = Label(
    upper_frame, text='Calculadora de IMC',
    width=25, height=1, pady=4, padx=0, relief='flat',
    anchor='center', font=('Carlito 16 bold'),
    bg=COLOR0, fg=COLOR1
)
app_label.place(x=0, y=0)

separator_label = Label(
    upper_frame, text='', width=295,
    height=1, padx=0, relief='flat',
    anchor='center', font=('Carlito 1'),
    bg=COLOR2, fg=COLOR1
)
separator_label.place(x=0, y=35)

weight_label = Label(
    lower_frame, text='Insira seu peso',
    height=1, pady=4, padx=0, relief='flat',
    anchor='center', font=('Carlito 10 bold'),
    bg=COLOR0, fg=COLOR1
)
weight_label.grid(row=0, column=0, sticky='nsew', pady=10, padx=3)

height_label = Label(
    lower_frame, text='Insira sua altura',
    height=1, pady=4, padx=0, relief='flat',
    anchor='center', font=('Carlito 10 bold'),
    bg=COLOR0, fg=COLOR1
)
height_label.grid(row=1, column=0, sticky='nsew', pady=10, padx=3)

result_label = Label(
    lower_frame, text='----', width=6,
    height=2, pady=0, padx=6, relief='flat',
    anchor='center', font=('Carlito 24 bold'),
    bg=COLOR2, fg=COLOR0
)
result_label.place(x=170, y=10)

imc_label = Label(
    lower_frame, text='--------', width=37,
    height=1, pady=0, padx=0, relief='flat',
    anchor='center', font=('Carlito 10 bold'),
    bg=COLOR0, fg=COLOR1
)
imc_label.place(x=0, y=100)


# -------------------------------------------------------------------------- #
# ENTRIES


weight_entry = Entry(
    lower_frame, relief='solid',
    font=('Carlito 10 bold'),
    justify='center', width=6
)
weight_entry.grid(row=0, column=1, sticky='nsew', pady=10, padx=3)

height_entry = Entry(
    lower_frame, relief='solid',
    font=('Carlito 10 bold'),
    justify='center', width=6
)
height_entry.grid(row=1, column=1, sticky='nsew', pady=10, padx=3)


# -------------------------------------------------------------------------- #
# BOTÕES


calculate_button = Button(
    lower_frame, text='Calcular', width=34,
    height=1, relief='raised', overrelief='solid',
    anchor='center', font=('Carlito 10 bold'),
    bg=COLOR2, fg=COLOR0, activebackground=COLOR2,
    activeforeground=COLOR0, padx=20,
    command=lambda: calculate(
        float(weight_entry.get()),
        float(height_entry.get())
    )
)
calculate_button.grid(
    row=4, column=0,
    columnspan=30, sticky='nsew',
    pady=50, padx=5
)


# -------------------------------------------------------------------------- #
# LOOP PRINCIPAL


window.mainloop()
