# main.py

from budget_category import BudgetCategory

def demonstrate_budget_management():
    """Demonstrate the functionality of the BudgetCategory class."""
    try:
        # Create budget categories
        food_category = BudgetCategory("Food", 500)
        transport_category = BudgetCategory("Transport", 300)
        
        # Demonstrate expense tracking for food
        print("\n=== Food Budget Management ===")
        food_category.add_expense(150)  # Grocery shopping
        food_category.add_expense(50)   # Restaurant meal
        food_category.display_category_summary()
        
        # Demonstrate refund handling
        print("\nProcessing refund of $25 for returned groceries...")
        food_category.add_refund(25)
        food_category.display_category_summary()
        
        # Demonstrate transport budget
        print("\n=== Transport Budget Management ===")
        transport_category.add_expense(100)  # Monthly bus pass
        transport_category.display_category_summary()
        
        # Demonstrate error handling
        print("\n=== Demonstrating Error Handling ===")
        print("Attempting to add invalid expense...")
        transport_category.add_expense(-50)  # Should raise ValueError
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the budget management demonstration."""
    print("Welcome to Personal Budget Management System!")
    demonstrate_budget_management()
    print("\nBudget management demonstration completed.")

if __name__ == "__main__":
    main()
