import pandas as pd
from dash import dcc, html, dash_table
import dash
from dash.dependencies import Input, Output
import plotly.express as px

# Load dataset (adjust path)
try:
    sales_data = pd.read_csv("Financials.csv")
except FileNotFoundError:
    raise Exception("Dataset not found. Ensure the 'sales_data.csv' file is in the correct directory.")

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Sales Data Analysis Dashboard"),
    dcc.Dropdown(
        id='analysis-selector',
        options=[
            {'label': 'Best-Selling Products Analysis', 'value': 'best-selling'},
            {'label': 'Product Performance Analysis', 'value': 'product-performance'},
            {'label': 'Customer Behavior Analysis', 'value': 'customer-behavior'},
            {'label': 'Regional Sales Analysis', 'value': 'regional-sales'}
        ],
        value='best-selling'
    ),
    dcc.Graph(id='analysis-chart'),
])

# Callbacks
@app.callback(
    Output('analysis-chart', 'figure'),
    Input('analysis-selector', 'value')
)
def update_chart(selected_analysis):
    # Sample implementations (adjust logic as needed)
    if selected_analysis == 'best-selling':
        data = sales_data.groupby('Product')['Sales'].sum().reset_index()
        fig = px.bar(data, x='Product', y='Sales', title='Best-Selling Products')
    else:
        fig = {}  # Add other cases here
    return fig

# Run the app
try:
    app.run_server(debug=True, port=8051)  # Use a different port if needed
except Exception as e:
    print(f"An error occurred while running the server: {e}")
