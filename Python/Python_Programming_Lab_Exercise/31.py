# Write a program combining numpy, pandas, and matplotlib for simple data analysis.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = np.array([10, 20, 30, 40])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Values"])

# Plot
plt.plot(df["Values"])
plt.title("Data Analysis")
plt.show()