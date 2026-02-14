import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Financial Forecasting Dashboard")

# Load data
df = pd.read_csv("data/raw/financial_data.csv")
forecast = pd.read_csv("data/processed/revenue_forecast.csv")
comparison = pd.read_csv("data/processed/model_comparison.csv")

# Convert dates
df["date"] = pd.to_datetime(df["date"])
forecast["ds"] = pd.to_datetime(forecast["ds"])

# Show raw data
st.subheader("Raw Financial Data")
st.write(df.tail())

# Plot historical revenue
st.subheader("Historical Revenue")
fig1, ax1 = plt.subplots()
ax1.plot(df["date"], df["revenue"])
ax1.set_title("Revenue Over Time")
st.pyplot(fig1)

# Plot forecast
st.subheader("Revenue Forecast")
fig2, ax2 = plt.subplots()
ax2.plot(forecast["ds"], forecast["yhat"])
ax2.set_title("Forecasted Revenue")
st.pyplot(fig2)

# Model comparison
st.subheader("Model Comparison")
st.write(comparison)

st.success("Dashboard running successfully.")
