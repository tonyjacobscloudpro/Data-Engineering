# Best Practices Followed
# Modular Design: The code is organized into functions for specific tasks, promoting reusability and clarity.
# Error Handling:
# Checks for the existence of columns.
# Validates column data types.
# Handles file errors gracefully.
# Command-Line Interface:
# Uses argparse to make the script flexible for different inputs.
# Documentation:
# Detailed docstrings explain the purpose of each function.
# A usage guide is included in the script header.
# Scalability:
# Supports various aggregations and row filtering.
# Easily extendable for additional features.

# csv_processing.py
"""
This script processes a CSV file to perform various aggregations, including:
1. Counting the frequency of items in a specified column.
2. Calculating the sum, mean, and max of numerical columns.
3. Filtering rows based on conditions.

Usage:
    python csv_processing.py <input_file.csv> <column_name>

Requirements:
    - pandas library
    - argparse for command-line argument parsing
"""

import pandas as pd
import argparse


def count_frequency(df, column_name):
    """
    Count the frequency of unique items in the specified column.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The column to analyze.

    Returns:
        pd.Series: A series with unique items and their counts.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")
    return df[column_name].value_counts()


def numerical_aggregations(df):
    """
    Perform aggregations on numerical columns (sum, mean, and max).

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: A DataFrame with aggregations for each numerical column.
    """
    numeric_columns = df.select_dtypes(include="number")
    if numeric_columns.empty:
        raise ValueError("No numerical columns found in the dataset.")
    return numeric_columns.aggregate(["sum", "mean", "max"])


def filter_rows(df, column_name, condition, value):
    """
    Filter rows based on a condition applied to a column.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column_name (str): The column to apply the condition on.
        condition (str): The condition ('>', '<', '==', etc.).
        value: The value to compare against.

    Returns:
        pd.DataFrame: A DataFrame containing the filtered rows.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")

    if condition == '>':
        return df[df[column_name] > value]
    elif condition == '<':
        return df[df[column_name] < value]
    elif condition == '==':
        return df[df[column_name] == value]
    else:
        raise ValueError(f"Condition '{condition}' is not supported.")


def main():
    """
    Main function to handle command-line arguments and process the CSV file.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Process a CSV file and perform aggregations."
    )
    parser.add_argument(
        "input_file", type=str, help="Path to the input CSV file"
    )
    parser.add_argument(
        "column_name", type=str, help="Column to perform frequency analysis on"
    )
    args = parser.parse_args()

    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(args.input_file)
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: File '{args.input_file}' is empty.")
        return

    print(f"Processing file: {args.input_file}\n")

    # Count the frequency of items in the specified column
    try:
        frequency = count_frequency(df, args.column_name)
        print("Frequency of items in column '{}':".format(args.column_name))
        print(frequency)
    except ValueError as e:
        print(e)
        return

    # Perform numerical aggregations
    try:
        print("\nNumerical aggregations (sum, mean, max):")
        print(numerical_aggregations(df))
    except ValueError as e:
        print(e)

    # Example: Filter rows where a numerical column value is greater than 50
    example_column = args.column_name
    example_condition = ">"
    example_value = 50

    if example_column in df.columns and pd.api.types.is_numeric_dtype(df[example_column]):
        print(f"\nRows where {example_column} {example_condition} {example_value}:")
        filtered_df = filter_rows(df, example_column, example_condition, example_value)
        print(filtered_df)
    else:
        print(f"\nColumn '{example_column}' is not numeric, skipping row filtering.")


if __name__ == "__main__":
    main()
