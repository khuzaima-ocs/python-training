import pandas as pd

def replace(df: pd.DataFrame):
    df.replace(to_replace="Hanan", value="Mohil Sb", inplace=True)

data = {
    "Name": ["Khuzaima", "Adeel", "Hanan"],
    "Age": [23, 22, 21],
}

df = pd.DataFrame(data)
print(df)
replace(df)
print(df)