import os, sys
import pandas as pd
from pathlib import Path

# Input arguments
df_to_read = Path(sys.argv[1])
df_sep = sys.argv[2]
indexCol = sys.argv[3]
disp_nRows = sys.argv[4]
disp_cols = sys.argv[5]
disp_inds = sys.argv[6]
col_to_print = sys.argv[7]

# Dataframe separator character
if df_sep == 'space':
    df_sep = ' '
elif df_sep == 'comma':
    df_sep = ','

# Number of rows displayed
if disp_nRows == 'default':
    pass
elif disp_nRows == 'all':
    pd.set_option('DISPLAY.MAX_ROWS', None)
else:
    print("Invalid input for -r, --row-display. Possible input arguments (default, all)")
    sys.exit(1)

# Index column
if indexCol == 'default':
    indexCol = None
else:
    try:
        indexCol = int(indexCol)
    except ValueError:
        pass

df = pd.read_table(df_to_read, sep=df_sep, index_col=indexCol)

print(df)

# Option to print the series of a given column header
if not col_to_print == "none":
    print(df[col_to_print])

# Option to display columns and indices
def parseYesNoUsrInput(_input, _arg):
    if _input == 'n':
        _input = False
    elif _input == 'y':
        _input = True
    else:
        print(f'Invalid input for {_arg}. Possible input arguments (y, n)')
        sys.exit(1)

    return _input

print_cols = parseYesNoUsrInput(disp_cols, '-c, --display-columns')
if print_cols:
    for col in df.columns:
        print(col)

print_indices = parseYesNoUsrInput(disp_inds, '-i, --display-indices')
if print_indices:
    for i in df.index:
        print(i)

sys.exit(0)
