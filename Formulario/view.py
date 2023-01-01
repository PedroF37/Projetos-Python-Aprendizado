import sqlite3


# criando conexão
connection = sqlite3.connect('data.db')


def insert_data(data):
    """Função para inserir os dados na tabela."""
    with connection:
        cursor = connection.cursor()
        insertion = '''
            insert into formulario
            (nome, email, telefone, data, estado, assunto)
            values (?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(insertion, data)


def show_all():
    """Função de consulta."""
    data_list = []
    with connection:
        cursor = connection.cursor()
        query = 'select * from formulario'
        cursor.execute(query)
        response = cursor.fetchall()

        for info in response:
            data_list.append(info)

    return data_list


def update_data(data):
    """Função para atualizar dados."""
    with connection:
        cursor = connection.cursor()
        update_info = '''
            update formulario
            set nome = ?,
            email = ?,
            telefone = ?,
            data = ?,
            estado = ?,
            assunto = ?
            where id = ?
        '''
        cursor.execute(update_info, data)


def delete_data(data):
    """Função para deletar dados."""
    with connection:
        cursor = connection.cursor()
        delete_info = 'delete from formulario where id = ?'
        cursor.execute(delete_info, data)
