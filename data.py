#import pandas as pd
import pandas as pandasForSortingCSV
csvData = pandasForSortingCSV.read_csv("customers-100.csv")

print("\nBefore sorting:")
print(csvData)

# sort by Last Name
csvData.sort_values(["First Name"],
    axis=0,
    ascending=[True],
    inplace=True)

# displaying sorted data frame
print("\nAfter sorting:")
print(csvData)