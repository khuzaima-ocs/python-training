import pandas as pd

series = pd.Series(["Index 0","Index 1","Index 2","Index 3"],[9,8,7,6])

data_1 = {
    "Name": ["Khuzaima", "Adeel", "Hanan"],
    "Age": [23, 22, 21],
    "CGPA": [3.4, 2.7, 3.3],
}

data_2 = [
    {
        "Name": "Khuzaima",
        "Age": 23,
        "CGPA": 3.4
    },
    {
        "Name": "Adeel",
        "Age": 22,
        "CGPA": 2.7
    },
    {
        "Name": "Hanan",
        "Age": 21,
        "CGPA": 3.3
    }
]

data_3 = [
    [1,2,3,4],[5,6,7,8],[9,10,11,12]
]

data_4 = [
    ("Khuzaima", 23, 3.4),("Adeel", 22, 2.7), ("Hanan", 21, 3.3)
]

df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)
df_3 = pd.DataFrame(data_3)
df_4 = pd.DataFrame(data_4)
df_5 = pd.DataFrame(series)

print(df_1, end="\n--------------\n")
print(df_2, end="\n--------------\n")
print(df_3, end="\n--------------\n")
print(df_4, end="\n--------------\n")
print(df_5, end="\n--------------\n")