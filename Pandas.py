#Code by: Dileep
#To read a CSV file from internet

import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv") 
print(data)
