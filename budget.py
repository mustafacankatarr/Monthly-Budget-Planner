"""Monthly Budget Planner.

Reads a list of monthly expenses from an external file and reports how much
was spent in total.
"""

INPUT_FILE = "expenses.txt"


def read_expenses(path):
    """Read 'category,amount' lines from the input file into a list of tuples."""
    expenses = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            category, amount = line.split(",")
            expenses.append((category.strip(), float(amount)))
    return expenses


def total_spending(expenses):
    """Return the sum of all expense amounts."""
    return sum(amount for _, amount in expenses)


def main():
    expenses = read_expenses(INPUT_FILE)
    total = total_spending(expenses)
    print(f"Total spending: {total:.2f}")


if __name__ == "__main__":
    main()
