
# PySpark level 1 Code Examples

## 1. Create a SparkSession
```python
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark Beginner Examples") \
    .master("local[*]") \
    .getOrCreate()

print("Spark Session Created!")
```

---

## 2. Create a DataFrame from a List
```python
data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()
```

**Output:**
```
+-----+---+
| Name|Age|
+-----+---+
|Alice| 25|
|  Bob| 30|
|Cathy| 28|
+-----+---+
```

---

## 3. Load a CSV File
```python
# Replace 'path/to/your/file.csv' with your file path
df = spark.read.csv("path/to/your/file.csv", header=True, inferSchema=True)
df.show()
```

---

## 4. Perform Basic DataFrame Operations
```python
df.printSchema()  # Print the schema of the DataFrame
df.select("Name").show()  # Select specific column(s)
df.filter(df.Age > 25).show()  # Filter rows based on condition
df.groupBy("Age").count().show()  # Group and aggregate
```

---

## 5. Write Data to Parquet
```python
df.write.parquet("output/path", mode="overwrite")
print("Data written to Parquet successfully!")
```

---

## 6. SQL Queries with Temp View
```python
# Create a temporary view for SQL queries
df.createOrReplaceTempView("people")

# Execute SQL query
result = spark.sql("SELECT Name, Age FROM people WHERE Age > 25")
result.show()
```

---

## 7. Add a New Column
```python
from pyspark.sql.functions import col

# Add a new column by calculating on existing columns
df = df.withColumn("Age_in_5_years", col("Age") + 5)
df.show()
```

**Output:**
```
+-----+---+-------------+
| Name|Age|Age_in_5_years|
+-----+---+-------------+
|Alice| 25|           30|
|  Bob| 30|           35|
|Cathy| 28|           33|
+-----+---+-------------+
```

---

## 8. Read JSON File
```python
# Replace 'path/to/your/file.json' with your JSON file path
df = spark.read.json("path/to/your/file.json")
df.show()
```

---

## 9. Handle Missing Data
```python
# Drop rows with missing values
df = df.dropna()

# Fill missing values with a default value
df = df.fillna({"Age": 0, "Name": "Unknown"})
df.show()
```

---

## 10. Use PySpark RDD (Optional Advanced)
```python
# Create an RDD
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# Perform operations on RDD
rdd = rdd.map(lambda x: x * 2)
print(rdd.collect())  # [2, 4, 6, 8, 10]
```

---

## 11. Save Data to CSV
```python
df.write.csv("output/csv/path", header=True, mode="overwrite")
print("Data written to CSV successfully!")
```

---

## 12. Simple Aggregations
```python
df.agg({"Age": "avg", "Age": "max"}).show()
```

**Output:**
```
+--------+
|max(Age)|
+--------+
|      30|
+--------+
```

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

**Output:**
```
+-----+---+------+
| Name|Age|Gender|
+-----+---+------+
|Alice| 25|     F|
|  Bob| 30|     M|
|Cathy| 28|     F|
+-----+---+------+
```

---

## 14. Cache and Persist a DataFrame
```python
df.cache()  # Cache DataFrame in memory
df.show()

df.persist()  # Persist DataFrame in memory and disk
df.show()
```

---

## 15. Stop the SparkSession
```python
spark.stop()
print("Spark Session Stopped!")
```
