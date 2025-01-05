import matplotlib.pyplot as plt
import seaborn as sns


def plot_monthly_sales(data):
    data['Month'] = data['InvoiceDate'].dt.to_period('M')
    monthly_sales = data.groupby('Month')['Quantity'].sum()
    monthly_sales.plot(kind='bar', title='Monthly Sales', figsize=(10, 6))
    plt.show()


def plot_top_products(data):
    top_products = data.groupby('Description')['Quantity'].sum().nlargest(5)
    top_products.plot(kind='barh', title='Top 5 Products', figsize=(8, 5))
    plt.xlabel('Quantity Sold')
    plt.ylabel('Product Description')
    plt.show()


def plot_sales_by_country(data):
    country_sales = data['Country'].value_counts().head(10)
    sns.barplot(x=country_sales.values, y=country_sales.index)
    plt.title('Top 10 Countries by Sales')
    plt.show()