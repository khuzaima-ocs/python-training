import pandas as pd

'''
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
'''

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

df = pd.DataFrame(student_data, columns=['Id', 'Age'])
print(df)