"""This module provides all the methods for expenses."""

import expenses_service
import file_handler


def main():
    """This is the main function to run the program."""
    expenses = file_handler.load_expenses()  # Expenses list

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total spending")
        print("4. Delete expense")
        print("5. View by category")
        print("6. Save and exit")

        try:
            choice = int(input("\nEnter choice (1-6): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            expenses_service.add_expenses(expenses)
        elif choice == 2:
            expenses_service.view_expenses(expenses)
        elif choice == 3:
            expenses_service.view_total(expenses)
        elif choice == 4:
            expenses_service.delete_expense(expenses)
        elif choice == 5:
            expenses_service.view_by_category(expenses)
        elif choice == 6:
            file_handler.save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
