import expenses_service

def main():
    expenses = [] # List of expenses
    
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
        
        match choice:
            case 1:
                expenses_service.add_expenses(expenses)
            case 2:
                expenses_service.view_expenses(expenses)
            case 3:
                expenses_service.view_total(expenses)
            case 4:
                expenses_service.delete_expense(expenses)
            case 5:
                expenses_service.view_by_category(expenses)
            case 6:
                # TODO: Save data to file
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()