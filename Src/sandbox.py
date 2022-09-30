import pandas as pd

filename = "Data_files/metod01.xlsx"

df = pd.read_excel(filename, sheet_name = "показники", engine='openpyxl')
#view the first five rows: 
print (df.head())


