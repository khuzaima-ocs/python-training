import pandas as pd

'''
Write a solution to select the name and age of the player with player id = 848.
The result format is in the following example.
'''

players = [
    { "id": 846, "Name": "Aa","Age": 21, "Pos": "Forward"},
    { "id": 847, "Name": "Bb","Age": 22, "Pos": "Forward"},
    { "id": 848, "Name": "Cc","Age": 20, "Pos": "Backward"},
    { "id": 849, "Name": "Dd","Age": 18, "Pos": "Center"},
]

df = pd.DataFrame(players)
res = df.loc[df['id'] == 848, ["Name", "Age"]]

print(res)