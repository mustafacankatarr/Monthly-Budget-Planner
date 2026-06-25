"""Monthly Budget Planner.

Reads a list of monthly expenses from an external file and reports the total
spending together with a per-category breakdown.
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


def build_breakdown(expenses):
    """Return a list of formatted 'category: amount' lines."""
    return [f"  {category}: {amount:.2f}" for category, amount in expenses]


def main():
    expenses = read_expenses(INPUT_FILE)
    total = total_spending(expenses)

    print("Spending by category:")
    for line in build_breakdown(expenses):
        print(line)
    print(f"Total spending: {total:.2f}")


if __name__ == "__main__":
    main()
