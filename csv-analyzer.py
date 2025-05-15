import pandas as pd

# Load data
df = pd.read_csv('sample-data.csv')

# Calculate stats
total_rows = len(df)
average_sales = df['Sales'].mean()
max_sale = df['Sales'].max()

# Print results
print(f"Total Rows: {total_rows}")
print(f"Average Sales: ${average_sales:.2f}")
print(f"Highest Sale: ${max_sale:.2f}")