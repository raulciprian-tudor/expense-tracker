"""This module was imported to use the datetime method used to get the current date and time"""

from datetime import datetime


def create_expense(amount: float, category: str, description: str):
    """Create a new expense dictionary with consistent structure"""
    return {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }


def add_expenses(expenses):
    """Add a new expense list"""
    print("Adding new expense")

    # Ask user for amount
    while True:
        try:
            amount = float(input("What's the amount? "))

            if amount <= 0:
                print("Invalid amount. Try again.")
                continue

            break

        except ValueError:
            print("Invalid amount. Try again.")

    # Ask user for description
    while True:
        description = input("What's the description? ").strip()

        if len(description) < 3:
            print("Description must be at least 3 characters!")
            continue

        break

    # Ask user for category
    while True:
        category = input("What's the category? ").strip().title()

        if len(category) < 3:
            print("Category must be at least 3 characters!")
            continue
        break

    # Create expense
    expense = create_expense(amount, category, description)

    # Add to list
    expenses.append(expense)

    print(f"✓ Expense added: ${amount:.2f} - {category}")


def view_expenses(expenses):
    """Display all expenses"""
    if not expenses:
        print("No expenses to show!")
        return

    for index, expense in enumerate(expenses):
        print(f"{index}: {expense}")


def view_total(expenses):
    """Calculate and display total spending"""
    total_spent = 0

    if not expenses:
        print("Total spending: 0")
        return

    for expense in expenses:
        total_spent += expense["amount"]

    print(f"Total spending: ${total_spent:.2f}")


def delete_expense(expenses):
    """Delete an expense by index"""

    if not expenses:
        print("No expenses to delete!")
        return
    # 1. Show all expenses with numbers
    print("\n--- YOUR EXPENSES ---")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. ${expense['amount']:.2f} - {expense['category']} - {expense['description']}"
        )

    # 2. Ask for number
    try:
        item_to_delete = int(input("\nEnter the number to delete (0 to cancel): "))

        if item_to_delete == 0:
            print("Deletion cancelled.")
            return

        # 3. Convert to zero-based index
        index = item_to_delete - 1

        # 4. Check if valid
        if 0 <= index <= len(expenses):
            deleted = expenses.pop(index)
            print(f"✓ Deleted: ${deleted['amount']:.2f} - {deleted['description']}")
        else:
            print(f"Invalid number! Please choose 1-{len(expenses)}")

    except ValueError:
        print("Please enter a valid number.")


def view_by_category(expenses):
    """Group and display expenses by category"""

    # 1. If list is empty tell user
    if not expenses:
        print("No expenses to show!")
        return

    # 2. Create dictionary to group expenses by category
    categories = {}
    # 3. Loop through expenses
    for index, expense in enumerate(expenses):
        category = expense["category"]
        # 4. If category not present, create new category
        if category not in categories:
            categories[category] = []

        # 5. Add expense to that category
        categories[category].append(expense)
    # 6. Display each category with its expenses
    print("\n --- EXPENSES BY CATEGORY ---")
    for category, expenses_list in categories.items():
        # Calculate total for this category
        total = sum(exp["amount"] for exp in expenses_list)

        print(f"\n{category}: {total:.2f}")

        for expense in expenses_list:
            print(f"  • ${expense['amount']:.2f} - {expense['description']}")
