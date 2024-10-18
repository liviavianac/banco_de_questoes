import sqlite3

class Database:
    def __init__(self, db_name="db.sql"):
        # Conectando ao banco de dados SQLite
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def buscar_questoes(self):
        # Executa uma consulta para buscar as questões
        self.cursor.execute("SELECT id, pergunta, resposta_correta FROM questoes")
        return self.cursor.fetchall()

    def fechar_conexao(self):
        # Fecha a conexão com o banco de dados
        self.conn.close()