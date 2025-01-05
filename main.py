from src.data_cleaning import load_and_clean_data
from src.eda import perform_eda
from src.forecasting import prepare_forecasting_data, forecast_sales
from src.customer_segmentation import perform_rfm_analysis
from src.visualization import plot_monthly_sales, plot_top_products, plot_sales_by_country

# Load and clean data
data_file_path = 'data/data.csv'
data = load_and_clean_data(data_file_path)

# Perform EDA
print("Performing Exploratory Data Analysis...")
perform_eda(data)

# Perform Sales Forecasting
print("Preparing data for sales forecasting...")
forecasting_data = prepare_forecasting_data(data)
forecast_sales(forecasting_data)

# Perform Customer Segmentation
print("Performing RFM Analysis for Customer Segmentation...")
perform_rfm_analysis(data)

# Generate Visualizations
print("Generating visualizations...")
plot_monthly_sales(data)
plot_top_products(data)
plot_sales_by_country(data)
print("Visuals Generated!")
