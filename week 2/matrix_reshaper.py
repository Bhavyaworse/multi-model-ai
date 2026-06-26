import pandas as pd
import numpy as np

machine_records = {
    'Machine_ID': ['M01', 'M01', 'M02', 'M02', 'M03', 'M03'],
    'Shift': ['Day', 'Night', 'Day', 'Night', 'Day', 'Night'],
    'Error_Rate': [0.02, 0.05, 0.01, 0.02, 0.08, 0.11],
    'RPM_Speed': [1500, 1550, 1480, 1490, 1620, 1650]
}

df = pd.DataFrame(machine_records)

pivot_table = df.pivot(index='Machine_ID', columns='Shift', values='Error_Rate')
print("--- Pivoted Error Rates ---")
print(pivot_table)

numeric_df = df[['Error_Rate', 'RPM_Speed']]
correlation_matrix = numeric_df.corr()
print("\n--- Feature Correlation Matrix ---")
print(correlation_matrix)
