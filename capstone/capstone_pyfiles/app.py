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
app.title = 'Title II Dashboard'
app.layout = html.Div(children=[

    html.Div([
        html.H2("Mathematics Teacher Production Dashboard"),
        html.Img(src="/assets/lsu_logo.png"),

        html.Div([
            dcc.Dropdown(
                id='submit-button',
                options=[{'label': str(x), 'value': x} for x in range(2018, 2011, -1)],
                value="",
                placeholder="Select Year",
                style={'width': 120}
            ),
        ], className='second-button'),

        html.Div([
            dcc.Input(
                id='usState-input',
                placeholder="Enter State or 'All'",
                type="text",
                value="",
                style={'width': 150},
            ),
            html.Button(id="usState-submit-button", children='Enter', n_clicks=0, style={'width': 100})
        ], className='first-button'),

    ],
        className="banner"
    ),

    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Tab One', value='tab-1-example'),
        dcc.Tab(label='Tab Two', value='tab-2-example'),
    ]),
    html.Div(id='tabs-content-example'),

    html.Div([
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
                    dcc.Graph(id='data_table'),
                    html.Div([
                        html.P("Teacher Production Table")
                    ], className="title"),

                ], className='containBar'),
            ], className='spacing')
        ], className='row'),
    ], id="testing"),

    html.Div([

        html.Div([
            html.H2("@Copyright 2019 LSU Mathematics Department")
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


@app.callback(Output("data_table", "figure"),
              [Input("usState-submit-button", "n_clicks")],
              [State("usState-input", "value")]
              )
def update_figure(n_clicks, state):
    data_table = make_data_table(state)
    return data_table


@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return html.Div([
            html.H3('Tab content 1'),
            dcc.Graph(
                id='graph-1-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'tab-2-example':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
