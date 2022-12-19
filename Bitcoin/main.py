# --------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Label, Frame, PhotoImage
from tkinter.ttk import Separator
import requests

# from PIL import import ImageTk, Image (pip/pip3 install pillow)


# --------------------------------------------------------------------------- #
# CONSTANTES


COLOR0 = "#444466"  # Preto
COLOR1 = "#feffff"  # Branco
COLOR2 = "#6f9fbd"  # Azul
COLOR3 = '#484f60'  # Roxo??

API_LINK = 'https://min-api.cryptocompare.com/data/price?'\
    'fsym=BTC&tsyms=USD,EUR,BRL'


# --------------------------------------------------------------------------- #
# FUNÇÕES


def get_data():
    """Pega os valores."""
    response = requests.get(API_LINK)
    data = response.json()

    dolar_price_label['text'] = f"Dólar: ${float(data['USD']):,.3f}"
    euro_price_label['text'] = f"Euro: €{float(data['EUR']):,.3f}"
    real_price_label['text'] = f"Real: R${float(data['BRL']):,.3f}"

    # chama a cada 1 segundo para ir atualizando os valores.
    output_frame.after(1000, get_data)


# --------------------------------------------------------------------------- #
# JANELA PRINCIPAL


window = Tk()
window.title('')
window.geometry('320x350')
window.resizable(0, 0)
window.configure(bg=COLOR3)


# --------------------------------------------------------------------------- #
# SEPARADOR


Separator(
    window, orient='horizontal'
).grid(row=0, columnspan=1, ipadx=157)


# --------------------------------------------------------------------------- #
# FRAMES


title_frame = Frame(
    window, width=320, height=50,
    bg=COLOR1, pady=0, padx=0, relief='flat'
)
title_frame.grid(row=1, column=0)

output_frame = Frame(
    window, width=320, height=300,
    bg=COLOR3, pady=0, padx=0, relief='flat'
)
output_frame.grid(row=2, column=0, sticky='nw')


# --------------------------------------------------------------------------- #
# LABELS


# image = Image.open('bitcoin.png')
# image = image.resize(('valorInteiro, valorInteiro'), Image.ANTIALIAS)
# image = ImageTk.PhotoImage(image)

image = PhotoImage(file='bitcoin.png')
image_label = Label(
    title_frame, image=image,
    compound='left', bg=COLOR1,
    relief='flat'

)
image_label.place(x=5, y=5)

title_label = Label(
    title_frame, text='Bitcoin Price Tracker',
    bg=COLOR1, fg=COLOR2, relief='flat',
    anchor='center', font=('Arial 20')

)
title_label.place(x=50, y=5)

dolar_price_label = Label(
    output_frame, text='',
    bg=COLOR3, fg=COLOR1, relief='flat',
    anchor='center', font=('Arial 20'),
    width=20, padx=10

)
dolar_price_label.place(x=0, y=50)

euro_price_label = Label(
    output_frame, text='',
    bg=COLOR3, fg=COLOR1, relief='flat',
    anchor='center', font=('Arial 12'),
    width=30

)
euro_price_label.place(x=10, y=150)

real_price_label = Label(
    output_frame, text='',
    bg=COLOR3, fg=COLOR1, relief='flat',
    anchor='center', font=('Arial 12'),
    width=31, padx=10

)
real_price_label.place(x=2, y=180)


# --------------------------------------------------------------------------- #
# LOOP PRINCIPAL


get_data()
window.mainloop()
