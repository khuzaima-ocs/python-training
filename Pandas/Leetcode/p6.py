import pandas as pd

'''
There are some duplicate rows in the DataFrame based on the email column.
Write a solution to remove these duplicate rows and keep only the first occurrence.
'''

customers = [   
    {"name": "Ella", "Email": "emily@example.com"},
    {"name": "David", "Email": "michael@example.co"},
    {"name": "Zachary", "Email": "sarah@example.com"},
    {"name": "Alice", "Email": "john@example.com"},
    {"name": "Finn", "Email": "john@example.com"},
    {"name": "Violet", "Email": "alice@example.com"},
]

df = pd.DataFrame(customers)

df.drop_duplicates(subset=["Email"], keep="first", inplace=True)

print(df)