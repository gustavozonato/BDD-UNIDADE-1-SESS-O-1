import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco REAL,
    estoque INTEGER
)
''')


produtos_data = [
    (1, 'Teclado Mecânico', 'Periféricos', 250.00, 15),
    (2, 'Mouse Gamer', 'Periféricos', 120.00, 20),
    (3, 'Monitor 24pol', 'Monitores', 850.00, 5),
    (4, 'Cadeira Office', 'Móveis', 450.00, 10),
    (5, 'Mouse Sem Fio', 'Periféricos', 80.00, 30)
]
cursor.executemany('INSERT INTO Produtos VALUES (?, ?, ?, ?, ?)', produtos_data)


print("--- Consulta Básica com WHERE e Operadores Lógicos ---")

query1 = """
SELECT nome, preco 
FROM Produtos 
WHERE categoria = 'Periféricos' AND preco > 100
"""
df1 = pd.read_sql_query(query1, conn)
print(df1, "\n")

print("--- Uso de AS (Alias) e Operadores Aritméticos ---")

query2 = """
SELECT nome AS Produto, 
       preco * estoque AS Valor_Total_Estoque 
FROM Produtos
"""
df2 = pd.read_sql_query(query2, conn)
print(df2, "\n")

print("--- Refinamento com LIKE, BETWEEN e ORDER BY ---")

query3 = """
SELECT * 
FROM Produtos 
WHERE nome LIKE 'Mouse%' 
  OR preco BETWEEN 200 AND 500
ORDER BY preco DESC
"""
df3 = pd.read_sql_query(query3, conn)
print(df3, "\n")

print("--- Uso do DISTINCT ---")

query4 = "SELECT DISTINCT categoria FROM Produtos"
df4 = pd.read_sql_query(query4, conn)
print(df4)


conn.close()
