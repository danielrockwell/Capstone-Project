import glob, os
import pandas as pd
import plotly.express as plt


# pd.set_option('display.expand_frame_repr', False)
os.chdir("../title2_data")
SHEET_NAME = "PreparedBySubject"
file_name = "../title2_data/all_year.xlsx"

def create_df_by_year_pgmType(file):
    dfs = pd.read_excel(file, sheet_name=SHEET_NAME)
    dfs = dfs[dfs["Category"].str.contains('Mathematics')].filter(["State", "ReportYear","ProgramType", "Prepared"])
    dfs = dfs.groupby(["State","ReportYear","ProgramType"], as_index=False)["Prepared"].sum()
    return dfs

def create_df_all_years_pgmType():
    df_year = pd.DataFrame()
    for file in glob.glob("*.xlsx"):
        df_year = pd.concat([df_year,create_df_by_year_pgmType(file)])

def create_df_all_years():
    dfs = pd.read_excel(file_name)
    dfs = dfs.groupby(["State", "ReportYear"], as_index=False)["Prepared"].sum()
    return dfs

df_year = create_df_all_years()

# Export into Excel Documents
# df_year.to_excel("../capstone_pyfiles/all_year.xlsx", index=False)