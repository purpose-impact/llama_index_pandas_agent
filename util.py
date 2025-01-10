import pandas as pd

# load the data
df = pd.read_csv('./data/BasicCompanyData-2025-01-01-part1_7.csv').head(50)

try:
    output_path = './data/company_data_min.csv'
    df.to_csv(output_path, index=False)
    print(f"Data successfully saved to {output_path}")
except Exception as e:
    print(f"Error saving data: {str(e)}")
