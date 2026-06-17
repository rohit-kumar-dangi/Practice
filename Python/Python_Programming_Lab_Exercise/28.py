# Write a program using pandas to read a CSV file and perform basic analysis

import pandas as pd

df = pd.read_csv("used_files\data.csv")

print(df.head())
print(df.describe())