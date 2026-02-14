import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_financial_data(days=730):
    """
    Generate synthetic financial data for 2 years.
    """
    start_date = datetime(2022, 1, 1)
    data = []

    for i in range(days):
        date = start_date + timedelta(days=i)

        # Simulated revenue and expenses
        revenue = np.random.normal(100000, 15000)
        expenses = np.random.normal(80000, 12000)

        data.append({
            "date": date,
            "revenue": max(revenue, 0),
            "expenses": max(expenses, 0)
        })

    df = pd.DataFrame(data)
    df["profit"] = df["revenue"] - df["expenses"]

    return df


if __name__ == "__main__":
    df = generate_financial_data()
    df.to_csv("data/raw/financial_data.csv", index=False)
    print("✅ Synthetic financial data generated successfully.")
