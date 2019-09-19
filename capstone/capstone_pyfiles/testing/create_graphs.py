import glob, os
import pandas as pd
import plotly.express as plt
import plotly.graph_objects as go

file_name = "../../capstone_data/program_count.xlsx"

# os.chdir("../../capstone_data/AllState_original/")
# SHEET_NAME = "Program"

#
# def master_program(file):
#     dfs = pd.read_excel(file, sheet_name=SHEET_NAME)
#     dfs = dfs[['State','ProgramType',"ReportYear"]]
#     dfs = dfs.groupby(['State',"ReportYear", 'ProgramType']).size().reset_index(name='counts')
#     return dfs
#
#
# def create_df_all_pgmType_by_State():
#     df_year = pd.DataFrame()
#     for file in glob.glob("*.xlsx"):
#         df_year = pd.concat([df_year,master_program(file)])
#     return df_year
#
#
# res=create_df_all_pgmType_by_State()
# res.to_excel("../../capstone_data/program_count.xlsx", index=False)


## Pie Chart
# dfs = pd.read_excel(file_name)
#
# dfs=dfs.query("State == 'Louisiana' and ReportYear==2018")
#
# labels = dfs["ProgramType"]
# values = dfs["counts"]
# #
# # Use `hole` to create a donut-like pie chart
# fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6)])
#
# fig.update_traces(textinfo='value')
# fig.show()




## Create Bar Chart
dfs = pd.read_excel(file_name)
dfs = dfs.groupby(['ReportYear', 'ProgramType'], as_index=False)['counts'].sum()
# print(dfs)
df2 = dfs[dfs["ProgramType"] == "Alternative, IHE-based"]
df1 = dfs[dfs["ProgramType"] == "Traditional"]
df3 = dfs[dfs["ProgramType"] == "Alternative, not IHE-based"]


fig = go.Figure(data=[
    go.Bar(name='Traditional', x=df1["ReportYear"], y=df1["counts"]),
    go.Bar(name='Alternative, IHE-based', x=df2["ReportYear"], y=df2["counts"]),
    go.Bar(name='Alternative, not IHE-based', x=df3["ReportYear"], y=df3["counts"])
])
# Change the bar mode
fig.update_layout(barmode='stack')
fig.show()
