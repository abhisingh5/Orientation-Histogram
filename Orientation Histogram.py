# Histogram of Hard Drive Size in 2023 Data
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('2023-06-13-survey.csv')

plt.hist(df['Hard Drive Size (in GB)'], bins=20, edgecolor='black')
plt.title('Histogram of Hard Drive Size of 2023 Cohort')
plt.xlabel('Hard Drive Size')
plt.ylabel('Frequency')
plt.show()