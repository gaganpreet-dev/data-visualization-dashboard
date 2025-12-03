import pandas as pd
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px

def load_sample():
    return pd.read_csv('data/sample_sales.csv', parse_dates=['Date'])

df = load_sample()

app = Dash(__name__)
app.title = "Data Visualization Dashboard"

categories = sorted(df['Category'].unique())
regions = sorted(df['Region'].unique())

app.layout = html.Div([
    html.H1("Data Visualization Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.Label("Select Category"),
            dcc.Dropdown(options=[{'label': c, 'value': c} for c in categories], value=categories[0], id='category'),
            html.Label("Select Region"),
            dcc.Dropdown(options=[{'label': r, 'value': r} for r in regions] + [{'label': 'All', 'value': 'All'}], value='All', id='region'),
            html.Label("Upload CSV (optional)"),
            dcc.Upload(id='upload-data', children=html.Div(['Drag and Drop or ', html.A('Select Files')]), multiple=False, style={'width':'100%','height':'60px','border':'1px dashed #aaa','textAlign':'center','padding':'10px','marginTop':'10px'}),
        ], style={'width':'25%','display':'inline-block','verticalAlign':'top','padding':'20px'}),
        html.Div([
            dcc.Graph(id='time-series'),
            dcc.Graph(id='bar-chart'),
        ], style={'width':'70%','display':'inline-block','padding':'20px','verticalAlign':'top'}),
    ]),
    html.H2("Data Table"),
    dash_table.DataTable(id='table', columns=[{"name": i, "id": i} for i in df.columns], data=df.to_dict('records'), page_size=10)
])

def parse_contents(contents):
    import base64, io
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        return pd.read_csv(io.StringIO(decoded.decode('utf-8')), parse_dates=['Date'])
    except Exception as e:
        return None

@app.callback(
    Output('time-series', 'figure'),
    Output('bar-chart', 'figure'),
    Output('table', 'data'),
    Input('category', 'value'),
    Input('region', 'value'),
    Input('upload-data', 'contents'),
)
def update_charts(category, region, upload_contents):
    dff = df.copy()
    if upload_contents:
        uploaded = parse_contents(upload_contents)
        if uploaded is not None:
            dff = uploaded

    if category:
        dff = dff[dff['Category'] == category]
    if region and region != 'All':
        dff = dff[dff['Region'] == region]

    # time series (monthly revenue)
    ts = dff.groupby(pd.Grouper(key='Date', freq='M'), as_index=False)['Revenue'].sum()
    fig_ts = px.line(ts, x='Date', y='Revenue', title='Monthly Revenue')

    # bar chart (sales by product)
    fig_bar = px.bar(dff.groupby('Product', as_index=False)['Sales'].sum(), x='Product', y='Sales', title='Sales by Product')

    table_data = dff.to_dict('records')
    return fig_ts, fig_bar, table_data

if __name__ == '__main__':
    app.run_server(debug=True)
