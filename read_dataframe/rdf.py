import click
import pandas as pd

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--sep', default=' ')
@click.option('--index-col', default=None)
@click.option('--display-nrows', default='default')
@click.option('--list-columns/--no-list-columns', default=False)
@click.option('--list-indices/--no-list-indices', default=False)
@click.option('--print-col/--no-print-col', default=False)
@click.option('--print-index/--no-print-index', default=False)
def cliread(
    filename, sep, index_col, display_nrows,
    list_columns, list_indices,
    print_col, print_index
    ):

    # Options
    # -------
    # display-nrows
    if display_nrows == 'default':
        pass
    elif display_nrows == 'all':
        pd.set_option('DISPLAY.MAX_ROWS', None)
    else:
        try:
            nRows = int(display_nrows)
            pd.set_option('DISPLAY.MAX_ROWS', nRows)
        except ValueError:
            print(
                "Invalid input for --display-nrows. Possible input " + 
                "arguments {default, all, <int>}"
                )
    
    # Index column
    if not index_col is None:
        try:
            index_col = int(index_col)
        except ValueError:
            pass

    df = pd.read_table(filename, sep=sep, index_col=index_col)
    print(df)

    # List columns
    if list_columns:
        ncol_to_list = input("Number of columns to list (<int> or 'all'): ")
        if ncol_to_list == 'all':
            ncol_to_list = None
        else:
            ncol_to_list = int(ncol_to_list)
        listColumns(df, ncol_to_list)

    # List indices
    if list_indices:
        nrow_to_list = input("Number of index to list (<int> or 'all'): ")
        if nrow_to_list == 'all':
            nrow_to_list = None
        else:
            nrow_to_list = int(nrow_to_list)
        listIndices(df, nrow_to_list)

    # Print a column based on user input
    if print_col:
        col_to_print = input("Column to print (<int> or <str>): ")
        try:
            col_to_print = int(col_to_print)
            print(df.iloc[:,col_to_print])
        except ValueError:
            print(df[col_to_print])

    # Print an index based on user input
    if print_index:
        row_to_print = input("Index to print (<int> or <str>): ")
        try:
            row_to_print = int(row_to_print)
            print(df.iloc[row_to_print,:])
        except ValueError:
            print(df.loc[row_to_print,:])

# Functions
def listColumns(_df, ncol_to_list=None):
    if ncol_to_list is None:
        for col in _df.columns:
            print(col)
    else:
        for count, col in enumerate(_df.columns):
            print(col)
            if count == ncol_to_list-1:
                break

def listIndices(_df, nrow_to_list=None):
    if nrow_to_list is None:
        for row in _df.index:
            print(row)
    else:
        for count, row in enumerate(_df.index):
            print(row)
            if count == nrow_to_list-1:
                break
