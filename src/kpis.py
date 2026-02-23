import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("database.db")

def total_revenue():
    conn = get_connection()
    query = """
    SELECT SUM(plan_price) as revenue
    FROM customers
    WHERE churn_date IS NULL
    """
    result = pd.read_sql(query, conn)
    conn.close()
    return result["revenue"][0]

def total_customers():
    conn = get_connection()
    query = "SELECT COUNT(*) as count FROM customers"
    result = pd.read_sql(query, conn)
    conn.close()
    return result["count"][0]

def churn_rate():
    conn = get_connection()
    query = """
    SELECT 
        SUM(CASE WHEN churn_date IS NOT NULL THEN 1 ELSE 0 END) * 1.0 /
        COUNT(*) as churn_rate
    FROM customers
    """
    result = pd.read_sql(query, conn)
    conn.close()
    return result["churn_rate"][0]

def monthly_revenue():
    conn = get_connection()
    query = """
    SELECT 
        strftime('%Y-%m', signup_date) as month,
        SUM(plan_price) as revenue
    FROM customers
    GROUP BY month
    ORDER BY month
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df