# Features of the Script
# Best Practices:

# Uses pandas for robust and efficient CSV file processing.
# Modular design: The main logic is encapsulated in a process_csv function.
# Error handling ensures the script is robust against common issues like missing files or empty datasets.
# Detailed Comments:

# Clear explanations of each step, including loading data, performing operations, and saving results.
# Highlights areas where customization is needed (e.g., column names).
# Flexibility:

# Designed to be reusable with any CSV file by updating column names and file paths.
# Extensibility:

# Additional aggregations or operations can be easily added.

# csv_processing.py

"""
Script for processing a CSV file. 
Performs various aggregations such as counting the frequency of items in a column and computing basic statistics.

Best Practices:
- Uses built-in Python modules for simplicity.
- Includes error handling for robustness.
- Leverages pandas for efficient CSV processing and aggregations.
"""

import pandas as pd

def process_csv(file_path):
    """
    Processes a CSV file and performs various aggregations.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        None: Prints the results of the analysis.
    """
    try:
        # Load the CSV file into a Pandas DataFrame
        data = pd.read_csv(file_path)

        # Display a summary of the data
        print("\n--- Data Summary ---")
        print(data.info())

        # Example Aggregation 1: Count frequency of each item in a specified column
        column_name = "Category"  # Change this to the name of the column you want to analyze
        if column_name in data.columns:
            print(f"\n--- Frequency Count for Column: {column_name} ---")
            frequency = data[column_name].value_counts()
            print(frequency)
        else:
            print(f"\nColumn '{column_name}' not found in the dataset.")

        # Example Aggregation 2: Compute basic statistics for numerical columns
        print("\n--- Basic Statistics for Numerical Columns ---")
        statistics = data.describe()
        print(statistics)

        # Example Aggregation 3: Group by another column and compute aggregate metrics
        group_column = "Category"  # Change this to a column that can be grouped
        numeric_column = "Sales"   # Change this to a numeric column for aggregation
        if group_column in data.columns and numeric_column in data.columns:
            print(f"\n--- Aggregation: Sum of '{numeric_column}' Grouped by '{group_column}' ---")
            grouped_data = data.groupby(group_column)[numeric_column].sum()
            print(grouped_data)
        else:
            print(f"\nColumns '{group_column}' or '{numeric_column}' not found in the dataset.")

        # Save the frequency data to a new CSV file (optional)
        output_file = "output_frequency.csv"
        frequency.to_csv(output_file)
        print(f"\nFrequency data saved to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please provide a valid CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the path to your CSV file
    file_path = "example.csv"  # Update this path to point to your CSV file

    # Call the function to process the CSV file
    process_csv(file_path)
