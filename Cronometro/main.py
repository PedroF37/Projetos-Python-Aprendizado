# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Button, Label


# -------------------------------------------------------------------------- #
# CONSTANTES


COLOR1 = '#0a0a0a'  # Preto
COLOR2 = '#fafcff'  # Branco
COLOR3 = '#21c25c'  # Verde
COLOR4 = '#eb463b'  # Vermelho
COLOR5 = '#dedcdc'  # Cinza? / Branco?
COLOR6 = '#3080f0'  # Azul


# -------------------------------------------------------------------------- #
# FLAGS E GLOBAIS


global actual_time
global run
global counter
global limit

actual_time = '00:00:00'
run = False
counter = -5
limit = 59


# -------------------------------------------------------------------------- #
# FUNÇÕES


def initiate_timer():
    """Função para iniciar cronômetro"""
    global actual_time
    global limit
    global counter
    global run

    if run:
        # antes do cronômetro começar
        if counter <= -1:
            init = f'Começando em {counter}'
            time_label['text'] = init
            time_label['font'] = 'Arial 10'
        else:
            # rodando o cronômetro
            time_label['font'] = 'Times 50 bold'
            temp_time = str(actual_time)
            hours, minutes, seconds = map(int, temp_time.split(':'))
            seconds = int(counter)

            if seconds >= limit:
                counter = 0
                minutes += 1

            seconds = str(0) + str(seconds)
            minutes = str(0) + str(minutes)
            hours = str(0) + str(hours)

            # atualizando os valores
            temp_time = f'{hours[-2:]}:{minutes[-2:]}:{seconds[-2:]}'
            time_label['text'] = temp_time
            actual_time = temp_time

        time_label.after(1000, initiate_timer)
        counter += 1


def start_clock():
    """Função para ativa flag 'run' de False para True."""
    global run
    run = True
    initiate_timer()


def pause_clock():
    """Função para pausar cronômetro."""
    global run
    run = False


def reinitiate_clock():
    """Função para reiniciar cronômetro."""
    global counter
    global actual_time

    counter = 0
    actual_time = '00:00:00'
    time_label['text'] = actual_time


# -------------------------------------------------------------------------- #
# JANELA PRINCIPAL


window = Tk()
window.title('')
window.geometry('300x180')
window.resizable(0, 0)
window.configure(bg=COLOR1)


# -------------------------------------------------------------------------- #
# LABELS


app_label = Label(
    window, text='Cronômetro',
    font=('Arial 10'), bg=COLOR1,
    fg=COLOR2
)
app_label.place(x=20, y=5)

time_label = Label(
    window, text=actual_time,
    font=('Times 50 bold'), bg=COLOR1,
    fg=COLOR4
)
time_label.place(x=25, y=40)


# -------------------------------------------------------------------------- #
# BOTÕES


init_button = Button(
    window, text='Iniciar', width=8, height=2,
    bg=COLOR1, fg=COLOR2, font=('Carlito 10 bold'),
    relief='raised', overrelief='ridge',
    activebackground=COLOR1, activeforeground=COLOR2,
    command=start_clock
)
init_button.place(x=20, y=120)

pause_button = Button(
    window, text='Pausar', width=8, height=2,
    bg=COLOR1, fg=COLOR2, font=('Carlito 10 bold'),
    relief='raised', overrelief='ridge',
    activebackground=COLOR1, activeforeground=COLOR2,
    command=pause_clock
)
pause_button.place(x=110, y=120)

reinit_button = Button(
    window, text='Reiniciar', width=8, height=2,
    bg=COLOR1, fg=COLOR2, font=('Carlito 10 bold'),
    relief='raised', overrelief='ridge',
    activebackground=COLOR1, activeforeground=COLOR2,
    command=reinitiate_clock
)
reinit_button.place(x=200, y=120)


# -------------------------------------------------------------------------- #
# LOOP PRINCIPAL


window.mainloop()
