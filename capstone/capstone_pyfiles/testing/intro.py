import pandas as pd
import plotly.graph_objects as plotgr

pd.set_option('display.expand_frame_repr', False)

file_name = "../title2_data/2018_AllStates.xlsx"
states_file = "../title2_data/states.csv"
sheet_name = "PreparedBySubject"

dfs = pd.read_excel(file_name, sheet_name=sheet_name)
dfs_states = pd.read_csv(states_file)


dfs_states=dfs_states.rename(columns={"Abbreviation": "abv"})


dfs = dfs[dfs["Category"].str.contains('Mathematics')].filter(["State", "ProgramType", "Prepared"])
dfs=dfs.groupby(["State","ProgramType"], as_index=False)["Prepared"].sum()

result = pd.merge(dfs,dfs_states,on="State",how="left")

# Traditional Math Teachers
result = result[result.ProgramType == 'Traditional']

# All Math Teachers
# result = result.filter(["abv","Prepared"])
# result = result.groupby(["abv"]).sum().reset_index()


# Export into Excel Documents
# result.to_excel("2018_all_math.xlsx", index=False)


fig = plotgr.Figure(
    data=plotgr.Choropleth(
        locations=result["abv"],
        z=result["Prepared"],
        locationmode="USA-states",
        colorscale='blues',
        colorbar_title="Number of Mathematics Teachers",
        colorbar_title_font_size=15,
        colorbar_title_side='right'
    )
)

fig.update_layout(
    title=plotgr.layout.Title(
        text="2018 Prepared Traditional Math Teachers by State",
        xref="paper",
        x=.5,
        font_family="Comic Sans",
        font_size=30
    ),
    geo_scope='usa',
    autosize=True
)

fig.show()
print(result)
