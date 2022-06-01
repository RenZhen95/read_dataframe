#!/bin/bash

# Read the options
TEMP=`getopt -o :hf:s:R:C:i:I:c: --long help:,file-name:,sep:,row-display:,display-columns:,display-indices:,index-col:print-col: -- "$@"`
eval set -- "$TEMP"

help=$"Usage: read_dataframe -f <fileName>
  -s : Separator character in dataframe (default ' ')
  -R : Option to display number of rows (all, default)
  -C : List out columns (y,n)
  -i : List out indices (y,n)
  -I : Column to be set as index
  -c : Print series of the given column header
"

# Default values
df_sep="space"
rowDisplay="default"
displayColumns="n"
displayIndices="n"
indexCol="default"
printCol="none"

if [ $# -lt 2 ]; then
    echo "$help"
    exit 1
fi

while true ; do
    case "$1" in
        -h|--help)
            echo "$help"
            exit 1;;
        -f|--file-name)
            fileName=$2; shift 2;;
        -s|--sep)
            df_sep=$2; shift 2;;
        -R|--row-display)
            rowDisplay=$2; shift 2;;
        -C|--display-columns)
            displayColumns=$2; shift 2;;
        -i|--display-indices)
            displayIndices=$2; shift 2;;
        -I|--index-col)
            indexCol=$2; shift 2;;
        -c|--print-col)
            printCol=$2; shift 2;;
        --) shift; break;;
        *)  exit 1;;
    esac
done

python3 ~/bin/.read_dataframe.py "`realpath \"$fileName\"`" $df_sep $indexCol $rowDisplay $displayColumns $displayIndices $printCol

exit 0
