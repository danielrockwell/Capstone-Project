# Capstone Project

This project utilizes the data collected from from Title II from the Higher Education Act to analyze the future of Mathematics Education Learning. This is made possible by the following:

* Agrregated, cleaned, and transformed data from Title II source.
* Integrated open source software to manipulate data into usable formatting.
* Created a dashboard using tools such as Dash, Pandas, Plotly to analyze the education data released from 2012-2018.

<p align="center">
  <img src="/dashboardV1.png" alt="Dashboard Version 1" width="738">
</p>

## Tools/Languages Used with Examples:

Python modules are needed to use this application

1. `pandas` is used to manipulate excel spreadsheets:

   ```py
    import pandas as pd
    file_name = "../title2_data/2018_AllStates.xlsx"
    states_file = "../title2_data/states.csv"
    sheet_name = "PreparedBySubject"

    dfs = pd.read_excel(file_name, sheet_name=sheet_name)
   ```

2. `plotly` and `dash` are used to make the visualizations and dashboard:

   ```py
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Output, Input, State
   ```

3. Other programming/scripting languages, such as `CSS` and `HTML` are used to create and style the dashboard:

   ```css
    .banner Img {
        position=relative;
        float: right;
        height: 55px;
        padding-top: 0.8%;
        padding-right: 1%;
     }
   ```
