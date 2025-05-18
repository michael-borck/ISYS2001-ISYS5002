# The data science ecosystem includes powerful libraries:
import pandas as pd         # Data manipulation and analysis
import numpy as np          # Scientific computing with arrays
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns       # Statistical visualizations

# A simple data analysis workflow:
# 1. Load data
data = pd.read_csv('large_dataset.csv')

# 2. Explore and clean
data = data.dropna()  # Remove missing values
print(data.describe())  # Summary statistics

# 3. Visualize relationships
sns.pairplot(data)  # Create matrix of scatter plots
plt.show()

# 4. Answer questions with data
grouped = data.groupby('category').mean()  # Averages by category
