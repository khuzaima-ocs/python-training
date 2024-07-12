import pandas as pd

data = {
    "No.": [520, 533, 509],
    "Name": ["Khuzaima", "Adeel", "Hanan"],
    "Age": [23, 22, 22],
    "CGPA": [3.4,2.7,3.3]
}

df = pd.DataFrame(data)
df.set_index("No.", inplace=True)

print(df)
df.sort_values(by=["Age", "CGPA"], inplace=True)
print(df)
df.sort_index(inplace=True)
print(df)