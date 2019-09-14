import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from capstone.capstone_pyfiles.graphs import make_bar_chart, make_US_map, make_data_table
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
            html.Button(id="usState-submit-button", children='Enter', n_clicks=0, style={'width': 100})
        ], className='first-button'),
        html.Div([
            dcc.Dropdown(
                id='submit-button',
                options=[
                    {'label': '2018', 'value': 2018},
                    {'label': '2017', 'value': 2017},
                    {'label': '2016', 'value': 2016},
                    {'label': '2015', 'value': 2015},
                    {'label': '2014', 'value': 2014},
                    {'label': '2013', 'value': 2013},
                    {'label': '2012', 'value': 2012}
                ],
                value="",
                placeholder="Select Year",
                style={'width': 120}
            ),
            # dcc.Input(
            #     id='year-input',
            #     placeholder="Enter Year",
            #     type="text",
            #     value="",
            #     style={'width': 120}
            # ),
            # html.Button('Enter', id="submit-button", n_clicks=0, style={'width': 100})
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
        html.Div([
            html.Div([
                dcc.Graph(id='data_table', figure=make_data_table()),
                html.Div([
                    html.P("Teacher Production Table")
                ], className="title"),

            ], className='containBar'),
        ], className='spacing')
    ], className='row'),

    html.Div([


        html.Div([
            html.H2("My name is")
        ], id="lsu_math_site"),
    ],
        className="footer"
    ),

], className="all")


@app.callback(Output("US_map", "figure"),
              [Input("submit-button", "value")],
              )
def update_figure(year):
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
