import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pmdarima.arima import auto_arima
import plotly.graph_objs as go
import plotly.io as pio
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
import time

axis_dict = {
    "Da": "Date",
    "D": "Dollar",
    "E": "Euro"
}


def monthly_prediction_func(csv_name, axis_one, axis_two, pred_time):
    time_start = time.time()
    print("Start | Elapsed time:", time_start)

    data = pd.read_csv(csv_name, sep=";")
    axis_one, axis_two = axis_dict[axis_one], axis_dict[axis_two]

    data["Date"] = pd.to_datetime(data["Date"], format="ISO8601")
    data['Year'] = data['Date'].dt.year
    data["Month"] = data["Date"].dt.month

    print("Start auto arima | Elapsed time:", time.time() - time_start)

    model = auto_arima(data[axis_two], seasonal=True, m=pred_time, suppress_warnings=True)
    p, d, q = model.order

    print("Start SARIMAX | Elapsed time:", time.time() - time_start)

    model = SARIMAX(data[axis_two], order=(p, d, q),
                    seasonal_order=(p, d, q, 31))
    fitted = model.fit()
    predictions = fitted.predict(len(data), len(data) + 60)

    time_end = time.time()
    print("Successful | Elapsed time:", time_end - time_start)
    return (data.index, data[axis_two], predictions, axis_one, axis_two)


def open_plot(data_index_gr, data_axis_two_gr, predictions_gr, axis_one_gr, axis_two_gr):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data_index_gr,
        y=data_axis_two_gr,
        mode='lines',
        name='Training Data',
        line=dict(color='blue')
    ))

    fig.add_trace(go.Scatter(
        x=predictions_gr.index,
        y=predictions_gr,
        mode='lines',
        name='Predictions',
        line=dict(color='green')
    ))

    fig.update_layout(
        title=f"{axis_one_gr} prediction",
        xaxis_title=axis_two_gr,
        yaxis_title=axis_one_gr,
        legend_title="Data",
        width=1000,
        height=600
    )
    with open("graph.html", "w") as f:
        f.writelines(pio.to_html(fig))
    pio.show(fig)


if __name__ == '__main__':
    data_index, data_axis_two, predictions, axis_one, axis_two = monthly_prediction_func(
        "data/stavka_cb.csv",
        "Da",
        "E",
        pred_time=52,
    )
    open_plot(data_index, data_axis_two, predictions, axis_one, axis_two)