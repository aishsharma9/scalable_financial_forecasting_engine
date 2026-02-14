import sqlite3
import pandas as pd

conn = sqlite3.connect("data/financial_database.db")

df = pd.read_sql("SELECT * FROM financial_data LIMIT 5", conn)

print(df)

conn.close()
