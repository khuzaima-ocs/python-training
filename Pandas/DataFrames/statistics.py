import pandas as pd

data = {
    "No.": [520, 533, 509],
    "Name": ["Khuzaima", "Adeel", "Hanan"],
    "Age": [23, 22, 22],
    "CGPA": [3.4,2.7,3.3]
}

df = pd.DataFrame(data)
df.set_index("No.", inplace=True)

print(df.describe())

print(f"Max Age: {df['Age'].max()}")
print(f"Min Age: {df['Age'].min()}")
print(f"Median Age: {df['Age'].median()}")
print(f"Product of Age : {df['Age'].prod()}")
print(f"Sum of Age : {df['Age'].sum()}")