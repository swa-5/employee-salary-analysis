import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Database connection
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

with open("database_setup.sql", "r") as file:
    sql_script = file.read()
    cursor.executescript(sql_script)

conn.commit()

# Load data
query = "SELECT * FROM employees"
df = pd.read_sql(query, conn)

print("Employee Data:")
print(df)

# Analysis 1: Average Salary by Department
avg_salary = df.groupby("department")["salary"].mean()
print("\nAverage Salary by Department:")
print(avg_salary)

# Visualization
avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("salary_chart.png")
plt.show()

# Analysis 2: Performance Based Increment Simulation
df["new_salary"] = df["salary"] + (df["performance_rating"] * 1000)

print("\nSalary After Performance Increment:")
print(df[["name", "salary", "new_salary"]])

conn.close()
