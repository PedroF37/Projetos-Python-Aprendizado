# --------------------------------------------------------------------------- #
# IMPORTAÇÕES


from tkinter import Tk, Frame, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# --------------------------------------------------------------------------- #
# CORES


COLOR0 = '#f0f3f5'  # Branco
COLOR1 = '#feffff'  # Branco
COLOR2 = '#6f9fbd'  # Azul
COLOR3 = '#38576b'  # Valor
COLOR4 = '#403d3d'  # Letra
COLOR5 = '#e06636'  # Laranja
COLOR6 = '#6dd695'  # Verde
COLOR7 = '#3F729B'  # Azul escuro (Fundo)


# --------------------------------------------------------------------------- #
# JANELA


window = Tk()
window.title('')
window.geometry('1200x600')
window.resizable(0, 0)


# --------------------------------------------------------------------------- #
# FRAMES PRINCIPAIS E TÍTULO DO APP


upper_frame = Frame(
    window, width=1200, height=45,
    pady=0, padx=0, bg=COLOR1, relief='flat'
)
upper_frame.grid(row=0, column=0)

lower_frame = Frame(
    window, width=1200, height=555,
    pady=15, padx=7, relief='flat'
)
lower_frame.grid(row=1, column=0, pady=2, sticky='nw')

title_label = Label(
    upper_frame, text='Dashboard de Vendas', width=20, height=2,
    pady=1, padx=0, bg=COLOR1, fg=COLOR4, relief='flat', anchor='n',
    font=('Roboto 14 bold')
)
title_label.place(x=0, y=5)


# --------------------------------------------------------------------------- #
# FRAME DE RECEITAS DE VENDAS


revenue_frame = Frame(
    lower_frame, width=200, height=90,
    bg=COLOR1, relief='flat'
)
revenue_frame.place(x=0, y=0)

line_label = Label(
    revenue_frame, text='', width=2, height=5,
    pady=0, padx=0, bg=COLOR2, relief='flat', anchor='nw',
    font=('Roboto 1 bold')
)
line_label.place(x=0, y=0)

revenue_label = Label(
    revenue_frame, text='Receitas Vendidas', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR4, relief='flat',
    anchor='center', font=('Roboto 10 bold')
)
revenue_label.place(x=20, y=5)

value_revenue_label = Label(
    revenue_frame, text='R$ 7,890,645', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR3, relief='flat',
    anchor='center', font=('Roboto 18 bold')
)
value_revenue_label.place(x=40, y=35)

gain_revenue_label = Label(
    revenue_frame, text='+18% vs mês anterior', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR6, relief='flat',
    anchor='center', font=('Roboto 8 bold')
)
gain_revenue_label.place(x=35, y=70)


# --------------------------------------------------------------------------- #
# FRAME QUANTIDADE TOTAL


quantity_frame = Frame(
    lower_frame, width=200, height=90,
    bg=COLOR1, relief='flat'
)
quantity_frame.place(x=210, y=0)

line_label = Label(
    quantity_frame, text='', width=2, height=5,
    pady=0, padx=0, bg=COLOR2, relief='flat', anchor='nw',
    font=('Roboto 1 bold')
)
line_label.place(x=0, y=0)

quantity_label = Label(
    quantity_frame, text='Quantidade Total Vendida', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR4, relief='flat',
    anchor='center', font=('Roboto 10 bold')
)
quantity_label.place(x=20, y=5)

value_quantity_label = Label(
    quantity_frame, text='# 8,905', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR3, relief='flat',
    anchor='center', font=('Roboto 18 bold')
)
value_quantity_label.place(x=40, y=35)

gain_quantity_label = Label(
    quantity_frame, text='+18% vs mês anterior', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR6, relief='flat',
    anchor='center', font=('Roboto 8 bold')
)
gain_quantity_label.place(x=35, y=70)


# --------------------------------------------------------------------------- #
# FRAME FATURAMENTO MENSAL


monthly_frame = Frame(
    lower_frame, width=760, height=200,
    bg=COLOR1, relief='flat'
)
monthly_frame.place(x=420, y=0)

line_label = Label(
    monthly_frame, text='', width=2, height=5,
    pady=0, padx=0, bg=COLOR2, relief='flat', anchor='nw',
    font=('Roboto 1 bold')
)
line_label.place(x=0, y=0)

monthly_label = Label(
    monthly_frame, text='Faturamento Mensal', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR4, relief='flat',
    anchor='center', font=('Roboto 10 bold')
)
monthly_label.place(x=20, y=5)


# Dados para o gráfico
monthly_sales = [
    2701, 4275, 6385, 8693, 2550,
    3622, 1793, 5862, 7984, 9831,
    3739, 4584
]

months = [
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'
]


# A figura (gráfico), e os eixos
graph = plt.Figure(figsize=(11.4, 2.5), dpi=66)
ax = graph.add_subplot(111)

ax.bar(months, monthly_sales, color='#82b1ff')

c = 0

# Configura rótulos individuais para as barras.
for item in ax.patches:
    # get_x - esquerda/direita; get_height - cima/baixo
    ax.text(
        item.get_x() - .03, item.get_height() + .5,
        str(monthly_sales[c]) + 'R$', fontsize=12,
        fontstyle='italic', verticalalignment='baseline',
        color='dimgrey'
    )

    c += 1

# Personalizando o gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)

ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)


