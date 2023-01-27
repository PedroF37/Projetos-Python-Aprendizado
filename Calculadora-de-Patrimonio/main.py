# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


# tkinter
from tkinter import Tk, Frame, Button, Label, Entry, messagebox
from tkinter.ttk import Style

# Pillow
from PIL import Image, ImageTk

# reduce
from functools import reduce

# re
from re import fullmatch


# -------------------------------------------------------------------------- #
# CORES E GLOBAIS


COLOR0 = '#2e2d2b'  # Preto
COLOR1 = '#feffff'  # Branco
COLOR2 = '#4fa882'  # Verde
COLOR3 = '#38576b'  # Valor
COLOR4 = '#403d3d'  # Letra
COLOR5 = '#e06636'  # Lucro
COLOR6 = '#e9edf5'  # + Verde
COLOR7 = '#00C9FF'  # Azul claro

number_pattern = r'^\d+$'

# -------------------------------------------------------------------------- #
# FUNÇÕES


def calculate(investments, debts):
    """Função que cuida do cálculo."""

    # Verifica se está tudo preenchido
    for (item1, item2) in zip(investments, debts):
        if item1 == '' or item2 == '':
            messagebox.showerror('Erro', 'Entre com todos os valores')
            return
        if fullmatch(number_pattern, item1) is None \
            or fullmatch(number_pattern, item2) is None:
            messagebox.showerror(
                'Erro', 'Tem que entrar com digitos decimais apenas'
            )
            return


    total_assets = reduce(lambda x, y: float(x) + float(y), investments)
    # print(total_assets)
    total_debts = reduce(lambda x, y: float(x) + float(y), debts)
    # print(total_debts)

    result_label['text'] = f'R${total_assets - total_debts:,.2f}'


# -------------------------------------------------------------------------- #
# JANELA


window = Tk()
window.title('')
window.geometry('380x500')
window.configure(background=COLOR1)
window.resizable(0, 0)

style = Style(window)
style.theme_use('clam')


# -------------------------------------------------------------------------- #
# FRAMES


# Frames Principais
upper_frame = Frame(window, width=380, height=50, bg=COLOR1, relief='flat')
upper_frame.grid(row=0, column=0, columnspan=2)

lower_frame = Frame(window, width=380, height=400, bg=COLOR1, relief='flat')
lower_frame.grid(row=2, column=0, pady=10)

result_frame = Frame(window, width=364, height=50, bg=COLOR3, relief='flat')
result_frame.grid(row=1, column=0, pady=10)


# Frames dentro de Frames
assets_frame = Frame(
    lower_frame, width=180, height=370,
    bg=COLOR6, relief='flat'
)
assets_frame.grid(row=0, column=0, pady=0, padx=5)

passive_frame = Frame(
    lower_frame, width=180, height=370,
    bg=COLOR6, relief='flat'
)
passive_frame.grid(row=0, column=1, pady=0)


# -------------------------------------------------------------------------- #
# CONFIGURANDO UPPER_FRAME


# Imagem
app_img = Image.open('img1.png')
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

logo_label = Label(
    upper_frame, image=app_img,
    compound='left',
    anchor='nw', padx=5,
    relief='flat', bg=COLOR1, fg=COLOR4
)
logo_label.place(x=5, y=0)

title_label = Label(
    upper_frame, text=' Calculadora de Património Líquido',
    compound='left', padx=2, pady=20, relief='flat', anchor='nw',
    font=('Roboto 12'), bg=COLOR1, fg=COLOR4
)
title_label.place(x=60, y=0)

line_label = Label(
    upper_frame, width=380, height=1,
    anchor='nw', font=('Roboto 1'),
    bg=COLOR3, fg=COLOR1
)
line_label.place(x=0, y=48)


# -------------------------------------------------------------------------- #
# CONFIGURANDO ASSETS_FRAME


assets_label = Label(
    assets_frame, text='Insira Ativos',
    padx=40, width=15, height=1, anchor='nw',
    font=('Roboto 11'), bg=COLOR2, fg=COLOR1
)
assets_label.place(x=0, y=0)

