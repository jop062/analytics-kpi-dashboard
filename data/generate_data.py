import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

dates = pd.date_range(start_date, end_date)

customers = []

customer_id = 1

for date in dates:
    # new signups each day
    new_signups = np.random.poisson(3)

    for _ in range(new_signups):
        plan_price = random.choice([29, 49, 99])
        churn_probability = random.uniform(0.01, 0.05)

        churned = np.random.rand() < churn_probability

        churn_date = None
        if churned:
            churn_date = date + timedelta(days=random.randint(30, 300))

        customers.append({
            "customer_id": customer_id,
            "signup_date": date,
            "plan_price": plan_price,
            "churn_date": churn_date
        })

        customer_id += 1

df = pd.DataFrame(customers)
df.to_csv("database.csv", index=False)

print("Data generated successfully.")