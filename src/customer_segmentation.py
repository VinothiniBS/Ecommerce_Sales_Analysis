from sklearn.cluster import KMeans


def perform_rfm_analysis(data):
    """Perform RFM analysis to segment customers."""
    rfm = data.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (data['InvoiceDate'].max() - x.max()).days,
        'InvoiceNo': 'count',
        'Quantity': 'sum'
    }).reset_index()
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    kmeans = KMeans(n_clusters=4, random_state=42)
    rfm['Segment'] = kmeans.fit_predict(rfm[['Recency', 'Frequency', 'Monetary']])
    print("Customer Segments:")
    print(rfm.head())