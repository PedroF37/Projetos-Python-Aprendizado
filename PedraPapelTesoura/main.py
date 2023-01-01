# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Frame, Label, Button
from tkinter.ttk import Style
from PIL import Image, ImageTk
from random import shuffle, choice


# -------------------------------------------------------------------------- #
# CONSTANTES E GLOBAIS


COLOR0 = '#FFFFFF'  # Branco
COLOR1 = '#333333'  # Preto
COLOR2 = '#fff873'  # Amarelo
COLOR3 = '#e85151'  # Vermelho
COLOR4 = '#34eb3d'  # Verde
COLOR5 = '#3b3b3b'  # Fundo

global HUMAN_PLAYER
global PC_PLAYER
global ROUNDS
global HUMAN_PLAYER_POINTS
global PC_PLAYER_POINTS

HUMAN_PLAYER_POINTS = 0
PC_PLAYER_POINTS = 0
ROUNDS = 5


# -------------------------------------------------------------------------- #
# FUNÇÕES


def game_round(player_choice):
    """Trata das rodadas e das escolhas dos jogadores."""
    global HUMAN_PLAYER
    global PC_PLAYER
    global ROUNDS
    global HUMAN_PLAYER_POINTS
    global PC_PLAYER_POINTS

    if ROUNDS > 0:
        options = ['Pedra', 'Papel', 'Tesoura']
        shuffle(options)
        PC_PLAYER = choice(options)
        HUMAN_PLAYER = player_choice
        human_player_choice['text'] = HUMAN_PLAYER
        human_player_choice['fg'] = COLOR1
        pc_player_choice['text'] = PC_PLAYER
        pc_player_choice['fg'] = COLOR1

        # Empate
        if (HUMAN_PLAYER == 'Pedra' and PC_PLAYER == 'Pedra') or \
           (HUMAN_PLAYER == 'Papel' and PC_PLAYER == 'Papel') or \
           (HUMAN_PLAYER == 'Tesoura' and PC_PLAYER == 'Tesoura'):
            human_player_line['bg'] = COLOR0
            pc_player_line['bg'] = COLOR0
            tie_line['bg'] = COLOR2
        # Jogador vence
        elif (HUMAN_PLAYER == 'Pedra' and PC_PLAYER == 'Tesoura') or \
             (HUMAN_PLAYER == 'Papel' and PC_PLAYER == 'Pedra') or \
             (HUMAN_PLAYER == 'Tesoura' and PC_PLAYER == 'Papel'):
            human_player_line['bg'] = COLOR4
            pc_player_line['bg'] = COLOR0
            tie_line['bg'] = COLOR0
            HUMAN_PLAYER_POINTS += 10
        else:
            human_player_line['bg'] = COLOR0
            pc_player_line['bg'] = COLOR4
            tie_line['bg'] = COLOR0
            PC_PLAYER_POINTS += 10

        # Atualiza pontuação e valor de 'ROUNDS'
        human_player_score['text'] = HUMAN_PLAYER_POINTS
        pc_player_score['text'] = PC_PLAYER_POINTS
        ROUNDS -= 1
    else:
        human_player_score['text'] = HUMAN_PLAYER_POINTS
        pc_player_score['text'] = PC_PLAYER_POINTS
        game_over()


def start_game():
    """Função que inicia o jogo."""
    global rock_img
    global paper_img
    global scissors_img
    global rock_button
    global paper_button
    global scissors_button

    start_button.destroy()

    rock_img = Image.open('icons/pedra.png')
    rock_img = rock_img.resize((50, 50), Image.ANTIALIAS)
    rock_img = ImageTk.PhotoImage(rock_img)
    rock_button = Button(
        game_frame, width=50, image=rock_img,
        compound='center', bg=COLOR0, fg=COLOR0,
        font=('Roboto 10 bold'), anchor='center',
        relief='flat', highlightthickness=0,
        command=lambda: game_round('Pedra')
    )
    rock_button.place(x=15, y=60)

    paper_img = Image.open('icons/papel.png')
    paper_img = paper_img.resize((50, 50), Image.ANTIALIAS)
    paper_img = ImageTk.PhotoImage(paper_img)
    paper_button = Button(
        game_frame, width=50, image=paper_img,
        compound='center', bg=COLOR0, fg=COLOR0,
        font=('Roboto 10 bold'), anchor='center',
        relief='flat', highlightthickness=0,
        command=lambda: game_round('Papel')
    )
    paper_button.place(x=100, y=60)

    scissors_img = Image.open('icons/tesoura.png')
    scissors_img = scissors_img.resize((50, 50), Image.ANTIALIAS)
    scissors_img = ImageTk.PhotoImage(scissors_img)
    scissors_button = Button(
        game_frame, width=50, image=scissors_img,
        compound='center', bg=COLOR0, fg=COLOR0,
        font=('Roboto 10 bold'), anchor='center',
        relief='flat', highlightthickness=0,
        command=lambda: game_round('Tesoura')
    )
    scissors_button.place(x=185, y=60)


