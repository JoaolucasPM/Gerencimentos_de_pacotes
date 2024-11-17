import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH/ "meu_banco.db");
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100), email VARCHAR(150))');
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email);
    cursor.execute("INSERT INTO clientes (nome, email) VALUES(?, ?);", data);
    conexao.commit();

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id);
    cursor.execute("UPDATE clientes SET nome=?, email=? where id=?;", data)
    conexao.commit();

def excluir_registro(conexao, cursor, id):
    data = (id,);
    cursor.execute("DELETE FROM clientes  where id=?;", data)
    conexao.commit();

def recuperar_cliente(curso, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes")


# cliente = recuperar_cliente(cursor, 1)
# print(cliente)

clientes = listar_clientes(cursor)
print(clientes)

for cliente in clientes:
    print(cliente)





     

