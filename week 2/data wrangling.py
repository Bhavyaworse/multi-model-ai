import pandas as pd
import numpy as np

telemetry_outputs = {
    'Run_ID': ['R101', 'R102', 'R103', 'R104', 'R105'],
    'Pressure_PSI': [115.5, np.nan, 98.2, 140.6, np.nan],
    'Safety_Check': ['Secure', 'Failed', 'Secure', 'Failed', 'Secure']
}

df_metrics = pd.DataFrame(telemetry_outputs)
print(df_metrics)

df_metrics['Pressure_PSI'] = df_metrics['Pressure_PSI'].fillna(100.0)
df_metrics = df_metrics.rename(columns={'Pressure_PSI': 'Calibrated_PSI'})
df_metrics.to_csv("output_telemetry_logs.csv", index=False)
print(df_metrics)