# Valor da casa
house_value_label = Label(
    assets_frame, text='Valor da Casa',
    height=1, anchor='e', font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
house_value_label.place(x=10, y=40)

house_value_entry = Entry(
    assets_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
house_value_entry.place(x=10, y=65)

# Imoveis
furniture_label = Label(
    assets_frame, text='Imóveis',
    height=1, anchor='e',
    font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
furniture_label.place(x=10, y=105)

furniture_entry = Entry(
    assets_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
furniture_entry.place(x=10, y=130)

# Veículos
vehicle_label = Label(
    assets_frame, text='Veículos',
    height=1, anchor='e',
    font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
vehicle_label.place(x=10, y=170)

vehicle_entry = Entry(
    assets_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
vehicle_entry.place(x=10, y=195)

# Investimentos
investments_label = Label(
    assets_frame, text='Investimentos',
    height=1, anchor='e',
    font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
investments_label.place(x=10, y=235)

investments_entry = Entry(
    assets_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
investments_entry.place(x=10, y=260)

# Outros..
other_assets_label = Label(
    assets_frame, text='Outros Ativos',
    height=1, anchor='e',
    font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
other_assets_label.place(x=10, y=300)

other_assets_entry = Entry(
    assets_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
other_assets_entry.place(x=10, y=325)


# -------------------------------------------------------------------------- #
# CONFIGURANDO PASSIVE_FRAME


passive_label = Label(
    passive_frame, text='Insira Passivos',
    padx=40, width=15, height=1, anchor='nw',
    font=('Roboto 11'), bg=COLOR5, fg=COLOR1
)
passive_label.place(x=0, y=0)

# Hipoteca
mortgage_value_label = Label(
    passive_frame, text='Hipoteca',
    height=1, anchor='e', font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
mortgage_value_label.place(x=10, y=40)

mortgage_value_entry = Entry(
    passive_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
mortgage_value_entry.place(x=10, y=65)

# Empréstimo do carro
car_loan_label = Label(
    passive_frame, text='Empréstimo do Carro',
    height=1, anchor='e',
    font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
car_loan_label.place(x=10, y=105)

car_loan_entry = Entry(
    passive_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
car_loan_entry.place(x=10, y=130)

# Empréstimo estudantil
student_loan_label = Label(
    passive_frame, text='Empréstimos Estudantis',
    height=1, anchor='e',
    font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
student_loan_label.place(x=10, y=170)

student_loan_entry = Entry(
    passive_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
student_loan_entry.place(x=10, y=195)

# Outras dívidas
other_debts_label = Label(
    passive_frame, text='Outras Dívidas',
    height=1, anchor='e',
    font=('Roboto 9'),
    bg=COLOR6, fg=COLOR0
)
other_debts_label.place(x=10, y=235)

other_debts_entry = Entry(
    passive_frame, width=12,
    font=('Roboto 9'),
    justify='center',
    relief='flat',
    bd=2, borderwidth=2
)
other_debts_entry.place(x=10, y=260)

# Imagem para botão calcular
calculate_img = Image.open('img2.png')
calculate_img = calculate_img.resize((25, 25))
calculate_img = ImageTk.PhotoImage(calculate_img)

# Botão de calcular
calculate_button = Button(
    passive_frame, width=120, anchor='center',
    image=calculate_img, compound='left',
    text='CALCULAR  ', relief='flat', overrelief='ridge',
    font=('Roboto 8 bold'), bg=COLOR7, fg=COLOR1,
    activebackground=COLOR7, activeforeground=COLOR1,
    padx=0, command=lambda: calculate(
        [
            house_value_entry.get(), furniture_entry.get(),
            vehicle_entry.get(), investments_entry.get(),
            other_assets_entry.get()
        ],
        [
            mortgage_value_entry.get(), car_loan_entry.get(),
            student_loan_entry.get(), other_debts_entry.get()
        ]
    )
)
calculate_button.place(x=10, y=320)


# -------------------------------------------------------------------------- #
# CONFIGURANDO RESULT_FRAME


result_label = Label(
    result_frame, text=f'R${00:,.2f}',
    padx=10, width=15, height=1, anchor='ne',
    font=('Roboto 25 bold'), bg=COLOR3, fg=COLOR1
)
result_label.place(x=60, y=7)


# -------------------------------------------------------------------------- #
# LOOP


window.mainloop()
