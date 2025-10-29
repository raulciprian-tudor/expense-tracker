from datetime import datetime

def create_expense(amount: float, category: str, description: str):
    # Create a new expense dictionary with consistent structure
    return {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

def add_expenses(expenses):
    # Add a new expense list
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
    # Display all expenses
    # TODO - check again if something's missing
    if not expenses:
        print("No expenses to show!")
        return
    else:
        for expense in range(len(expenses)): 
            print(expense, expenses[expense])        

def view_total(expenses):
    # Calculate and display total spending+
    # TODO
    pass

def delete_expense(expenses):
    # Delete an expense by index
    # TODO
    pass

def view_by_category(expenses):
    # Group and display expenses by category
    # TODO
    pass

