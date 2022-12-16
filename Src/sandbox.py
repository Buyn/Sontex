# ----------------------------------------------
# * import : 
# ----------------------------------------------
import pandas as pd


# ----------------------------------------------
# * vars : 
# ----------------------------------------------


# ----------------------------------------------
# * main :
# ----------------------------------------------
import pandas as pd

# Read data from the Excel file
df = pd.read_excel("test.xlsx")

# Loop through the rows and columns of the DataFrame
for row_index, row in df.iterrows():
    for col_index, value in row.iteritems():
        # Get the cell style from the cell
        cell_style = df.style.apply(lambda x: x[col_index], axis=1)[row_index]

        # Get the cell color and font size from the cell style
        cell_color = cell_style.background_color.to_string(index=False)
        font_size = cell_style.font.size

        # Print the cell color and font size
        print("Cell color:", cell_color)
        print("Font size:", font_size)


# ----------------------------------------------
# * -------------------------------------------:
