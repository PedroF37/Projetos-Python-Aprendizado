# --------------------------------------------------------------------------- #
# IMPORTAÇÕES


# tkinter
from tkinter import Tk, Frame, Label, Button, Listbox, Entry, messagebox

# db
from db import create_table, insertion, update_data
from db import query_data, delete_data


# --------------------------------------------------------------------------- #
# CORES


COLOR0 = '#000000'  # Preto
COLOR1 = '#59656F'
COLOR2 = '#feffff'  # Branco
COLOR3 = '#0074eb'  # Azul
COLOR4 = '#f04141'  # Vermelho
COLOR5 = '#59b356'  # Verde
COLOR6 = '#cdd1cd'  # Cinza


# --------------------------------------------------------------------------- #
# FUNÇÕES


def show_tasks():
    """Função que cuida de mostrar as tarefas."""
    listbox.delete(0, 'end')
    tasks = query_data()
    for task in tasks:
        listbox.insert('end', task[1])


def choose_action(action):
    """Função que cuida dos botões 'novo' e 'atualizar'."""
    if action == 'Novo':

        for widget in lower_left_frame.winfo_children():
            widget.destroy()

        def add_task():
            task_to_add = new_task_entry.get()
            insertion([task_to_add])
            new_task_entry.delete(0, 'end')
            show_tasks()

        task_label = Label(
            lower_left_frame, text='Insira nova tarefa',
            width=40, height=5, pady=15, font=('Roboto 11 bold'),
            anchor='center'
        )
        task_label.grid(row=0, column=0, sticky='nsew')

        new_task_entry = Entry(
            lower_left_frame,
            width=15, justify='center'
        )
        new_task_entry.grid(
            row=1, column=0,
            sticky='nsew', pady=0,
            padx=0
        )

        add_new_task_button = Button(
            lower_left_frame, text='ADICIONAR', width=10,
            height=1, anchor='center', pady=5,
            font=('Roboto 11 bold'), relief='raised',
            command=add_task
        )
        add_new_task_button.grid(
            row=2, column=0,
            sticky='nsew', pady=0, padx=0
        )

    elif action == 'Atualizar':

        for widget in lower_left_frame.winfo_children():
            widget.destroy()

        def on_update_button():
            update_task_label = Label(
                lower_left_frame, text='Atualizar tarefa',
                width=40, height=5, pady=15, font=('Roboto 11 bold'),
                anchor='center'
            )
            update_task_label.grid(row=0, column=0, sticky='nsew')

            update_task_entry = Entry(
                lower_left_frame,
                width=15, justify='center'
            )
            update_task_entry.grid(
                row=1, column=0,
                sticky='nsew', pady=0,
                padx=0
            )

            selected_task = listbox.curselection()
            update_task_entry.insert(0, listbox.get(selected_task))
            tasks = query_data()

            def update_task():
                for task in tasks:
                    if listbox.get(selected_task) == task[1]:
                        update_data([update_task_entry.get(), task[0]])
                        update_task_entry.delete(0, 'end')

                show_tasks()

            update_task_button = Button(
                lower_left_frame, text='ATUALIZAR', width=10,
                height=1, anchor='center', pady=5,
                font=('Roboto 11 bold'), relief='raised',
                command=update_task
            )
            update_task_button.grid(
                row=2, column=0,
                sticky='nsew', pady=0, padx=0
            )

        on_update_button()


def delete_task():
    """Função que cuida de deletar tarefa."""
    selected_task = listbox.curselection()
    tasks = query_data()

    for task in tasks:
        if listbox.get(selected_task) == task[1]:
            delete_data([task[0]])  # ou: delete_data(str(task[0]))

    show_tasks()


# --------------------------------------------------------------------------- #
# JANELA


# Apenas cria se não existir
create_table()


window = Tk()
window.title('To-do App')
window.resizable(0, 0)
window.geometry('600x210')
window.configure(bg=COLOR1)


# --------------------------------------------------------------------------- #
# FRAMES


left_frame = Frame(window, width=300, height=210, bg=COLOR2, relief='flat')
left_frame.grid(row=0, column=0, sticky='nsew')

right_frame = Frame(window, width=300, height=210, bg=COLOR2, relief='flat')
right_frame.grid(row=0, column=1, sticky='nsew')

upper_left_frame = Frame(
    left_frame, width=300,
    height=75, bg=COLOR2, relief='flat'
)
upper_left_frame.grid(row=0, column=0, sticky='nsew')

lower_left_frame = Frame(
    left_frame, width=300,
    height=135, bg=COLOR2, relief='flat'
)
lower_left_frame.grid(row=1, column=0, sticky='nsew')


# --------------------------------------------------------------------------- #
# BOTÕES


new_button = Button(
    upper_left_frame, text='Novo', width=10,
    height=1, bg=COLOR3, fg='white', anchor='center',
    relief='raised', activebackground=COLOR3, font=('Roboto 10 bold'),
    activeforeground='white', command=lambda: choose_action('Novo')

)
new_button.grid(row=0, column=0, sticky='nsew', pady=1)

remove_button = Button(
    upper_left_frame, text='Remover', width=10,
    height=1, bg=COLOR4, fg='white', anchor='center',
    relief='raised', activebackground=COLOR4, font=('Roboto 10 bold'),
    activeforeground='white', command=delete_task

)
remove_button.grid(row=0, column=1, sticky='nsew', pady=1)

update_button = Button(
    upper_left_frame, text='Atualizar', width=10,
    height=1, bg=COLOR5, fg='white', anchor='center',
    relief='raised', activebackground=COLOR5, font=('Roboto 10 bold'),
    activeforeground='white', command=lambda: choose_action('Atualizar')

)
update_button.grid(row=0, column=2, sticky='nsew', pady=1)


# --------------------------------------------------------------------------- #
# LABELS


task_label = Label(
    right_frame, text='Tarefas',
    width=37, height=1, pady=7,
    padx=10, relief='flat', anchor='w',
    font=('Roboto 20 bold'), fg=COLOR0,
    bg=COLOR2
)
task_label.grid(row=0, column=0, sticky='nsew', pady=1)


# --------------------------------------------------------------------------- #
# LISTBOXES


listbox = Listbox(right_frame, font=('Roboto 9 bold'), width=1, height=14)
listbox.grid(row=1, column=0, sticky='nsew', pady=5)


# --------------------------------------------------------------------------- #
# LOOP

show_tasks()
window.mainloop()
