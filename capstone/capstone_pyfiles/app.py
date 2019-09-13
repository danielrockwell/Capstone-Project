import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from capstone.capstone_pyfiles.graphs import make_bar_chart,make_US_map

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://fonts.googleapis.com/css?family=Raleway&display=swap']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div([
        html.H2("Mathematics Teacher Production Dashboard"),
        html.Img(src="/assets/lsu_logo.png")
    ],
        className="banner"
    ),

    html.Div([
        html.H4(""),
    ],
        className="space"
    ),
    html.Div([
        html.Div([
            dcc.Graph(id='US_map')
        ],
            className="six columns"),
        html.Div([
            dcc.Graph(id='bar_chart')
        ],
            className="six columns"),
    ], className="row"),

    html.Span([
        dcc.Input(
            id='year-input',
            placeholder="Enter Year",
            type="text",
            value=""
        ),
        html.Button(id="submit-button", n_clicks=0, children='submit')
    ], className='first-button'),
    html.Span([
        dcc.Input(
            id='usState-input',
            placeholder="Enter State or 'All'",
            type="text",
            value=""
        ),
        html.Button(id="usState-submit-button", n_clicks=0, children='submit')
    ], className='second-button'),
    html.Div([
        html.H2("@Copyright 2019 LSU Mathematics Department"),

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


@app.callback(Output("bar_ch"
                     "art", "figure"),
              [Input("usState-submit-button", "n_clicks")],
              [State("usState-input", "value")]
              )
def update_figure(n_clicks, state):
    barChart = make_bar_chart(state)
    return barChart


if __name__ == '__main__':
    app.run_server(debug=True)
