# 💰 Personal Expense Tracker

A command-line application built with Python to track and manage personal expenses with categorization, data persistence, and comprehensive reporting features.

## 📋 Features

- ✅ **Add Expenses** - Record expenses with amount, category, and description
- ✅ **View All Expenses** - Display complete expense history with details
- ✅ **Calculate Total Spending** - Get instant overview of total expenditure
- ✅ **Delete Expenses** - Remove unwanted expense entries
- ✅ **Category-Based Reporting** - View expenses grouped by category with totals
- ✅ **Data Persistence** - Automatic save/load functionality using JSON
- ✅ **Input Validation** - Robust error handling for user inputs
- ✅ **Clean CLI Interface** - Intuitive menu-driven user experience

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- No external dependencies required (uses standard library only)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/raulciprian-tudor/expense-tracker.git
cd expense-tracker
```

2. Run the application:

```bash
python3 main.py

# Suggestion: you can use alias run=python3 in terminal and then run the app by typing "run main.py"
```

## 💻 Usage

### Main Menu

When you run the application, you'll see the following menu:

```
=== Personal Expense Tracker ===
1. Add expense
2. View all expenses
3. View total spending
4. Delete expense
5. View by category
6. Save and exit

Enter choice (1-6):
```

### Adding an Expense

1. Select option `1` from the main menu
2. Enter the amount (must be a positive number)
3. Enter the category (e.g., Food, Transport, Bills)
4. Enter a description
5. The expense is automatically added to your list

**Example:**

```
What's the amount? $45.50
Enter category: Food
Enter description: Lunch at cafe
✓ Expense added successfully
```

### Viewing All Expenses

Select option `2` to see all your expenses in a formatted list:

```
--- ALL EXPENSES ---
1. $45.50 - Food - Lunch at cafe
2. $20.00 - Transport - Bus ticket
3. $100.00 - Bills - Internet bill
```

### Viewing Total Spending

Select option `3` to see your total expenditure:

```
Total Spent: $165.50
```

### Deleting an Expense

1. Select option `4`
2. View the numbered list of expenses
3. Enter the number of the expense you want to delete
4. Confirm deletion

### Viewing by Category

Select option `5` to see expenses grouped by category with subtotals:

```
--- EXPENSES BY CATEGORY ---

Food: $75.50
  • $45.50 - Lunch at cafe
  • $30.00 - Groceries

Transport: $20.00
  • $20.00 - Bus ticket

Bills: $100.00
  • $100.00 - Internet bill
```

### Saving and Exiting

Select option `6` to save your data and exit the application. Your expenses are automatically saved to `data/expenses.json` and will be loaded the next time you run the program.

## 📁 Project Structure

```
expense-tracker/
├── main.py                 # Main program loop and menu system
├── expenses_service.py     # Core expense management functions
├── file_handler.py         # Save/load functionality
├── data/
│   └── expenses.json       # Persistent data storage
└── README.md              # Project documentation
```

## 🛠️ Technical Details

### Data Structure

Each expense is stored as a dictionary with the following structure:

```python
{
    "amount": 45.50,
    "category": "Food",
    "description": "Lunch at cafe",
    "date": "2024-10-30 14:23"
}
```

### File Storage

Expenses are persisted in JSON format in the `data/` directory. The file is automatically created on first save and loaded on program startup.

### Error Handling

The application includes comprehensive error handling for:

- Invalid numeric inputs (non-numbers, negative values)
- Empty expense lists
- File I/O errors
- Out-of-range selections

## 🎯 What I Learned

Building this project helped me practice and understand:

- **Lists and Dictionaries**: Managing complex data structures
- **Loops**: Implementing `while` and `for` loops with proper flow control
- **Exception Handling**: Using `try/except` blocks for robust error handling
- **Functions**: Creating modular, reusable code
- **File I/O**: Reading and writing JSON data
- **Input Validation**: Ensuring data integrity through validation loops
- **Code Organization**: Separating concerns across multiple modules
- **User Experience**: Designing intuitive CLI interfaces

## 🔮 Future Enhancements

Potential features for future versions:

- [ ] Budget tracking with spending alerts
- [ ] Date range filtering for expense queries
- [ ] Export to CSV/Excel format
- [ ] Monthly and weekly spending reports
- [ ] Recurring expense management
- [ ] Multiple user profiles
- [ ] Data visualization (ASCII charts)
- [ ] Search functionality by keyword
- [ ] Edit existing expenses
- [ ] Currency conversion support

## 🧪 Testing

To test the application:

1. Add several expenses across different categories
2. Verify all CRUD operations work correctly
3. Test input validation with invalid inputs:
   - Negative amounts
   - Text in amount field
   - Out-of-range menu selections
4. Close and reopen the application to verify data persistence
5. Test edge cases (empty lists, deleting from empty list, etc.)

## 📝 Development Notes

### Design Decisions

- **JSON over CSV**: Chose JSON for better support of nested data structures
- **Menu-driven interface**: Simpler for users than command-line arguments
- **Separate modules**: Improved code organization and maintainability
- **Input validation loops**: Ensures data integrity without crashes

### Challenges Overcome

1. **List modification during iteration**: Learned to use `break` after modifying lists in loops
2. **Variable shadowing**: Discovered naming conflicts between variables and imported modules
3. **Indentation bugs**: Mastered Python's whitespace sensitivity
4. **Data persistence**: Implemented JSON serialization for the first time

## 👨‍💻 Author

Built as a learning project while completing CS50's Introduction to Programming with Python (CS50P).

**Skills Demonstrated**: Python, Data Structures, File I/O, Error Handling, CLI Development

## 📄 License

This project is open source.

## 🙏 Acknowledgments

- CS50P course by Harvard University and Dr. David Malan
- Python documentation and community resources

## 📞 Contact

Feel free to reach out if you have questions or suggestions!

- GitHub: [@raulciprian-tudor](https://github.com/raulciprian-tudor)
- LinkedIn: [Tudor Raul Ciprian](www.linkedin.com/in/ciprian-tudor-frontend-ux)

---

**⭐ If you find this project helpful, please consider giving it a star!**

_Built with 🐍 Python and ❤️ for learning_
