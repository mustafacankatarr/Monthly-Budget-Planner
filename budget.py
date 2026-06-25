"""Monthly Budget Planner.

Reads monthly expenses from an external file, calculates the total spending and
a recommended emergency fund, and writes a formatted report to an output file.
"""

INPUT_FILE = "expenses.txt"
OUTPUT_FILE = "report.txt"

# Share of monthly spending to set aside as an emergency fund.
BUFFER_RATE = 0.10


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


def build_report(expenses):
    """Build the full report text as a single string."""
    total = total_spending(expenses)
    emergency_fund = total * BUFFER_RATE

    lines = ["Monthly Budget Report", "=====================", "", "Spending by category:"]
    lines.extend(build_breakdown(expenses))
    lines.append("")
    lines.append(f"Total spending:        {total:.2f}")
    lines.append(f"Emergency fund ({BUFFER_RATE:.0%}):   {emergency_fund:.2f}")
    return "\n".join(lines)


def main():
    expenses = read_expenses(INPUT_FILE)
    report = build_report(expenses)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(report)
    print(f"\nReport written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
