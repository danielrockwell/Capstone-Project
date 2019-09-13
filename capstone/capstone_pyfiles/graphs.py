import plotly.express as px
import plotly.graph_objects as plotgr
import pandas as pd


def make_bar_chart(state):
    if state == 'All' or state == "":
        data_years = pd.read_excel("../capstone_data/all_year.xlsx")
    else:
        data_years = pd.read_excel("../capstone_data/all_year.xlsx")
        data_years = data_years.query("State=='{}'".format(state))
    barChart = px.bar(data_years, x="ReportYear", y="Prepared", hover_data=['State', 'Prepared'],
                      labels={'ReportYear': 'Year of Report', 'Prepared': "Math Teachers Produced (Thousands)"})
    barChart.update_layout(
        title="Number of Math Teachers Produced by Year" if (
                state == 'All' or state == "") else "Number of Math Teachers in {} Produced by Year".format(
            state),
        title_x=.5,
        title_font_size=30,
        font_family="Open Sans",
        height=400,
    )

    barChart.update_xaxes(title_font=dict(size=25))
    barChart.update_yaxes(title_font=dict(size=25))
    return barChart


def make_US_map(year):
    if year == "":
        result = pd.read_excel("../capstone_data/all_year_abv.xlsx")
    else:
        result = pd.read_excel("../capstone_data/all_year_abv.xlsx")
        result = result.query('ProgramType == "Traditional" and ReportYear == {}'.format(year))
    fig = plotgr.Figure(
        data=plotgr.Choropleth(
            locations=result["abv"],
            z=result["Prepared"],
            locationmode="USA-states",
            colorscale='blues',
            colorbar_title="Number of Mathematics Teachers",
            colorbar_title_font_size=15,
            colorbar_title_side='right',
            colorbar_len=.75,
            colorbar_xanchor='left',
            colorbar_x=-0.1
        )
    )

    fig.update_layout(
        title=plotgr.layout.Title(
            text="{} Prepared Traditional Math Teachers by State".format(year),
            xref="paper",
            x=.5,
            y=1,
            font_family="Open Sans",
            font_size=30,
        ),
        margin=plotgr.layout.Margin(
            l=0,
            r=0,
            b=0,
            t=0, ),
        geo_scope='usa',
        autosize=True,
        height=400, )
    return fig
