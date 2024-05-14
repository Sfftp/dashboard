import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
from django_plotly_dash import DjangoDash
import pandas as pd

app = DjangoDash("Simple_example")

df = pd.read_csv('stavka_cb.csv')
fig = go.Figure([go.Scatter(x=df['Date'], y=df['Rate'])])


app.layout = html.Div(children=[
    html.H1(children="Ставка центрального банка"),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


