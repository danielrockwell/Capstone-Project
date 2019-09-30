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

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Title II Dashboard'
app.layout = html.Div(children=[
    html.Div(id="output-clientside"),
    html.Div([
        html.Div([
            html.H2("Mathematics Teacher Production Dashboard"),
        ], className="title-container"),
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
                    style={'width': 150, "font-size": 15,
                           "font-family": "'Raleway', sans-serif"},
                ),
                html.Button(id="usState-submit-button", children='Enter', n_clicks=0,
                            style={'width': 100, "font-size": 15,
                                   "font-family": "'Raleway', sans-serif"},
                            ),
            ], id='f_button'),
            html.Div([
                dcc.Dropdown(
                    id='submit-button',
                    options=[{'label': str(x), 'value': x} for x in range(2018, 2011, -1)],
                    value="",
                    placeholder="Select Year",
                    style={'width': 120, "font-size": 15,
                           "font-family": "'Raleway', sans-serif"},
                ),
            ], id='s_button')
        ], id="submit-container"),
    ],
        className="banner"
    ),

    dcc.Tabs(id="tabs-example", style={'font-size': '2vh', },
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
                         dbc.Row([
                             html.Div([
                                 html.Div([
                                     html.Div([
                                         html.H3('Program Types'),
                                         dcc.Graph(
                                             id='donut-graph',
                                             style={'height': '40vh'}),
                                     ], className="six columns", id="pie-div"),
                                     html.Div([
                                         html.H3('Program Types by Year'),
                                         dcc.Graph(
                                             id='stacked-bar',
                                             style={'height': '40vh'}),
                                     ], className="six columns", id="bar-div"),
                                 ], className="row", id="tab2-graphs")
                             ], className="ten columns offset-by-one", id="tab2_main"),
                         ]),
                         dbc.Row([
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
                                         "are the most important factors in raising student achievement.”",
                                         id="text-test"
                                     ),
                                 ], className="jumbo"
                             ),
                         ])
                     ], className="ten columns offset-by-one")
                 ]),
                 dcc.Tab(label='Title II Information', children=[
                     html.Div([
                         dbc.Row(
                             [
                                 dbc.Col([
                                     dbc.Row([
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
                                                 html.A(
                                                     html.Button("Go To Title II Website", id="title2-button"),
                                                     href='https://title2.ed.gov/Public/Home.aspx',
                                                     target="_blank"
                                                 ),
                                             ], className="jumbo"
                                         ),
                                         dbc.Row([
                                             dbc.Col([
                                                 dbc.Jumbotron(
                                                     [
                                                         html.H1("Title II", className="display-3", id="third-title"),
                                                         html.P(
                                                             "General information about Title II",
                                                             className="lead"
                                                         ),
                                                         html.Hr(className="my-3"),
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
                                                     ], className="jumbo", id="jumbo2"
                                                 ),
                                             ], width=6),
                                             dbc.Col([
                                                 dbc.Jumbotron(
                                                     [
                                                         html.H1("About This Dashboard", className="display-3",
                                                                 id="second-title"),
                                                         html.P(
                                                             "The How and Why of this Dashboard",
                                                             className="lead", id='about-sub'
                                                         ),
                                                         html.Hr(className="my-2"),
                                                         dbc.Row([
                                                             dbc.Col([
                                                                 html.P(
                                                                     "This dashboard was created in order to give insight to the "
                                                                     "enornous amount of free information available on title2.org to better teacher and leadership quality. "
                                                                     "Helpful visualizations allows data-driven decisions in order to produce the highest quality of "
                                                                     "education within the United States. With a larger emphasis and the trends within the Mathematics "
                                                                     "realm, this dashboard whas been specifiaclly tweaked to aid the Mathematics department in Louisiana.",
                                                                 ),
                                                             ], width=12),

                                                             dbc.Col([
                                                                 html.P(
                                                                     "The creation of this dashboard is primaruly built using Python, HTML, CSS, and Dash. Other "
                                                                     "popular Data Science modules that were used in the data processing were Pandas and Plotly. To view the "
                                                                     "source code for this dashboard, click on the GitHub icon to go directly to the GitHub page."
                                                                 ),
                                                             ], width=9),
                                                             dbc.Col([
                                                                 html.A(
                                                                     html.Img(src="/assets/gh_logo.png", id="gh_logo"),
                                                                     href="https://github.com/danielrockwell/Capstone-Project",
                                                                     target="_blank",
                                                                 )

                                                             ], width=3),
                                                         ])

                                                     ], className="jumbo"),
                                             ], width=6)
                                         ])
                                     ])
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
                                             style={"width": "75rem"}, color="light"
                                         )
                                     ], id="card-container")
                                 ], width={"size": 4, "offset": 1}, )
                             ],

                         ),

                     ], className="ten columns offset-by-one")
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


@app.callback(Output("donut-graph", "figure"),
              [Input("usState-submit-button", "n_clicks")],
              [State("usState-input", "value")]
              )
def update_figure(n_clicks, state):
    donut = create_donut_chart(state)
    return donut


@app.callback(Output("stacked-bar", "figure"),
              [Input("usState-submit-button", "n_clicks")],
              [State("usState-input", "value")]
              )
def update_figure(n_clicks, state):
    stack_bar = create_stacked_bar(state)
    return stack_bar


app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="resize"),
    Output("output-clientside", "children"),
    [Input("bar_chart", "figure")],
)

if __name__ == '__main__':
    app.run_server(debug=True)
