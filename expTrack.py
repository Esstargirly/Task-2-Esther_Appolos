total = 0
expenses = []

print("Welcome to the Expense Tracker")
print("Enter your expenses one by one. Type ‘done’ when finished.\n")

while True:
    entry = input("Enter expense amount (or ‘done’ to finish): ")

    if entry.lower() == "done":
        break

    try:
        amount = float(entry)
        if amount < 0:
            print("Please enter a positive amount.")
            continue
        expenses.append(amount)
        total = total + amount
        print(f"  Added ₦{amount:,.2f}. Running total: ₦{total:,.2f}")
    except ValueError:
        print("Invalid input. Please enter a number.")

print("\n— Expense Summary —")
if not expenses:
    print("No expenses were recorded.")
else:
    for i, expense in enumerate(expenses, start=1):
        print(f"Expense {i}: ₦{expense:,.2f}")
    print(f"\n  Total Spent: ₦{total:,.2f}")

print("\nByeee")