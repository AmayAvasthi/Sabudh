import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

try:
    # Set the Agg backend for Matplotlib
    import matplotlib
    matplotlib.use('Agg')

    # Load the TSV file into a Pandas DataFrame
    file_path = 'test.tsv'
    df = pd.read_csv(file_path, sep='\t')

    # Display the first few rows of the dataset
    print(df.head())

    # Check data types
    print("Data Types:")
    print(df.dtypes)

    # Summary statistics
    print("Summary Statistics:")
    print(df.describe())

    # Check for missing values
    print("Missing Values:")
    print(df.isnull().sum())

    # Remove duplicates (if needed)
    df.drop_duplicates(inplace=True)

    # Data Visualization (examples)
    # Create an 'images' directory if it doesn't exist
    output_directory = 'images'
    os.makedirs(output_directory, exist_ok=True)

    # Example: Histogram of a numeric variable
    plt.hist(df['tconst'], bins=20)
    plt.xlabel('tconst')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_directory, 'tconst_histogram.png'))
    plt.close()

    # Example: Box plot to visualize distributions
    sns.boxplot(data=df, x='averageRating', y='numVotes')
    plt.xlabel('Average Rating')
    plt.ylabel('Number of Votes')
    plt.savefig(os.path.join(output_directory, 'averageRating_box_plot.png'))
    plt.close()

    # Correlation matrix (specify numeric_only=True to avoid the warning)
    correlation_matrix = df.corr(numeric_only=True)

    # Heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.savefig(os.path.join(output_directory, 'correlation_heatmap.png'))
    plt.close()

    # Feature Engineering and Preprocessing can be performed here as needed.

    # Document your findings and insights.

    # Save the cleaned and preprocessed data (if needed)
    # df.to_csv('cleaned_data.csv', index=False)

except Exception as e:
    print(f"An error occurred: {e}")
