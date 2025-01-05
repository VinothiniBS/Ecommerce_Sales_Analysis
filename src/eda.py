import pandas as pd

def perform_eda(data):

    # Sales by month
    data['Month'] = data['InvoiceDate'].dt.to_period('M')
    monthly_sales = data.groupby('Month')['Quantity'].sum()
    print("Monthly Sales:")
    print(monthly_sales)

    # Top 5 selling products
    top_products = data.groupby('Description')['Quantity'].sum().nlargest(5)
    print("Top 5 Products:")
    print(top_products)

    # Sales by country
    country_sales = data['Country'].value_counts()
    print("Sales by Country:")
    print(country_sales)