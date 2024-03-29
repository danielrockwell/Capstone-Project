import plotly.express as px
import plotly.graph_objects as plotgr
import pandas as pd


def make_bar_chart(state):
    if state == 'All' or state == "":
        data_years = pd.read_excel("../capstone_data/all_year.xlsx")
    else:
        data_years = pd.read_excel("../capstone_data/all_year.xlsx")
        data_years = data_years.query("State=='{}'".format(state))
    barChart = px.bar(data_years,
                      x="ReportYear", y="Prepared",
                      hover_data=['State', 'Prepared'],
                      labels={'ReportYear': "{}".format(state), 'Prepared': ""}
                      )
    barChart.update_layout(
        font_family="Open Sans",
        autosize=True,
        margin={"l": 0,
                "r": 40,
                "t":0,
                "b":0},
        plot_bgcolor='rgba(0,0,0,0)',

    )

    barChart.update_xaxes(title_font=dict(size=25))
    barChart.update_yaxes(title_font=dict(size=25))
    return barChart


def make_US_map(year):
    if year == "":
        result = pd.read_excel("../capstone_data/all_year_abv.xlsx")
        result = result.query('ProgramType == "Traditional" and ReportYear == 2018')

    else:
        result = pd.read_excel("../capstone_data/all_year_abv.xlsx")
        result = result.query('ProgramType == "Traditional" and ReportYear == {}'.format(year))
    fig = plotgr.Figure(
        data=plotgr.Choropleth(
            locations=result["abv"],
            z=result["Prepared"],
            locationmode="USA-states",
            colorscale='blues',
            colorbar_title="Year: {}".format(year) if year != "" else "",
            colorbar_title_font_size=15,
            colorbar_title_side='bottom',
            colorbar_len=.65,
            colorbar_xanchor='left',
            colorbar_x=-0.2,
            colorbar_xpad=50,
        )
    )

    fig.update_layout(
        margin=plotgr.layout.Margin(
            l=0,
            r=0,
            b=70,
            t=0),
        geo_scope='usa',
        autosize=True,
    )
    return fig


def make_data_table(state):
    if state == 'All' or state == "":
        df = pd.read_excel('../capstone_data/master_subject.xlsx')
    else:
        df = pd.read_excel('../capstone_data/master_subject.xlsx')
        df = df.query("State=='{}'".format(state))
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    fig = plotgr.Figure(data=[plotgr.Table(

        header=dict(values=list(df.columns),
                    line_color='darkslategray',
                    fill_color=headerColor,
                    align=['left', 'center'],
                    font=dict(color='white', size=12)),

        cells=dict(values=[df.State, df.ReportYear, df.ProgramType, df.Category, df.Prepared],
                   line_color='darkslategray',
                   fill_color=[[rowOddColor, rowEvenColor, rowOddColor, rowEvenColor] * (len(df) // 4)],
                   align=['left', 'center'],
                   font=dict(color='darkslategray', size=11)))
    ])

    fig.update_layout(
        margin=plotgr.layout.Margin(
            l=20,
            r=20,
            b=20,
            t=20),
        autosize=True,

    )

    return fig


def create_donut_chart():
    dfs = pd.read_excel("../capstone_data/program_count.xlsx")
    dfs = dfs.query("State == 'Louisiana' and ReportYear==2018")

    labels = dfs["ProgramType"]
    values = dfs["counts"]

    fig = plotgr.Figure(data=[plotgr.Pie(labels=labels, values=values, hole=.6)])

    fig.update_traces(textinfo='value')

    fig.update_layout(
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='Program Type', x=0.5, y=0.5, font_size=20, showarrow=False)],
        legend=dict(x=-.1, y=1),
        margin=plotgr.layout.Margin(
            l=10,
            r=10,
            b=10,
            t=10),
    )

    return fig


def create_stacked_bar():
    dfs = pd.read_excel("../capstone_data/program_count.xlsx")
    dfs = dfs.groupby(['ReportYear', 'ProgramType'], as_index=False)['counts'].sum()
    # print(dfs)
    df2 = dfs[dfs["ProgramType"] == "Alternative, IHE-based"]
    df1 = dfs[dfs["ProgramType"] == "Traditional"]
    df3 = dfs[dfs["ProgramType"] == "Alternative, not IHE-based"]

    fig = plotgr.Figure(data=[
        plotgr.Bar(name='Traditional', x=df1["ReportYear"], y=df1["counts"]),
        plotgr.Bar(name='Alternative, IHE-based', x=df2["ReportYear"], y=df2["counts"]),
        plotgr.Bar(name='Alternative, not IHE-based', x=df3["ReportYear"], y=df3["counts"])
    ])
    # Change the bar mode
    fig.update_layout(barmode='stack',
                      margin=plotgr.layout.Margin(
                          l=10,
                          r=10,
                          b=10,
                          t=10),
                      plot_bgcolor='rgba(0,0,0,0)'
                      )
    return fig
