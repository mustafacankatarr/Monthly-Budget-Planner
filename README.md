# Monthly Budget Planner

A small command-line tool that reads a list of monthly expenses from a file,
analyses the spending and writes a formatted report.

## Features
- Reads expenses from `expenses.txt` (one `category,amount` per line)
- Calculates total spending and a per-category breakdown
- Recommends an emergency fund as a share of total spending
- Reports the average daily spending and the biggest expense
- Writes the result to `report.txt`

## Usage
```
python budget.py
```

## Input format
One expense per line, for example:
```
Rent,1200
Groceries,450
```
Blank lines and lines starting with `#` are ignored.
