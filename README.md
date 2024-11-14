# Personal Budget Management System

A Python-based personal budget management system that helps users track and manage their expenses across different budget categories.

## Features

- Create and manage multiple budget categories
- Track expenses within each category
- Process refunds and budget adjustments
- Real-time budget monitoring
- Input validation and error handling
- Detailed budget summaries

## Project Structure

```
Module4Lesson3/
├── PersonalBudgetManagement.py  # Core budget category implementation
├── main.py                      # Demo and usage examples
└── README.md                    # Project documentation
```

## Installation

1. Ensure you have Python 3.6 or higher installed
2. Clone or download this repository
3. No additional dependencies required

## Usage

Run the demonstration script:
```bash
python main.py
```

Example code for creating and managing a budget category:
```python
from budget_category import BudgetCategory

# Create a new budget category
food_budget = BudgetCategory("Food", 500)

# Add expenses
food_budget.add_expense(150)  # Grocery shopping
food_budget.add_expense(50)   # Restaurant meal

# Process a refund
food_budget.add_refund(25)    # Return item refund

# View budget summary
food_budget.display_category_summary()
```

## Class Documentation

### BudgetCategory

The main class for managing budget categories.

#### Methods:
- `__init__(category_name: str, allocated_budget: float)`: Initialize a new budget category
- `add_expense(amount: float)`: Record an expense
- `add_refund(amount: float)`: Process a refund
- `display_category_summary()`: Show current budget status
- `get_remaining_budget()`: Get available budget
- Various getters and setters with input validation

## Error Handling

The system includes comprehensive error handling for:
- Invalid expense amounts
- Insufficient budget
- Invalid refund amounts
- Invalid category names
- Invalid budget allocations

## Best Practices

- Uses encapsulation with private attributes
- Input validation on all operations
- Clear error messages
- Type hints for better code maintainability
- Comprehensive documentation

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
