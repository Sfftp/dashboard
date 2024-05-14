import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
from .stocks_companies import st_rt

app = DjangoDash("Simple_example")


import plotly.express as px




app.layout = html.Div([
    html.H4('Stock price analysis'),
    dcc.Graph(id="time-series-chart"),
    html.P("Select stock:"),
    dcc.Dropdown(
        id="ticker",
        options=["AAPL", "AMD", "TSLA", "NVDA", "AMZN"],
        value="APPL",
        clearable=False,
    ),
])


@app.callback(
    Output("time-series-chart", "figure"),
    Input("ticker", "value"))
def display_time_series(ticker):
    df = st_rt(ticker, 's')
    fig = px.line(df, x="", y='Close')
    return fig

