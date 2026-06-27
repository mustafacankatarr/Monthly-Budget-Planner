"""Monthly Budget Planner.

Reads a list of monthly expenses from an external file, analyses the spending
and writes a formatted report to an output file. Built incrementally to
practise a professional Git workflow (branches, merges and a clean history).
"""

INPUT_FILE = "expenses.txt"
OUTPUT_FILE = "report.txt"

# Number of days used to estimate the average daily spending.
DAYS_IN_MONTH = 30

# Share of monthly spending to set aside as an emergency fund.
BUFFER_RATE = 0.20


def read_expenses(path):
    """Read 'category,amount' lines from the input file into a list of tuples.

    Blank lines and lines starting with '#' are ignored, and malformed lines are
    skipped with a warning so a single typo cannot crash the whole report.
    """
    expenses = []
    with open(path, "r", encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                category, amount = line.split(",")
                expenses.append((category.strip(), float(amount)))
            except ValueError:
                print(f"Skipping malformed line {number}: {line!r}")
    return expenses


def total_spending(expenses):
    """Return the sum of all expense amounts."""
    return sum(amount for _, amount in expenses)


def top_category(expenses):
    """Return the (category, amount) pair with the highest spending."""
    return max(expenses, key=lambda item: item[1])


def build_breakdown(expenses, total):
    """Return category lines sorted by amount, each with its share of the total."""
    lines = []
    for category, amount in sorted(expenses, key=lambda item: item[1], reverse=True):
        share = (amount / total * 100) if total else 0
        lines.append(f"  {category:<14} {amount:>9.2f}  ({share:4.1f}%)")
    return lines


def build_report(expenses):
    """Build the full report text as a single string."""
    total = total_spending(expenses)
    emergency_fund = total * BUFFER_RATE
    daily_average = total / DAYS_IN_MONTH
    biggest_category, biggest_amount = top_category(expenses)

    lines = ["Monthly Budget Report", "=====================", "", "Spending by category:"]
    lines.extend(build_breakdown(expenses, total))
    lines.append("")
    lines.append(f"Total spending:             {total:>9.2f}")
    lines.append(f"Average daily spending:     {daily_average:>9.2f}")
    lines.append(f"Emergency fund ({BUFFER_RATE:>4.0%}):       {emergency_fund:>9.2f}")
    lines.append(f"Biggest expense:            {biggest_category} ({biggest_amount:.2f})")
    return "\n".join(lines)


def main():
    expenses = read_expenses(INPUT_FILE)
    if not expenses:
        print("No expenses found. Please add entries to", INPUT_FILE)
        return

    report = build_report(expenses)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(report)
    print(f"\nReport written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
