# --------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Label, Frame, Button, StringVar


# --------------------------------------------------------------------------- #
# CONSTANTES


color1 = '#3b3b3b'  # preto
color2 = '#feffff'  # branco
color3 = '#38576b'  # azul (carregado)
color4 = '#ECEFF1'  # cinza
color5 = '#FFAB40'  # laranja


# --------------------------------------------------------------------------- #
# JANELA PRINCIPAL


window = Tk()
window.title('Calculadora')
window.geometry('295x310')
window.resizable(0, 0)
# window.config(bg=color1)


# --------------------------------------------------------------------------- #
# FRAMES


screen_frame = Frame(window, width=295, height=50, bg=color3)
screen_frame.grid(row=0, column=0)

body_frame = Frame(window, width=295, height=260)
body_frame.grid(row=1, column=0)


# --------------------------------------------------------------------------- #
# FUNÇÕES DE CÁLCULO


# Vai concatenando os valores e sinais (12+85*...)
values = ''


def value_insertion(key_value):
    """Função para agregar os valores na tela."""
    global values
    values = values + key_value
    # passa o valor para a tela
    value.set(values)


def equation():
    """Função para executar os cálculos."""
    global values
    result = eval(values)
    # print(result)
    value.set(result)


def clear_screen():
    """Função para limpar a tela depois de ser pressionado o sinal de '='."""
    global values
    values = ''
    value.set('')


# --------------------------------------------------------------------------- #
# LABELS


value = StringVar()
output_label = Label(
    screen_frame, textvariable=value, width=18, height=2,
    padx=4, pady=7, relief='flat', anchor='ne',
    justify='right', font=('Sans 19'), bg=color3, fg=color2
)
output_label.place(x=0, y=0)


# --------------------------------------------------------------------------- #
# BOTÕES


b_1 = Button(
    body_frame, text='C', width=11, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=clear_screen
)
b_1.place(x=0, y=0)

b_2 = Button(
    body_frame, text='mod', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('%')
)
b_2.place(x=147, y=0)

b_3 = Button(
    body_frame, text='/', width=4, height=2,
    bg=color5, fg=color2, activebackground=color5,
    activeforeground=color2, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('/')
)
b_3.place(x=220, y=0)

b_4 = Button(
    body_frame, text='7', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('7')
)
b_4.place(x=0, y=52)

b_5 = Button(
    body_frame, text='8', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('8')
)
b_5.place(x=74, y=52)

b_6 = Button(
    body_frame, text='9', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('9')
)
b_6.place(x=148, y=52)

b_7 = Button(
    body_frame, text='*', width=4, height=2,
    bg=color5, fg=color2, activebackground=color5,
    activeforeground=color2, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('*')
)
b_7.place(x=220, y=52)

b_8 = Button(
    body_frame, text='4', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('4')
)
b_8.place(x=0, y=104)

b_9 = Button(
    body_frame, text='5', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('5')
)
b_9.place(x=74, y=104)

b_10 = Button(
    body_frame, text='6', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('6')
)
b_10.place(x=148, y=104)

b_11 = Button(
    body_frame, text='-', width=4, height=2,
    bg=color5, fg=color2, activebackground=color5,
    activeforeground=color2, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('-')
)
b_11.place(x=220, y=104)

b_12 = Button(
    body_frame, text='1', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('1')
)
b_12.place(x=0, y=156)

b_13 = Button(
    body_frame, text='2', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('2')
)
b_13.place(x=74, y=156)

b_14 = Button(
    body_frame, text='3', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('3')
)
b_14.place(x=148, y=156)

b_15 = Button(
    body_frame, text='+', width=4, height=2,
    bg=color5, fg=color2, activebackground=color5,
    activeforeground=color2, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('+')
)
b_15.place(x=220, y=156)

b_16 = Button(
    body_frame, text='0', width=11, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('0')
)
b_16.place(x=0, y=208)

b_17 = Button(
    body_frame, text='.', width=4, height=2,
    bg=color4, font=('Sans 13 bold'),
    relief='raised', overrelief='ridge',
    command=lambda: value_insertion('.')
)
b_17.place(x=147, y=208)

b_18 = Button(
   body_frame, text='=', width=4, height=2,
   bg=color5, fg=color2, activebackground=color5,
   activeforeground=color2, font=('Sans 13 bold'),
   relief='raised', overrelief='ridge',
   command=equation
)
b_18.place(x=220, y=208)


# --------------------------------------------------------------------------- #
# LOOP PRINCIPAL


window.mainloop()


# --------------------------------------------------------------------------- #
