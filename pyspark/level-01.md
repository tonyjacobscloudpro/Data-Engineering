
# PySpark Level 1 Code Examples

## 1. Create a SparkSession
```python
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark Beginner Examples") \  # Sets a name for your application
    .master("local[*]") \  # Specifies the master as local with all available cores
    .getOrCreate()

print("Spark Session Created!")
```
**Explanation**: A SparkSession is the entry point to using PySpark. It allows you to create DataFrames, run SQL queries, and perform distributed computations.

---

## 2. Create a DataFrame from a List
```python
data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)  # Create DataFrame from a list of tuples
df.show()  # Display the DataFrame content
```
**Explanation**: This creates a DataFrame using a Python list of tuples and defines column names. `show()` prints the first 20 rows of the DataFrame.

---

## 3. Load a CSV File
```python
# Replace 'path/to/your/file.csv' with your file path
df = spark.read.csv("path/to/your/file.csv", header=True, inferSchema=True)

df.show()
```
**Explanation**: The `read.csv()` function loads a CSV file into a DataFrame. 
- `header=True` reads the first row as column names.
- `inferSchema=True` automatically infers the data types of the columns.

---

## 4. Perform Basic DataFrame Operations
```python
df.printSchema()  # Print the schema of the DataFrame
df.select("Name").show()  # Select specific column(s)
df.filter(df.Age > 25).show()  # Filter rows where Age > 25
df.groupBy("Age").count().show()  # Group by Age and calculate counts
```
**Explanation**:
- `printSchema()` displays the structure of the DataFrame (column names and data types).
- `select()` is used to retrieve specific columns.
- `filter()` filters rows based on conditions.
- `groupBy()` performs grouping and allows aggregation functions like `count()`.

---

## 5. Write Data to Parquet
```python
df.write.parquet("output/path", mode="overwrite")
print("Data written to Parquet successfully!")
```
**Explanation**: Writes the DataFrame to a Parquet file, a columnar storage format. 
- `mode="overwrite"` ensures existing files in the path are replaced.

---

## 6. SQL Queries with Temp View
```python
# Create a temporary view for SQL queries
df.createOrReplaceTempView("people")

# Execute SQL query
result = spark.sql("SELECT Name, Age FROM people WHERE Age > 25")
result.show()
```
**Explanation**: Converts a DataFrame into a temporary SQL view that allows running SQL queries directly on the data.

---

## 7. Add a New Column
```python
from pyspark.sql.functions import col

# Add a new column by calculating on existing columns
df = df.withColumn("Age_in_5_years", col("Age") + 5)
df.show()
```
**Explanation**: `withColumn()` adds or modifies columns in a DataFrame. In this case, it calculates a new column based on the existing "Age" column.

---

## 8. Read JSON File
```python
# Replace 'path/to/your/file.json' with your JSON file path
df = spark.read.json("path/to/your/file.json")
df.show()
```
**Explanation**: Loads a JSON file into a DataFrame. PySpark automatically parses the JSON structure.

---

## 9. Handle Missing Data
```python
# Drop rows with missing values
df = df.dropna()

# Fill missing values with a default value
df = df.fillna({"Age": 0, "Name": "Unknown"})
df.show()
```
**Explanation**:
- `dropna()` removes rows with null values.
- `fillna()` replaces missing values with a default value.

---

## 10. Use PySpark RDD (Optional Advanced)
```python
# Create an RDD
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# Perform operations on RDD
rdd = rdd.map(lambda x: x * 2)
print(rdd.collect())  # Collect results back to the driver
```
**Explanation**: Demonstrates Resilient Distributed Dataset (RDD), a lower-level abstraction for distributed data processing.

---

## 11. Save Data to CSV
```python
df.write.csv("output/csv/path", header=True, mode="overwrite")
print("Data written to CSV successfully!")
```
**Explanation**: Writes the DataFrame to a CSV file, preserving column headers.

---

## 12. Simple Aggregations
```python
df.agg({"Age": "avg", "Age": "max"}).show()
```
**Explanation**: Performs aggregation functions (`avg`, `max`) on the "Age" column.

---

## 13. Join Two DataFrames
```python
data2 = [("Alice", "F"), ("Bob", "M"), ("Cathy", "F")]
columns2 = ["Name", "Gender"]
df2 = spark.createDataFrame(data2, columns2)

# Inner join
joined_df = df.join(df2, on="Name", how="inner")
joined_df.show()
```
**Explanation**: Joins two DataFrames on the "Name" column using an inner join.

---

## 14. Cache and Persist a DataFrame
```python
df.cache()  # Cache DataFrame in memory
df.show()

df.persist()  # Persist DataFrame in memory and disk
df.show()
```
**Explanation**:
- `cache()` stores the DataFrame in memory for faster repeated access.
- `persist()` provides flexibility for storage levels (e.g., memory, disk).

---

## 15. Stop the SparkSession
```python
spark.stop()
print("Spark Session Stopped!")
```
**Explanation**: Stops the SparkSession to release resources when the application is done.

---
