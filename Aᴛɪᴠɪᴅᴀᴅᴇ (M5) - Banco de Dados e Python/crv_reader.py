import csv

def inserir_de_csv(self, file_name='csv/clientes.csv'):
    try:
        reader = csv.reader(
            open(file_name, 'rt'), delimiter=',')
        linha = (reader,)
        for linha in reader:
            self.db.cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", linha)
            # gravando no bd
        self.db.commit_db()
        print("Dados importados do csv com sucesso.")
    except sqlite3.IntegrityError:
        print("Aviso: O email deve ser único.")
        return False
