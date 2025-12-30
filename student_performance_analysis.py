"""
Student Performance Analysis

This script:
- Reads student marks from a CSV file
- Cleans invalid data
- Calculates average marks per department
- Computes pass percentage
- Identifies top performers per department
"""
import pandas as pd

# read CSV file
df = pd.read_csv("student_marks.csv")

# view data
print(df)
print(df.info())

# basic statistics
print("Overall average:", df["mark"].mean())

# average marks per department
dept_avg = df.groupby("dept")["mark"].mean()
print("\nAverage marks per department:")
print(dept_avg)
# remove invalid marks
df = df[(df["mark"] >= 0) & (df["mark"] <= 100)]

print("\nAfter cleaning:")
print(df)

# pass/fail column
df["pass"] = df["mark"] >= 50

# pass percentage per dept
pass_pct = df.groupby("dept")["pass"].mean() * 100
print("\nPass percentage per department:")
print(pass_pct)

# topper per dept
topper = df.loc[df.groupby("dept")["mark"].idxmax()]
print("\nTopper per department:")
print(topper[["name", "mark", "dept"]])
#read second dataset
details=pd.read_csv("student_details.csv")
print("\nStudent details:")
print(details)
#merge datasets
merged_df=pd.merge(df,details,on="name")
print("\nMerged Data:")
print(merged_df)
#check for missing matches
merged_outer=pd.merge(df,details,on="name",how="outer",indicator=True)
print("\nMerge check:")
print(merged_outer[["_merge","name"]])

      