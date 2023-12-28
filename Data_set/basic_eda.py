import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the TSV file into a Pandas DataFrame
file_path = 'test.tsv'
df = pd.read_csv(file_path, sep='\t')

# Display the first few rows of the dataset
print(df.head())

# Check data types
print(df.dtypes)

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Remove duplicates (if needed)
df.drop_duplicates(inplace=True)

# Data Visualization (examples)
# Example: Histogram of a numeric variable
plt.hist(df['tconst'], bins=20)
plt.xlabel('tconst')
plt.ylabel('Frequency')
plt.show()

# Example: Box plot to visualize distributions
sns.boxplot(data=df, x='averageRating', y='numVotes')
plt.xlabel('averageRating')
plt.ylabel('numVotes')
plt.show()

# Correlation matrix
correlation_matrix = df.corr()

# Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Feature Engineering and Preprocessing can be performed here as needed.

# Document your findings and insights.

# Save the cleaned and preprocessed data (if needed)
# df.to_csv('cleaned_data.csv', index=False)
