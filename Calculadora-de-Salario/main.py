# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Frame, Label, Button, Entry
from tkinter.ttk import Style
from PIL import Image, ImageTk


# -------------------------------------------------------------------------- #
# CONSTANTES


COLOR0 = '#2e2d2b'  # Preto
COLOR1 = '#feffff'  # Branco
COLOR2 = '#4fa882'  # Verde
COLOR3 = '#28576b'  # Valor
COLOR4 = '#403d3d'  # Letra
COLOR5 = '#e06636'  # Profit
COLOR6 = '#038cfc'  # Azul
COLOR7 = '#3fbfb9'  # Verde
COLOR8 = '#263238'  # + Verde
COLOR9 = '#e9edf5'  # Branco


# -------------------------------------------------------------------------- #
# FUNÇÕES


def output_calculations(hours, days, weeks, months, years):
    """Função para mostrar resultados dos cálculos."""
    hour_output_label['text'] = f' Salário por hora: R$ {hours:,.2f}'
    day_output_label['text'] = f' Salário diário: R$ {days:,.2f}'
    week_output_label['text'] = f' Salário semanal: R$ {weeks:,.2f}'
    month_output_label['text'] = f' Salário mensal: R$ {months:,.2f}'
    annual_output_label['text'] = f' Salário anual: R$ {years:,.2f}'


def output_entry_info(name, total_hours_day, work_days, annual_salary):
    """Função para mostrar os dados digitados pelo usuário."""
    output_name_label['text'] = name
    output_hours_label['text'] = f'Horas de trabalho ' \
        f'por dia: {total_hours_day}'
    output_days_label['text'] = f'Dias de trabalho por semana: {work_days}'
    output_annual_salary_label['text'] = f'R$ {annual_salary:,.2f}'


def calculate_salary():
    """Função para calcular o salario."""
    # Pega o input do usuário
    name = name_entry.get().title()
    total_hours_day = int(hours_entry.get())
    work_days = int(days_entry.get())
    annual_salary = float(annual_salary_entry.get())

    # Calculando total horas de trabalho por semana
    total_hours_work_week = total_hours_day * work_days

    # Calculando total horas de trabalho por ano
    # 52 - as semanas no ano
    total_hours_work_year = 52 * total_hours_work_week

    # Calculando o salário por horas
    hourly_pay = annual_salary / total_hours_work_year

    # Calculando salário diário
    daily_pay = hourly_pay * total_hours_day

    # Calculando salário semanal
    weekly_pay = annual_salary / 52

    # Calculando salário mensal
    monthly_pay = annual_salary / 12

    # Calculando salário bruto anual
    annual_pay = monthly_pay * 12

    output_entry_info(name, total_hours_day, work_days, annual_salary)
    output_calculations(
        hourly_pay, daily_pay,
        weekly_pay, monthly_pay, annual_pay
    )


# -------------------------------------------------------------------------- #
# JANELA


window = Tk()
window.title('')
window.geometry('580x350')
window.resizable(0, 0)
window.configure(bg=COLOR9)


style = Style(window)
style.theme_use('clam')


# -------------------------------------------------------------------------- #
# FRAMES


upper_frame = Frame(window, width=580, height=60, pady=5, bg=COLOR1)
upper_frame.grid(row=0, column=0)

lower_frame = Frame(window, width=580, height=290, pady=0, bg=COLOR1)
lower_frame.grid(row=1, column=0)


# -------------------------------------------------------------------------- #
# LABELS


# Logo e título do app.
app_image_logo = Image.open('imagens/salary.png')
app_image_logo = app_image_logo.resize((25, 25))
app_image_logo = ImageTk.PhotoImage(app_image_logo)
app_label = Label(
    upper_frame, text='Calculadora de Salário', image=app_image_logo,
    width=600, compound='left', relief='raised', anchor='nw',
    font=('Verdana 15'), bg=COLOR1, fg=COLOR4
)
app_label.place(x=0, y=0)

# Labels para pedir input do usuario.
# Nome, horas de trabalho, dias de trabalho e
# salário anual.
name_label = Label(
    lower_frame, text='Escreva o seu nome completo',
    anchor='nw', font=('Roboto 10'),
    bg=COLOR1, fg=COLOR4
)
name_label.place(x=10, y=10)

hours_label = Label(
    lower_frame, text='Quantas horas você trabalha por dia?',
    anchor='nw', font=('Roboto 10'),
    bg=COLOR1, fg=COLOR4
)
hours_label.place(x=10, y=40)

days_label = Label(
    lower_frame, text='Quantos dias você trabalha por semana?',
    anchor='nw', font=('Roboto 10'),
    bg=COLOR1, fg=COLOR4
)
days_label.place(x=10, y=70)

annual_salary_label = Label(
    lower_frame, text='Qual é o seu salário anual?',
    anchor='nw', font=('Roboto 10'),
    bg=COLOR1, fg=COLOR4
)
annual_salary_label.place(x=10, y=100)

