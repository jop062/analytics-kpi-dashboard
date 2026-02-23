import streamlit as st
import plotly.express as px
from database import create_database
from kpis import total_revenue, total_customers, churn_rate, monthly_revenue

st.set_page_config(page_title="Analytics KPI Dashboard", layout="wide")

# Ensure DB exists
create_database()

st.title("📊 SaaS Analytics Dashboard")

# KPI Cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue():,.0f}")
col2.metric("Total Customers", f"{total_customers():,}")
col3.metric("Churn Rate", f"{churn_rate()*100:.2f}%")

st.divider()

# Revenue Trend
st.subheader("Monthly Revenue Trend")
df = monthly_revenue()

fig = px.line(
    df,
    x="month",
    y="revenue",
    markers=True,
)

st.plotly_chart(fig, use_container_width=True)