def game_over():
    """Função que trata do fim do jogo."""
    global ROUNDS
    global HUMAN_PLAYER_POINTS
    global PC_PLAYER_POINTS

    # Resetando variáveis para o estado inicial
    HUMAN_PLAYER_POINTS = 0
    PC_PLAYER_POINTS = 0
    ROUNDS = 5

    # Destroi os botões
    rock_button.destroy()
    paper_button.destroy()
    scissors_button.destroy()

    # Definindo o vencedor
    human_score = int(human_player_score['text'])
    pc_score = int(pc_player_score['text'])

    if human_score > pc_score:
        winner_label = Label(
            game_frame, text='Parabéns! Você Venceu!', height=1,
            anchor='center', font=('Roboto 10 bold'), bg=COLOR0, fg=COLOR4
        )
        winner_label.place(x=5, y=60)
    elif human_score < pc_score:
        winner_label = Label(
            game_frame, text='PC Venceu!', height=1,
            anchor='center', font=('Roboto 10 bold'), bg=COLOR0, fg=COLOR3
        )
        winner_label.place(x=5, y=60)
    else:
        winner_label = Label(
            game_frame, text='Foi Empate!', height=1,
            anchor='center', font=('Roboto 10 bold'), bg=COLOR0, fg=COLOR2
        )
        winner_label.place(x=5, y=60)

    def play_again():
        """Inicia um novo jogo, com tudo zerado."""
        human_player_score['text'] = '0'
        pc_player_score['text'] = '0'
        winner_label.destroy()
        play_again_button.destroy()
        start_game()

    play_again_button = Button(
        game_frame, width=30, text='Jogar de Novo',
        bg=COLOR5, fg=COLOR0, font=('Roboto 10 bold'),
        anchor='center', relief='raised', overrelief='ridge',
        padx=0, command=play_again
    )
    play_again_button.place(x=7, y=151)


# ---------------------------------------------------------------------------#
# JANELA


window = Tk()
window.title('')
window.resizable(0, 0)
window.configure(bg=COLOR5)


# -------------------------------------------------------------------------- #
# FRAMES


score_frame = Frame(window, width=260, height=100, bg=COLOR1, relief='raised')
score_frame.grid(row=0, column=0, sticky='nw')

game_frame = Frame(window, width=260, height=180, bg=COLOR0, relief='flat')
game_frame.grid(row=1, column=0, sticky='nw')


style = Style(window)
style.theme_use('clam')


# -------------------------------------------------------------------------- #
# LABELS


human_player = Label(
    score_frame, text='Você', height=1,
    anchor='center', font=('Roboto 10 bold'),
    bg=COLOR1, fg=COLOR0
)
human_player.place(x=25, y=70)

human_player_line = Label(
    score_frame, text='', height=10,
    anchor='center', font=('Roboto 10 bold'),
    bg=COLOR0, fg=COLOR0
)
human_player_line.place(x=0, y=0)

human_player_score = Label(
    score_frame, text='0', height=1,
    anchor='center', font=('Roboto 30 bold'),
    bg=COLOR1, fg=COLOR0
)
human_player_score.place(x=50, y=20)

score_divider = Label(
    score_frame, text=':', height=1,
    anchor='center', font=('Roboto 30 bold'),
    bg=COLOR1, fg=COLOR0
)
score_divider.place(x=120, y=20)

pc_player = Label(
    score_frame, text='PC', height=1,
    anchor='center', font=('Roboto 10 bold'),
    bg=COLOR1, fg=COLOR0
)
pc_player.place(x=210, y=70)

pc_player_line = Label(
    score_frame, text='', height=10,
    anchor='center', font=('Roboto 10 bold'),
    bg=COLOR0, fg=COLOR0
)
pc_player_line.place(x=256, y=0)

pc_player_score = Label(
    score_frame, text='0', height=1,
    anchor='center', font=('Roboto 30 bold'),
    bg=COLOR1, fg=COLOR0
)
pc_player_score.place(x=180, y=20)


tie_line = Label(
    score_frame, text='', width=255,
    anchor='center', font=('Roboto 1 bold'),
    bg=COLOR0, fg=COLOR0
)
tie_line.place(x=0, y=95)

human_player_choice = Label(
    game_frame, text='', height=1,
    anchor='center', font=('Roboto 10 bold'),
    bg=COLOR0, fg=COLOR0
)
human_player_choice.place(x=25, y=10)

pc_player_choice = Label(
    game_frame, text='', height=1,
    anchor='center', font=('Roboto 10 bold'),
    bg=COLOR0, fg=COLOR0
)
pc_player_choice.place(x=190, y=10)


# -------------------------------------------------------------------------- #
# BOTÃO INICIAR


start_button = Button(
    game_frame, width=30, text='Jogar',
    bg=COLOR5, fg=COLOR0, font=('Roboto 10 bold'),
    anchor='center', relief='raised', overrelief='ridge',
    padx=0, command=start_game
)
start_button.place(x=7, y=151)


# -------------------------------------------------------------------------- #
# LOOP


window.mainloop()
