import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction
from capstone.capstone_pyfiles.graphs import make_bar_chart, make_US_map, make_data_table, create_donut_chart, \
    create_stacked_bar
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://fonts.googleapis.com/css?family=Alegreya+Sans:100|Raleway:100&display=swap',
                        dbc.themes.BOOTSTRAP, ]

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Demo",
    brand_href="#",
    sticky="top",
)

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            """\
                Donec id elit non mi porta gravida at eget metus.
                Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
                nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
                malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
                mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
                commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
                amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
                odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Title II Dashboard'
app.layout = html.Div(children=[
    html.Div(id="output-clientside"),
    html.Div([
        html.H2("Mathematics Teacher Production Dashboard"),
        html.Div([
            html.Img(src="/assets/lsu_logo.png", id="img_in_flex"),
        ], id="img-flex"),
        html.Div([
            html.Div([
                dcc.Input(
                    id='usState-input',
                    placeholder="Enter State or 'All'",
                    type="text",
                    value="",
                    style={'width': 150, },
                ),
                html.Button(id="usState-submit-button", children='Enter', n_clicks=0, style={'width': 100})
            ], id='f_button'),
            html.Div([
                dcc.Dropdown(
                    id='submit-button',
                    options=[{'label': str(x), 'value': x} for x in range(2018, 2011, -1)],
                    value="",
                    placeholder="Select Year",
                    style={'width': 120}
                ),
            ], id='s_button')
        ], id="submit-container"),
    ],
        className="banner"
    ),

    dcc.Tabs(id="tabs-example", style={'font-size': '300%', },
             children=[
                 dcc.Tab(id="tab1", label='Teacher Production Graphs',
                         children=[
                             html.Div([
                                 html.Div([
                                     html.Div([
                                         html.H3("Production of Math Teachers by Year"),
                                         dcc.Graph(id='bar_chart',
                                                   style={'height': '40vh'}),
                                     ], className="six columns", id="barchart-div"),

                                     html.Div([
                                         html.H3("Production of Math Teachers by State"),
                                         dcc.Graph(id='US_map',
                                                   style={'height': '40vh'}),
                                     ], className="six columns", id="map-div"),

                                     html.Div([
                                         html.H3("Teacher Production Table"),
                                         dcc.Graph(id='data_table',
                                                   style={'height': '50vh'}),
                                     ], className="twelve columns", id="table-div"),
                                 ], className="row", id="tab1-graphs")
                             ], className="ten columns offset-by-one")
                         ]),
                 dcc.Tab(label='Analysis and Statistics', children=[
                     html.Div([
                         html.Div([
                             html.Div([
                                 html.H3('Program Types'),
                                 dcc.Graph(
                                     id='donut-graph',
                                     figure=create_donut_chart()
                                 ),
                             ], className="six columns", id="pie-div"),
                             html.Div([
                                 html.H3('Program Types by Year'),
                                 dcc.Graph(
                                     id='stacked-bar',
                                     figure=create_stacked_bar()
                                 ),
                             ], className="six columns", id="bar-div"),
                         ], className="row", id="tab2-graphs")
                     ], className="ten columns offset-by-one", id="tab2_main")
                 ]),
                 dcc.Tab(label='Title II Information', children=[
                     html.Div([
                         dbc.Row(
                             [
                                 dbc.Col([
                                     dbc.Jumbotron(
                                         [
                                             html.H1("Title II", className="display-3"),
                                             html.P(
                                                 "General information about Title II",
                                                 className="lead",
                                             ),
                                             html.Hr(className="my-2"),
                                             html.P(
                                                 "According to Scholastic.com, The Every Student Succeeds Act (ESSA) is the most recent reauthorization of the 1965 act "
                                                 "that establishes the federal government’s role in education. Under ESSA, Title II authorizes "
                                                 "programs to improve teaching and leadership through professional learning at the state and district "
                                                 "levels. Under ESSA, professional development is more clearly defined and there are rules for evidence "
                                                 "of learning. Specifically, Title II Part A is used to increase academic achievement of students by "
                                                 "improving teachers and school leadership quality. You can read the Title II Part A details on the "
                                                 "U.S. Department of Education’s website. As stated in Learning Forward’s report Why Professional "
                                                 "Development Matters, “In education, research has shown that teaching quality and school leadership "
                                                 "are the most important factors in raising student achievement.”"
                                             ),
                                             dbc.Button("Learn mores", size="lg", color="primary", ),
                                         ], id="jumbo"
                                     )
                                 ], width=7),

                                 dbc.Col([
                                     html.Div([
                                         dbc.Card(
                                             [
                                                 dbc.CardImg(src="/assets/title2_img.png", top=True),
                                                 dbc.CardBody(
                                                     html.P("Image from the Title Website", id="card-text")
                                                 ),
                                             ],
                                             style={"width": "75rem"},
                                         )
                                     ],id="card-container")
                                     #     html.Div(
                                     #         [
                                     #             html.Img(src="/assets/title2_img.png", id="title-img"),
                                     #             html.H2("Title II Information Website",id="title2-text"),
                                     #         ],className="img-cont")
                                     #
                                 ], width={"size": 4, "offset": 1}, )
                             ]
                         )
                     ], className="ten columns offset-by-one")
                     # html.Div([
                     #     html.H3('Tab content 3'),
                     #     dcc.Graph(
                     #         id='graph-2-tab',
                     #         figure=create_donut_chart(),
                     #     )
                     # ]),
                 ]),
             ]),

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


app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("bar_chart", "figure")],
)

if __name__ == '__main__':
    app.run_server(debug=True)
