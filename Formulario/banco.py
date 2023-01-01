import sqlite3


# Criando conexão
connection = sqlite3.connect('data.db')

# Criando tabela
with connection:
    cursor = connection.cursor()
    cursor.execute(
        '''create table formulario(
                id integer primary key autoincrement,
                nome text,
                email text,
                telefone text,
                data DATE,
                estado text,
                assunto text
        )'''
    )
