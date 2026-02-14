import pandas as pd
import sqlite3


def load_data_to_database():

    # Read CSV data
    df = pd.read_csv("data/raw/financial_data.csv")

    # Connect to SQLite database
    conn = sqlite3.connect("data/financial_database.db")

    # Load into SQL table
    df.to_sql("financial_data", conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Data loaded into SQL database successfully.")


if __name__ == "__main__":
    load_data_to_database()
