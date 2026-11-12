class Expenses:

    def __init__(self):
        self.expenses = {}

    def add_expense(self):

        category = input("Enter expense category: ")

        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Invalid amount!")
                return

            self.expenses[category] = (
                self.expenses.get(category, 0) + amount
            )

            print("Expense recorded successfully!")

        except ValueError:
            print("Please enter a valid amount!")

    def total_expenses(self):

        return sum(self.expenses.values())