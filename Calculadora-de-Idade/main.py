# --------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Frame, Label, Button
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date


# --------------------------------------------------------------------------- #
# CONSTANTES


COLOR1 = '#3b3b3b'  # preto (ou cinza escuro?)
COLOR2 = '#333333'  # cinza (mais carregado..)
COLOR3 = '#FFFFFF'  # branco
COLOR4 = '#fcc058'  # laranja


# --------------------------------------------------------------------------- #
# FUNÇÕES


def calculate_age():
    """Função para calcular a idade."""
    beginning = initial_date_entry.get()
    birth_date = birth_date_entry.get()

    # separa os valores e converte para o formato do datetime
    day1, month1, year1 = [int(value) for value in beginning.split('/')]
    initial_date = date(year1, month1, day1)

    day2, month2, year2 = [int(value) for value in birth_date.split('/')]
    birth_date = date(year2, month2, day2)

    year = relativedelta(initial_date, birth_date).years
    month = relativedelta(initial_date, birth_date).months
    day = relativedelta(initial_date, birth_date).days

    year_label['text'] = year
    month_label['text'] = month
    day_label['text'] = day


# --------------------------------------------------------------------------- #
# JANELA PRINCIPAL


window = Tk()
window.title('')
window.geometry('350x430')
window.resizable(0, 0)


# --------------------------------------------------------------------------- #
# FRAMES


upper_frame = Frame(
    window, width=350, height=140,
    pady=0, padx=0, relief='flat',
    bg=COLOR2
)
upper_frame.grid(row=0, column=0)

lower_frame = Frame(
    window, width=350, height=360,
    pady=0, padx=0, relief='flat',
    bg=COLOR1
)
lower_frame.grid(row=1, column=0)


# --------------------------------------------------------------------------- #
# LABELS


# Frame superior
calculator_label = Label(
    upper_frame, text='CALCULADORA', width=22,
    height=1, padx=3, relief='flat',
    anchor='center', font=('Roboto 18 bold'),
    bg=COLOR2, fg=COLOR3
)
calculator_label.place(x=0, y=30)

age_label = Label(
    upper_frame, text='DE IDADE', width=12,
    height=1, padx=0, relief='flat',
    anchor='center', font=('Roboto 35 bold'),
    bg=COLOR2, fg=COLOR4
)
age_label.place(x=0, y=70)


# Frame inferior
initial_date_label = Label(
    lower_frame, text='Data Inicial',
    height=1, padx=0, pady=0, relief='flat',
    anchor='nw', font=('Roboto 13'),
    bg=COLOR1, fg=COLOR3
)
initial_date_label.place(x=20, y=30)

birth_date_label = Label(
    lower_frame, text='Data de Nascimento',
    height=1, padx=0, pady=0, relief='flat',
    anchor='nw', font=('Roboto 13'),
    bg=COLOR1, fg=COLOR3
)
birth_date_label.place(x=20, y=70)

year_label = Label(
    lower_frame, text='--',
    height=1, padx=0, pady=0,
    relief='flat', anchor='center',
    font=('Roboto 25 bold'),
    bg=COLOR1, fg=COLOR3
)
year_label.place(x=40, y=135)

year_text_label = Label(
    lower_frame, text='Anos',
    height=1, padx=0, pady=0,
    relief='flat', anchor='center',
    font=('Roboto 11 bold'),
    bg=COLOR1, fg=COLOR3
)
year_text_label.place(x=40, y=180)
#

month_label = Label(
    lower_frame, text='--',
    height=1, padx=0, pady=0,
    relief='flat', anchor='center',
    font=('Roboto 25 bold'),
    bg=COLOR1, fg=COLOR3
)
month_label.place(x=140, y=135)

month_text_label = Label(
    lower_frame, text='Meses',
    height=1, padx=0, pady=0,
    relief='flat', anchor='center',
    font=('Roboto 11 bold'),
    bg=COLOR1, fg=COLOR3
)
month_text_label.place(x=130, y=180)
#

day_label = Label(
    lower_frame, text='--',
    height=1, padx=0, pady=0,
    relief='flat', anchor='center',
    font=('Roboto 25 bold'),
    bg=COLOR1, fg=COLOR3
)
day_label.place(x=240, y=135)

day_text_label = Label(
    lower_frame, text='Dias',
    height=1, padx=0, pady=0,
    relief='flat', anchor='center',
    font=('Roboto 11 bold'),
    bg=COLOR1, fg=COLOR3
)
day_text_label.place(x=240, y=180)


# --------------------------------------------------------------------------- #
# ENTRIES


initial_date_entry = DateEntry(
    lower_frame, width=13,
    bg='darkblue', fg=COLOR3,
    borderwidth=2, date_patter='dd/mm/y',
    y=2022
)
initial_date_entry.place(x=190, y=30)

birth_date_entry = DateEntry(
    lower_frame, width=13,
    bg='darkblue', fg=COLOR3,
    borderwidth=2, date_patter='dd/mm/y',
    y=2022
)
birth_date_entry.place(x=190, y=70)


# --------------------------------------------------------------------------- #
# BOTÃO DE SUBMETER


submit_button = Button(
    lower_frame, text='Calcular', height=1,
    width=20, relief='raised', overrelief='ridge',
    font=('Roboto 10 bold'), bg=COLOR1, fg=COLOR3,
    activebackground=COLOR1, activeforeground=COLOR3,
    command=calculate_age
)
submit_button.place(x=70, y=225)


# --------------------------------------------------------------------------- #
# LOOP PRINCIPAL


window.mainloop()


# --------------------------------------------------------------------------- #
