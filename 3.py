import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('result.csv')

# Display the first 10 rows
print("First 10 rows of the DataFrame:")
print(df.head(10))

# Filter the DataFrame to show only rows where Salary is greater than 75,000
filtered_df = df[df['Salary'] > 75000]

print("\nRows where Salary is greater than 75,000:")
print(filtered_df)
