# Write a program using pandas to filter and group data.

import pandas as pd

df = pd.read_csv("used_files\data.csv")

# Filter
filtered = df[df["marks"] > 50]
print(filtered)

# Group
grouped = df.groupby("class")["marks"].mean()
print(grouped)