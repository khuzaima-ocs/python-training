import pandas as pd

'''
Write a solution to display the first 3 rows of this DataFrame.
'''

players = [
    { "id": 846, "Name": "Aa","Age": 21, "Pos": "Forward"},
    { "id": 847, "Name": "Bb","Age": 22, "Pos": "Forward"},
    { "id": 848, "Name": "Cc","Age": 20, "Pos": "Backward"},
    { "id": 849, "Name": "Dd","Age": 18, "Pos": "Center"},
]

df = pd.DataFrame(players)

print(df.head(3))