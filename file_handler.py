"""Import modules for handling files"""

import json


def save_expenses(expenses):
    """Save expenses to JSON file"""
    try:
        with open("data/expenses.json", "w") as file:
            json.dump(expenses, file, indent=2)
        print(f"✓ Saved {len(expenses)} expenses!")
    except Exception as e:
        print(f"⚠ Error saving: {e}")


def load_expenses():
    """Load expenses from a JSON file"""
    try:
        with open("data/expenses.json", "r") as file:
            expenses = json.load(file)
            print(f"✓ Loaded {len(expenses)} expenses!")
            return expenses

    except FileNotFoundError:
        print("ℹ No saved data. Starting fresh!")
        return []

    except Exception as e:
        print(f"⚠ Error loading: {e}")
        return []
