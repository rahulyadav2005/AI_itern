import pandas as pd
import numpy as np






data = {
    "EmpID":[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115],
    "Name":["Rahul","Suman","Amit","Anchal","Rohit","Priya","Neha","Karan","Vikas","Pooja","Ajay","Komal","Arjun","Riya","Deepak"],
    "department":["IT","HR","IT","Finance","HR","IT","Marketing","Finance","IT","HR","Marketing","IT","Finance","HR","IT"],
    "Age":[22,25,np.nan,29,31,26,28,np.nan,24,27,30,23,35,29,26],
    "Salary":[35000,42000,50000,60000,45000,np.nan,38000,70000,52000,41000,48000,36000,75000,43000,51000],
    "City":["Varanasi","Delhi","Lucknow","Patna","Delhi","Kanpur","Jaipur","Patna","Varanasi","Delhi","Lucknow","Kanpur","Patna","Delhi","Varanasi"]
}

df = pd.DataFrame(data)

print("Original data")
print(df)



print("\nData types")
print(df.dtypes)



print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\n Information")
print(df.info())

print("\n Summary")
print(df.describe())



df.rename(columns={"Salary":"MonthlySalary"}, inplace=True)

print("\nRenaming")
print(df.head())


#  Missing Values


df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Monthly_Salary"].fillna(df["Monthly_Salary"].mean(), inplace=True)

print("\nAfter fillna()")
print(df)


#  Drop Missing Values

drop = df.dropna()

print("\nAfter dropna()")
print(drop)

#delet

df1 = df.drop("City", axis=1)

print("\nAfter Deleting City Column")
print(df1.head())


 # Function


def salary_category(x):
    if x >= 60000:
        return "High"
    elif x >= 45000:
        return "Medium"
    else:
        return "Low"

df["Category"] = df["Monthly_Salary"].apply(salary_category)

print("\nSalary Category")
print(df[["Name","Monthly_Salary","Category"]])



print("\nAverage Salary")
print(df["Monthly_Salary"].mean())

print("\nMaximum Salary")
print(df["Monthly_Salary"].max())

print("\nMinimum Salary")
print(df["Monthly_Salary"].min())

print("\nMedian Salary")
print(df["Monthly_Salary"].median())

print("\nSalary Standard Deviation")
print(df["Monthly_Salary"].std())

print("\nTotal Salary")
print(df["Monthly_Salary"].sum())



print("\nAge + 2")
print(df["Age"] + 2)

print("\nSalary Bonus (10%)")
print(df["Monthly_Salary"] * 1.10)



extra = pd.DataFrame({
    "Emp_ID":[116,117],
    "Name":["Rakesh","Sneha"],
    "Department":["IT","HR"],
    "Age":[27,24],
    "Monthly_Salary":[47000,39000],
    "City":["Delhi","Lucknow"],
    "Category":["Medium","Low"]
})

new_df = pd.concat([df, extra], ignore_index=True)

print("\nAfter Concatenation")
print(new_df)


#Question
print("\nQ1. Employees working in IT Department")
print(df[df["Department"]=="IT"])

print("\nQ2. Employee having Maximum Salary")
print(df[df["Monthly_Salary"]==df["Monthly_Salary"].max()])

print("\nQ3. Average Salary Department Wise")
print(df.groupby("Department")["Monthly_Salary"].mean())

print("\nQ4. Number of Employees in each Department")
print(df["Department"].value_counts())

print("\nQ5. Employees whose Salary is greater than 50000")
print(df[df["Monthly_Salary"]>50000])