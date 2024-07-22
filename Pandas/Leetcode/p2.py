import pandas as pd

'''
Write a solution to calculate and display the number of rows and columns of players.
Return the result as an array: [number of rows, number of columns]
'''

players = [
    { 846, "Aa",21,"Forward"},
    { 847, "Bb",22,"Forward"},
    { 848, "Cc",20,"Backward"},
    { 849, "Dd",28,"Backward"},
    { 850, "Ee",32,"Center"},
    { 851, "Ff",18,"Center"},
    { 852, "Gg",26,"Forward"},
    { 853, "Hh",28,"Center"},
]

df = pd.DataFrame(players, columns=["sda", "Name","Age", "Position"])

print(list(df.shape))