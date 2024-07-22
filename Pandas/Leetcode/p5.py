import pandas as pd

'''
Write a solution to create a new column name bonus that contains the doubled values of the salary column.
'''

employees = [
    {"name": "Piper" , "salary": 4548},
    {"name": "Grace" , "salary": 28150},
    {"name": "Georgia" , "salary": 1103},
    {"name": "Willow" , "salary": 6593},
    {"name": "Finn" , "salary": 74576},
    {"name": "Thomas" , "salary": 24433},
]

df = pd.DataFrame(employees)
df['bonus'] = df['salary'] * 2

print(df)