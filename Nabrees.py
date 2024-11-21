import pandas as pd
from abc import ABC, abstractmethod
import dash
from dash import html, dash_table, dcc
from dash.dependencies import Input, Output
import plotly.express as px


# Interface for data ingestion
class DataIngestionStrategy(ABC):
    @abstractmethod
    def ingest_data(self, file_path):
        pass


# Concrete class for Excel data ingestion
class ExcelDataIngestion(DataIngestionStrategy):
    def ingest_data(self, file_path):
        data = pd.read_excel(file_path)
        # Strip whitespace from column names
        data.columns = data.columns.str.strip()
        return data


# Context class for data ingestion
class DataIngestionContext:
    def __init__(self, strategy: DataIngestionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DataIngestionStrategy):
        self._strategy = strategy

    def ingest(self, file_path):
        return self._strategy.ingest_data(file_path)


# Interface for data processing
class DataProcess(ABC):
    @abstractmethod
    def process_data(self, data):
        pass


# Context class for data processing
class DataProcessingContext:
    def __init__(self, strategy: DataProcess):
        self._strategy = strategy

    def set_strategy(self, strategy: DataProcess):
        self._strategy = strategy

    def process(self, data):
        return self._strategy.process_data(data)


class TrendsOverTime(DataProcess):
    def process_data(self, data):
        # Ensure 'Date' is in datetime format
        data['Date'] = pd.to_datetime(data['Date'])
        grouped = data.groupby(data['Date'].dt.to_period("M"))['Customer_ID'].count().reset_index()
        grouped.columns = ['Date', 'TotalTransactions']
        grouped['Date'] = grouped['Date'].dt.to_timestamp()
        return grouped


class PurchaseCategoryAnalysis(DataProcess):
    def process_data(self, data):
        return data.groupby('Purchase Category')['Customer_ID'].count().reset_index(name='TotalPurchases')


class LocationDistribution(DataProcess):
    def process_data(self, data):
        return data.groupby('Location')['Customer_ID'].count().reset_index(name='CustomerCount')


# File path to the dataset
file_path = r"Nabrees Dataset.xlsx"

# Load and process data
data_ingestion_context = DataIngestionContext(ExcelDataIngestion())
sales_data = data_ingestion_context.ingest(file_path)

data_processing_context = DataProcessingContext(TrendsOverTime())
trends_data = data_processing_context.process(sales_data)

data_processing_context.set_strategy(PurchaseCategoryAnalysis())
category_data = data_processing_context.process(sales_data)

data_processing_context.set_strategy(LocationDistribution())
location_data = data_processing_context.process(sales_data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Customer Transactions Analysis'),

    # Data Table
    html.H2("Data Table"),
    dash_table.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i} for i in sales_data.columns],
        data=sales_data.to_dict('records'),
        page_action='native',
        page_size=10,
    ),

    # Dropdown for selecting charts
    html.H3('Select a Chart to Display:'),
    dcc.Dropdown(
        id='chart-selector',
        options=[
            {'label': 'Trends Over Time', 'value': 'trends-over-time'},
            {'label': 'Purchase Categories', 'value': 'purchase-categories'},
            {'label': 'Location Distribution', 'value': 'location-distribution'},
        ],
        value='trends-over-time',
    ),

    # Dynamic Chart
    html.Div(id='dynamic-chart'),
])


# Callback for dynamic chart
@app.callback(
    Output('dynamic-chart', 'children'),
    [Input('chart-selector', 'value')]
)
def update_chart(selected_chart):
    if selected_chart == 'trends-over-time':
        fig = px.line(trends_data, x='Date', y='TotalTransactions', title='Trends Over Time')
    elif selected_chart == 'purchase-categories':
        fig = px.bar(category_data, x='Purchase Category', y='TotalPurchases', title='Purchase Categories')
    elif selected_chart == 'location-distribution':
        fig = px.bar(location_data, x='Location', y='CustomerCount', title='Location Distribution')
    else:
        return "Please select a chart."

    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True)