# Label e imagem que fica por cima do botão 'CALCULAR'
calculate_image_logo = Image.open('imagens/salary.png')
calculate_image_logo = calculate_image_logo.resize((90, 90))
calculate_image_logo = ImageTk.PhotoImage(calculate_image_logo)
calculate_label = Label(
    lower_frame, image=calculate_image_logo,
    bg=COLOR1, fg=COLOR4
)
calculate_label.place(x=470, y=0)

# Labels que ficam na parte inferior esquerda do app.
# Espelham o input do usuário, nome, horas, dias e salário
output_name_label = Label(
    lower_frame, width=30, pady=5, padx=5,
    relief='raised', anchor='nw',
    font=('Roboto 10'), bg=COLOR9, fg=COLOR0
)
output_name_label.place(x=10, y=150)

output_hours_label = Label(
    lower_frame, width=30, pady=5, padx=5,
    relief='raised', anchor='nw',
    font=('Roboto 10'), bg=COLOR9, fg=COLOR0
)
output_hours_label.place(x=10, y=179)

output_days_label = Label(
    lower_frame, width=30, pady=5, padx=5,
    relief='raised', anchor='nw',
    font=('Roboto 10'), bg=COLOR9, fg=COLOR0
)
output_days_label.place(x=10, y=208)

output_annual_salary_label = Label(
    lower_frame, width=30, pady=5, padx=5,
    relief='raised', anchor='nw',
    font=('Roboto 10 bold'), bg=COLOR9, fg=COLOR0
)
output_annual_salary_label.place(x=10, y=237)

# Labels que ficam na parte inferior direita do app.
# Mostram o resultado dos cálculos, salário por hora,
# por dia, por semana, mês e por ano.
hour_output_logo = Image.open('imagens/yellow-circle.png')
hour_output_logo = hour_output_logo.resize((20, 20))
hour_output_logo = ImageTk.PhotoImage(hour_output_logo)
hour_output_label = Label(
    lower_frame, image=hour_output_logo,
    width=300, compound='left', anchor='nw',
    font=('Roboto 10'), bg=COLOR1, fg=COLOR0
)
hour_output_label.place(x=300, y=145)

day_output_logo = Image.open('imagens/blue-circle.png')
day_output_logo = day_output_logo.resize((20, 20))
day_output_logo = ImageTk.PhotoImage(day_output_logo)
day_output_label = Label(
    lower_frame, image=day_output_logo,
    width=300, compound='left', anchor='nw',
    font=('Roboto 10'), bg=COLOR1, fg=COLOR0
)
day_output_label.place(x=300, y=170)

week_output_logo = Image.open('imagens/gray-circle.png')
week_output_logo = week_output_logo.resize((20, 20))
week_output_logo = ImageTk.PhotoImage(week_output_logo)
week_output_label = Label(
    lower_frame, image=week_output_logo,
    width=300, compound='left', anchor='nw',
    font=('Roboto 10'), bg=COLOR1, fg=COLOR0
)
week_output_label.place(x=300, y=195)

month_output_logo = Image.open('imagens/red-circle.png')
month_output_logo = month_output_logo.resize((20, 20))
month_output_logo = ImageTk.PhotoImage(month_output_logo)
month_output_label = Label(
    lower_frame, image=month_output_logo,
    width=300, compound='left', anchor='nw',
    font=('Roboto 10'), bg=COLOR1, fg=COLOR0
)
month_output_label.place(x=300, y=220)

annual_output_logo = Image.open('imagens/green-circle.png')
annual_output_logo = annual_output_logo.resize((20, 20))
annual_output_logo = ImageTk.PhotoImage(annual_output_logo)
annual_output_label = Label(
    lower_frame, image=annual_output_logo,
    width=300, compound='left', anchor='nw',
    font=('Roboto 10'), bg=COLOR1, fg=COLOR0
)
annual_output_label.place(x=300, y=245)


# -------------------------------------------------------------------------- #
# ENTRIES


name_entry = Entry(lower_frame, width=25, justify='center', relief='solid')
name_entry.place(x=200, y=11)

hours_entry = Entry(lower_frame, width=15, justify='center', relief='solid')
hours_entry.place(x=290, y=41)

days_entry = Entry(lower_frame, width=15, justify='center', relief='solid')
days_entry.place(x=290, y=71)

annual_salary_entry = Entry(
    lower_frame, width=15, justify='center', relief='solid'
)
annual_salary_entry.place(x=290, y=101)


# -------------------------------------------------------------------------- #
# BOTÕES


button_image_logo = Image.open('imagens/salary.png')
button_image_logo = button_image_logo.resize((20, 20))
button_image_logo = ImageTk.PhotoImage(button_image_logo)
calculate_button = Button(
    lower_frame, text='CALCULAR', image=button_image_logo,
    compound='left', relief='raised', overrelief='ridge',
    anchor='ne', font=('Roboto 8 bold'), bg=COLOR1, fg=COLOR4,
    command=calculate_salary
)
calculate_button.place(x=450, y=92)


# -------------------------------------------------------------------------- #
# LOOP


window.mainloop()
