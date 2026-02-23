# analytics-kpi-dashboard

# Analytics KPI Dashboard

An interactive SaaS analytics dashboard built with:

- SQL (SQLite)
- Pandas
- Plotly
- Streamlit

## Features

- Total Revenue
- Customer Count
- Churn Rate
- Monthly Revenue Trend

## Run Locally

```bash
pip install -r requirements.txt
python data/generate_data.py
streamlit run src/dashboard.py