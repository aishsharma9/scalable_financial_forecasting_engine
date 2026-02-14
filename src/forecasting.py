import pandas as pd
from prophet import Prophet


def run_forecast():
    """
    Load financial data and generate revenue forecast.
    """

    # Load data
    df = pd.read_csv("data/raw/financial_data.csv")

    # Prepare data for Prophet
    df_prophet = df[["date", "revenue"]]
    df_prophet.columns = ["ds", "y"]

    # Convert date column
    df_prophet["ds"] = pd.to_datetime(df_prophet["ds"])

    print("Training forecasting model...")

    # Create model
    model = Prophet()

    # Train model
    model.fit(df_prophet)

    # Create future dates (90 days forecast)
    future = model.make_future_dataframe(periods=90)

    # Generate forecast
    forecast = model.predict(future)

    # Save output
    forecast.to_csv("data/processed/revenue_forecast.csv", index=False)

    print("✅ Forecast generated successfully.")


if __name__ == "__main__":
    run_forecast()
