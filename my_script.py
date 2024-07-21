import pandas as pd

# http://geeksforgeeks.org/pandas-tutorial/
# create a two-dimensional list
data = [['John', 25, 'New York'],
       ['Alice', 30, 'London'],
       ['Bob', 35, 'Paris']]

# create a DataFrame from the list
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

print(df)