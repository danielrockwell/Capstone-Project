import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from capstone.capstone_pyfiles.graphs import make_bar_chart, make_US_map
import pandas as pd
import plotly.express as px

YEAR = 0
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://fonts.googleapis.com/css?family=Alegreya+Sans:100|Raleway:100&display=swap']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[

    html.Div([
        html.H2("Mathematics Teacher Production Dashboard"),
        html.Img(src="/assets/lsu_logo.png"),
        html.Div([
            dcc.Input(
                id='usState-input',
                placeholder="Enter State or 'All'",
                type="text",
                value="",
                style={'width': 150}
            ),
            html.Button(id="usState-submit-button",children='Enter', n_clicks=0,style={'width': 100})
        ], className='first-button'),
        html.Div([
            dcc.Input(
                id='year-input',
                placeholder="Enter Year",
                type="text",
                value="",
                style={'width': 120}
            ),
            html.Button('Enter',id="submit-button", n_clicks=0,style={'width': 100})
        ], className='second-button'),

    ],
        className="banner"
    ),

    html.Div([

        html.Div([
            html.Div([
                dcc.Graph(id='bar_chart'),
                html.Div([
                    html.P("Production of Math Teachers by Year")
                ], className="title"),

            ], className='containBar'),
        ], className="six columns"),

        html.Div([
            html.Div([
                dcc.Graph(id='US_map'),
                html.Div([
                    html.P("Production of Math Teachers by State")
                ], className="title"),

            ], className='containBar'),
        ], className="six columns"),

    ], className="row"),

    html.Div([
        html.Div([],className="spacing"),
    ], className='row'),

    html.Div([
        # html.H2("@Copyright 2019 LSU Mathematics Department"),
        html.H2("Footer")
    ],
        className="footer"
    ),

], className="all")


@app.callback(Output("US_map", "figure"),
              [Input("submit-button", "n_clicks")],
              [State("year-input", "value")]
              )
def update_figure(n_clicks, year):
    usMap = make_US_map(year)
    return usMap


@app.callback(Output("bar_chart", "figure"),
              [Input("usState-submit-button", "n_clicks")],
              [State("usState-input", "value")]
              )
def update_figure(n_clicks, state):
    barChart = make_bar_chart(state)
    return barChart


if __name__ == '__main__':
    app.run_server(debug=True)
