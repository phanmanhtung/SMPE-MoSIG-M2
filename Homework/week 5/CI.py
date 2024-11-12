import pandas as pd
import numpy as np
from scipy import stats

# Read the data from the CSV file
data_file = 'measurements_03_47.csv'
data = pd.read_csv(data_file)

# Function to calculate the confidence interval
def compute_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    sem = stats.sem(data)  # Standard error of the mean
    margin_of_error = sem * stats.t.ppf((1 + confidence) / 2., n-1)
    return mean, mean - margin_of_error, mean + margin_of_error

# Print the column names to debug issues
print("Column names:", data.columns)

# Strip any whitespace from column names
data.columns = data.columns.str.strip()

# Group data by 'Type' and calculate confidence intervals
results = {}
for group, df_group in data.groupby('Type'):
    mean, lower_bound, upper_bound = compute_confidence_interval(df_group['Time'])
    results[group] = {
        'mean': mean,
        '95% CI lower bound': lower_bound,
        '95% CI upper bound': upper_bound
    }

# Print the results
for group, stats in results.items():
    print(f"Type: {group}")
    print(f"  Mean Time: {stats['mean']:.6f}")
    print(f"  95% Confidence Interval: ({stats['95% CI lower bound']:.6f}, {stats['95% CI upper bound']:.6f})")
    print()
