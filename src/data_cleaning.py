import pandas as pd

def load_and_clean_data(file_path):
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data.dropna(subset=['CustomerID'], inplace=True)
    data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]
    return data
