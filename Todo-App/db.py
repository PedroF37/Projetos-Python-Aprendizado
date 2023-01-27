import sqlite3


# Conexão
connection = sqlite3.connect('tasks.db')


# Tabela
def create_table():
    """Função que cria a tabela."""
    with connection:
        cursor = connection.cursor()
        cursor.execute('''
            create table if not exists tarefas(
                id integer primary key,
                nome text
            )
        ''')


def insertion(data):
    """Função que insere os dados na tabela."""
    with connection:
        cursor = connection.cursor()
        insertion = 'insert into tarefas (nome) values (?)'
        cursor.execute(insertion, data)


def update_data(record):
    """Função para atualizar registros na tabela."""
    with connection:
        cursor = connection.cursor()
        update = 'update tarefas set nome = (?) where id = (?)'
        cursor.execute(update, record)



def query_data():
    """Função que consulta os dados na tabela."""
    tasks = list()
    with connection:
        cursor = connection.cursor()
        query = 'select * from tarefas'
        cursor.execute(query)

        records = cursor.fetchall()
        for record in records:
            tasks.append(record)

    return tasks


def delete_data(id):
    """Função que deleta dados na tabela."""
    with connection:
        cursor = connection.cursor()
        deletion = 'delete from tarefas where id = (?)'
        cursor.execute(deletion, id)
