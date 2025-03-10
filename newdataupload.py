import pandas as pd

# Load the CSV file
df = pd.read_csv('CITY_OF_SAN_PEDRO_transformed.csv')

# Remove rows where barangay_Res is "San Pedro"
df = df[df['barangay_Res'] != 'San Pedro']

# Sort the dataframe by barangay_Res and date
df = df.sort_values(by=['barangay_Res', 'date'])

# Calculate the daily new recovered cases
recovered_columns = [
    'count_Recovered', 'count_Recovered_age_9_below', 'count_Recovered_age_10_17',
    'count_Recovered_age_18_39', 'count_Recovered_age_40_59', 'count_Recovered_age_60_79',
    'count_Recovered_age_80_above', 'count_Recovered_Unknown', 'count_Recovered_Male',
    'count_Recovered_Female'
]

for col in recovered_columns:
    df[col] = df.groupby('barangay_Res')[col].diff().fillna(df[col])
    df[col] = df[col].round(0).astype(int)  # Ensure whole numbers

# Get unique barangay_Res values
barangays = df['barangay_Res'].unique()

# Save each barangay's data to a separate CSV file
for barangay in barangays:
    barangay_df = df[df['barangay_Res'] == barangay]
    barangay_df.to_csv(f'datauploadtransformed_data_{barangay}.csv', index=False)