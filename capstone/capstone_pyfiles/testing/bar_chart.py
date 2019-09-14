import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from capstone.capstone_pyfiles.testing.visuals import create_df_all_years

data_years = create_df_all_years()
data_years=data_years.query("State=='Louisiana'")
print(data_years)
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

# fig.show()
