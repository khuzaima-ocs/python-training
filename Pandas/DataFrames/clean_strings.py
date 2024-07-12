import pandas as pd

def clean_strings(df):
    for i in range(df.shape[0]):
        df.iat[i, 0] = df.iat[i, 0].strip().capitalize()


data = {
    "Name": ["khUZaimA  ", " aDEEl", "HaNaN"],
    "Age": [23, 22, 21],
}

df = pd.DataFrame(data)
print(df)
clean_strings(df)
print(df)