canvas = FigureCanvasTkAgg(graph, monthly_frame)
canvas.get_tk_widget().place(x=0, y=26)


# --------------------------------------------------------------------------- #
# FRAME FATURAMMENTO POR PRODUTO


product_frame = Frame(
    lower_frame, width=410, height=420,
    bg=COLOR1, relief='flat'
)
product_frame.place(x=0, y=100)

line_label = Label(
    product_frame, text='', width=2, height=5,
    pady=0, padx=0, bg=COLOR2, relief='flat', anchor='nw',
    font=('Roboto 1 bold')
)
line_label.place(x=0, y=0)

product_label = Label(
    product_frame, text='Faturamento por Produto Top - 10', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR4, relief='flat',
    anchor='center', font=('Roboto 10 bold')
)
product_label.place(x=20, y=2)


# Dados para o gráfico
products = [
    'produto - 1', 'produto - 2', 'produto - 3', 'produto - 4',
    'produto - 5', 'produto - 6', 'produto - 7', 'produto - 8',
    'produto - 9', 'produto - 10', 'produto - 11', 'produto - 12'
]


# A figura (gráfico) e os eixos
graph = plt.Figure(figsize=(8, 8), dpi=51.5)
ax = graph.add_subplot(111)

# monthly_sales -> frame faturamento mensal
ax.barh(products, monthly_sales, color='#82b1ff')
ax.set_alpha(0.8)


c = 0

# Configura rótulos individuais para as barras.
for item in ax.patches:
    ax.text(
        item.get_width() + .3, item.get_y() + .50,
        str(monthly_sales[c]) + 'R$', fontsize=12,
        verticalalignment='center', fontstyle='italic',
        color='dimgrey'
    )

    c += 1

# Personalizando o gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.xaxis.grid(False)


product_canvas = FigureCanvasTkAgg(graph, product_frame)
product_canvas.get_tk_widget().place(x=0, y=20)


# --------------------------------------------------------------------------- #
# FRAME DESEMPENHO POR CATEGORIA


category_frame = Frame(
    lower_frame, width=370, height=310,
    bg=COLOR1, relief='flat'
)
category_frame.place(x=420, y=210)

line_label = Label(
    category_frame, text='', width=2, height=5,
    pady=0, padx=0, bg=COLOR2, relief='flat', anchor='nw',
    font=('Roboto 1 bold')
)
line_label.place(x=0, y=0)

category_label = Label(
    category_frame, text='Desempenho por Categoria Top - 5', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR4, relief='flat',
    anchor='center', font=('Roboto 10 bold')
)
category_label.place(x=20, y=2)


# Vendas
totals = [5701, 4275, 8385, 5934, 6934]

# Categorias
labels = [
    'Categoria - 1', 'Categoria - 2',
    'Categoria - 3', 'Categoria - 4',
    'Categoria - 5'
]

graph = plt.Figure(figsize=(5.15, 4), dpi=70)
ax = graph.add_subplot(111)

explode = (0.1, 0.1, 0.1, 0.1, 0.1)

# Cores
colors = ['#ff9999', '#c5cae9', '#bbdefb', '#99ff99', '#ffcc99']

ax.pie(
    totals, explode=explode, wedgeprops=dict(width=0.64),
    labels=labels, colors=colors, autopct='%1.1f%%',
    shadow=True, startangle=90
)


category_canvas = FigureCanvasTkAgg(graph, category_frame)
category_canvas.get_tk_widget().place(x=0, y=20)


# --------------------------------------------------------------------------- #
# FRAME FATURAMENTO POR VENDEDORES


sellers_frame = Frame(
    lower_frame, width=380, height=310,
    bg=COLOR1, relief='flat'
)
sellers_frame.place(x=800, y=210)

line_label = Label(
    sellers_frame, text='', width=2, height=5,
    pady=0, padx=0, bg=COLOR2, relief='flat', anchor='nw',
    font=('Roboto 1 bold')
)
line_label.place(x=0, y=0)

sellers_label = Label(
    sellers_frame, text='Faturamento por Vendedor Top - 5', height=1,
    pady=0, padx=0, bg=COLOR1, fg=COLOR4, relief='flat',
    anchor='center', font=('Roboto 10 bold')
)
sellers_label.place(x=20, y=2)


graph = plt.Figure(figsize=(7.3, 4.6), dpi=57)
ax = graph.add_subplot(111)

# Vendas
sales = [2701, 4275, 6385, 8693, 3622]

# Vendedores
sellers = [
    'Vendedor - 1', 'Vendedor - 2',
    'Vendedor - 3', 'Vendedor - 4', 'Vendedor - 5'
]

colors = ['#ff9999', '#c5cae9', '#bbdefb', '#99ff99', '#ffcc99']

ax.bar(sellers, sales, color=colors)

c = 0

# Configura rótulos individuais para as barras.
for item in ax.patches:
    ax.text(
        item.get_x() - .03, item.get_height() + .5,
        str(sales[c]) + 'R$', fontsize=12, weight='bold',
        verticalalignment='baseline', fontstyle='italic',
        color='dimgrey'
    )

    c += 1

# Personalizando o gráfico
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')

ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)


sellers_canvas = FigureCanvasTkAgg(graph, sellers_frame)
sellers_canvas.get_tk_widget().place(x=0, y=20)


# --------------------------------------------------------------------------- #
# LOOP


window.mainloop()
