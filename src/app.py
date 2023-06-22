# importing the libraries
import pandas as pd 
import dash
from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output, State
import plotly.express as px

#reading the data
df =pd.read_csv('stock_data.csv')
df['Ticker'].unique()

# webapp
app= dash.Dash()
server = app.server
dropdown = dcc.Dropdown(['AAPL', 'MSFT', 'TSLA'], "TSLA", clearable=False)

graph = dcc.Graph() # figure={}

app.layout = html.Div([html.H4("Stock graphs with Dash"), dropdown, graph])


@callback(
    Output(graph, "figure"), 
    Input(dropdown, "value")
)
def update_line_chart(ticker): # whenever we choose a different ticker it should update the graph
    mask = df["Ticker"] == ticker # coming from the function parameter
    fig = px.line(df[mask], x="Date", y="Close")
    return fig # whatever you are returning here is connected to the component property of the output which is figure

if __name__ == "__main__":
    app.run_server()


