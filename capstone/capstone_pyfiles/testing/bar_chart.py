import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from capstone.capstone_pyfiles.testing.data_cleaning import create_df_all_years

data_years = pd.read_excel("../../capstone_data/all_year.xlsx")
data_years=data_years.query("State=='Louisiana'")
fig = px.bar(data_years, x="ReportYear", y="Prepared", hover_data=['State', 'Prepared'],
             labels={'ReportYear': 'Year of Report', 'Prepared': "Math Teachers Produced (in Thousands)"},
             title="Number of Math Teachers Produced by Year")

fig.update_layout(
    title_x=.5,
    title_font_size=40,
    font_family="Comic Sans",
    # updatemenus=[
    #     go.layout.Updatemenu(
    #         buttons=list([
    #             dict(
    #                 args=[],
    #                 label="All",
    #                 method="restyle"
    #             ), dict(
    #                 args=["State", "Prepared"],
    #                 label="Louisiana",
    #                 method="restyle"
    #             )
    #         ]),
    #         direction="down",
    #         showactive=True,
    #         xanchor='left',
    #         x=0,
    #         yanchor='bottom',
    #
    #     ),
    # ],
    margin_l=200,
    margin_r=100
)

fig.update_xaxes(title_font=dict(size=20))
fig.update_yaxes(title_font=dict(size=20))

fig.show()

# if state == 'All' or state == "":
#     data_years = pd.read_excel("../capstone_data/all_year.xlsx")
# else:
#     data_years = pd.read_excel("../capstone_data/all_year.xlsx")
#     data_years = data_years.query("State=='{}'".format(state))
# barChart = px.bar(data_years,
#                   x="ReportYear", y="Prepared",
#                   hover_data=['State', 'Prepared'],
#                   labels={'ReportYear': "{}".format(state), 'Prepared': "Teachers (in Thousands)"}
#                   )
# barChart.update_layout(
#     # title="Number of Math Teachers Produced by Year" if (
#     #         state == 'All' or state == "") else "Number of Math Teachers in {} Produced by Year".format(
#     #     state),
#     # title_x=.5,
#     # title_font_size=70,
#     font_family="Open Sans",
#     autosize=True,
#     # margin={"l": 0,
#     #         "r": 0,
#     #         "t":0,
#     #         "b":0},
#     plot_bgcolor='rgba(0,0,0,0)',
#
# )
#
# # barChart.update_xaxes(title_font=dict(size=25))
# # barChart.update_yaxes(title_font=dict(size=25))
# return barChart