#import the DASH library
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import seaborn as sns
import pandas as pd

# initialize DASH by creating an app
app=dash.Dash(__name__)
app.layout=html.Div(
    children=[
        html.H1(children='PyVisLab: visualize data dashboard'),
        html.P(children='This dashboard can be used to visualize your data in various kind of graphs. ')
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

