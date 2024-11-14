# budget_category.py

class BudgetCategory:
    """A class to manage budget categories with allocated and remaining amounts.
    
    This class handles budget tracking for specific categories, including
    expense management and budget allocation.
    """
    
    # Task 1: Define Budget Category Class
    def __init__(self, category_name: str, allocated_budget: float) -> None:
        """Initialize a budget category.
        
        Args:
            category_name: The name of the budget category
            allocated_budget: The total budget allocated to this category
        """
        # Private attributes
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget
    
    # Task 2: Implement Getters and Setters
    # Getter for category name
    def get_category_name(self) -> str:
        """Get the category name.
        
        Returns:
            The category name
        """
        return self.__category_name

    # Setter for category name with validation (e.g., name must be a string)
    def set_category_name(self, name: str) -> None:
        """Set the category name.
        
        Args:
            name: The new category name
            
        Raises:
            ValueError: If name is not a non-empty string
        """
        if isinstance(name, str) and name.strip():
            self.__category_name = name
        else:
            raise ValueError("Category name must be a non-empty string.")
    
    # Getter for allocated budget
    def get_allocated_budget(self) -> float:
        """Get the allocated budget.
        
        Returns:
            The allocated budget
        """
        return self.__allocated_budget

    # Setter for allocated budget with validation (e.g., budget should be a positive number)
    def set_allocated_budget(self, budget: float) -> None:
        """Set the allocated budget.
        
        Args:
            budget: The new allocated budget
            
        Raises:
            ValueError: If budget is not a positive number
        """
        if isinstance(budget, (int, float)) and budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget  # Reset remaining budget if total is adjusted
        else:
            raise ValueError("Allocated budget must be a positive number.")
    
    # Task 3: Add Budget Functionality
    def add_expense(self, amount: float) -> None:
        """Add an expense to the budget.
        
        Args:
            amount: The expense amount
            
        Raises:
            ValueError: If amount is not positive or exceeds the remaining budget
        """
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        elif amount > self.__remaining_budget:
            raise ValueError("Expense exceeds remaining budget.")
        else:
            raise ValueError("Expense amount must be positive.")

    def get_remaining_budget(self) -> float:
        """Get the remaining budget for this category.
        
        Returns:
            The current remaining budget
        """
        return self.__remaining_budget
    
    def add_refund(self, amount: float) -> None:
        """Add a refund or correction to the budget.
        
        Args:
            amount: The amount to add back to the budget
            
        Raises:
            ValueError: If amount is negative or would exceed the allocated budget
        """
        if amount <= 0:
            raise ValueError("Refund amount must be positive.")
        if self.__remaining_budget + amount > self.__allocated_budget:
            raise ValueError("Refund would exceed allocated budget.")
        self.__remaining_budget += amount

    # Task 4: Display Budget Details
    def display_category_summary(self) -> None:
        """Display a summary of the budget category.
        """
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")
