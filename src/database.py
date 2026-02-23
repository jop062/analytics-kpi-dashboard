import sqlite3
import pandas as pd

def load_data():
    df = pd.read_csv("database.csv", parse_dates=["signup_date", "churn_date"])
    return df

def create_database():
    conn = sqlite3.connect("database.db")
    df = load_data()
    df.to_sql("customers", conn, if_exists="replace", index=False)
    conn.close()