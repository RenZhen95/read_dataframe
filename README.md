<h1>
  <picture>
    <img alt="ReadDataFrame" src="icons/ReadDataFrame.png">
  </picture>
</h1>

# Simple Python CLI tool to read tables using Pandas

If you're one of those guys who prefers to work from the command line and need to often quickly check out what's saved in a file (without the hassle of having to touch your mouse ... ) this could be a useful tool.

**R**ead **D**ata**F**rame (rdf) provides a simple command-line interface to read tables. It essentially replaces

```python
import pandas as pd

df = pd.read_table(<yourfile>)
print(df)
```

with

```console
$ rdf <yourfile>
```

## Installation
```
pip install read-dataframe
```

## Usage
### Basic usage
To read a table, take for example the classical iris dataset
```console
$ rdf irisdataset.csv --sep ','
     sepal.length  sepal.width  petal.length  petal.width    variety
0             5.1          3.5           1.4          0.2     Setosa
1             4.9          3.0           1.4          0.2     Setosa
2             4.7          3.2           1.3          0.2     Setosa
3             4.6          3.1           1.5          0.2     Setosa
4             5.0          3.6           1.4          0.2     Setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  Virginica
146           6.3          2.5           5.0          1.9  Virginica
147           6.5          3.0           5.2          2.0  Virginica
148           6.2          3.4           5.4          2.3  Virginica
149           5.9          3.0           5.1          1.8  Virginica

[150 rows x 5 columns]
```

If for whatever reason you would like to set the column 'variety' to be the index column
```console
$ rdf irisdataset.csv --sep ',' --index-col variety
           sepal.length  sepal.width  petal.length  petal.width
variety
Setosa              5.1          3.5           1.4          0.2
Setosa              4.9          3.0           1.4          0.2
Setosa              4.7          3.2           1.3          0.2
Setosa              4.6          3.1           1.5          0.2
Setosa              5.0          3.6           1.4          0.2
...                 ...          ...           ...          ...
Virginica           6.7          3.0           5.2          2.3
Virginica           6.3          2.5           5.0          1.9
Virginica           6.5          3.0           5.2          2.0
Virginica           6.2          3.4           5.4          2.3
Virginica           5.9          3.0           5.1          1.8

[150 rows x 4 columns]
```

Want to have all 150 rows printed out? Try:
```console
$ rdf irisdataset.csv --sep ',' --display-nrows all 
```

### More user interactive functions
Adding the option `--list-columns` would prompt the user to give the number of column headers to be printed out (from first to last column), and a similar option is available for the index via `--list-indices`
```console
$ rdf irisdataset.csv --sep ',' --list-columns
     sepal.length  sepal.width  petal.length  petal.width    variety
0             5.1          3.5           1.4          0.2     Setosa
1             4.9          3.0           1.4          0.2     Setosa
2             4.7          3.2           1.3          0.2     Setosa
3             4.6          3.1           1.5          0.2     Setosa
4             5.0          3.6           1.4          0.2     Setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  Virginica
146           6.3          2.5           5.0          1.9  Virginica
147           6.5          3.0           5.2          2.0  Virginica
148           6.2          3.4           5.4          2.3  Virginica
149           5.9          3.0           5.1          1.8  Virginica

[150 rows x 5 columns]
Number of columns to list (<int> or 'all'): 2
sepal.length
sepal.width
```

To print the Series 'petal.length', add the `--print-col` option, which will similarly prompt the user for a column of interest. Since the 'petal.length' column is 2nd column (counting from 0), inputing 2 would give the same results. Also, a similar option is available for the index via `--print-index`
```console
$ rdf irisdataset.csv --sep ',' --print-col
     sepal.length  sepal.width  petal.length  petal.width    variety
0             5.1          3.5           1.4          0.2     Setosa
1             4.9          3.0           1.4          0.2     Setosa
2             4.7          3.2           1.3          0.2     Setosa
3             4.6          3.1           1.5          0.2     Setosa
4             5.0          3.6           1.4          0.2     Setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  Virginica
146           6.3          2.5           5.0          1.9  Virginica
147           6.5          3.0           5.2          2.0  Virginica
148           6.2          3.4           5.4          2.3  Virginica
149           5.9          3.0           5.1          1.8  Virginica

[150 rows x 5 columns]
Column to print (<int> or <str>): petal.length
0      1.4
1      1.4
2      1.3
3      1.5
4      1.4
      ...
145    5.2
146    5.0
147    5.2
148    5.4
149    5.1
Name: petal.length, Length: 150, dtype: float64
```
