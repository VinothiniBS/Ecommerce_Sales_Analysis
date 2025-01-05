from prophet import Prophet
import matplotlib.pyplot as plt

def prepare_forecasting_data(data):
    """Prepare data for forecasting by aggregating sales over time."""
    time_series = data[['InvoiceDate', 'Quantity']].copy()
    time_series['InvoiceDate'] = time_series['InvoiceDate'].dt.to_period('D').dt.to_timestamp()
    sales_daily = time_series.groupby('InvoiceDate').sum().reset_index()
    sales_daily.columns = ['ds', 'y']
    return sales_daily


def forecast_sales(data):
    """Forecast future sales using Facebook Prophet."""
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    model.plot(forecast)
    plt.title('Sales Forecast')
    plt.show()