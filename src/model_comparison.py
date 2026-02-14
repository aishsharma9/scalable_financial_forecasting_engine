import pandas as pd
import numpy as np
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error
import warnings

warnings.filterwarnings("ignore")


def load_data():
    df = pd.read_csv("data/raw/financial_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


def prophet_forecast(train, test):

    df_prophet = train[["date", "revenue"]]
    df_prophet.columns = ["ds", "y"]

    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=len(test))
    forecast = model.predict(future)

    predictions = forecast["yhat"].iloc[-len(test):].values

    return predictions


def arima_forecast(train, test):

    model = ARIMA(train["revenue"], order=(5,1,0))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=len(test))

    return forecast.values


def compare_models():

    df = load_data()

    split = int(len(df) * 0.8)

    train = df[:split]
    test = df[split:]

    prophet_pred = prophet_forecast(train, test)
    arima_pred = arima_forecast(train, test)

    prophet_mae = mean_absolute_error(test["revenue"], prophet_pred)
    arima_mae = mean_absolute_error(test["revenue"], arima_pred)

    print("\nModel Comparison Results:")
    print("-------------------------")
    print(f"Prophet MAE: {prophet_mae:.2f}")
    print(f"ARIMA   MAE: {arima_mae:.2f}")

    results = pd.DataFrame({
        "Model": ["Prophet", "ARIMA"],
        "MAE": [prophet_mae, arima_mae]
    })

    results.to_csv("data/processed/model_comparison.csv", index=False)

    print("\n✅ Results saved to data/processed/model_comparison.csv")


if __name__ == "__main__":
    compare_models()
