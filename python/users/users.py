class User:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.income = Income()
        self.expenses = Expenses()
        self.savings = Savings()

    def view_balance(self):

        total_income = self.income.total_income
        total_expenses = self.expenses.total_expenses()

        balance = total_income - total_expenses

        print("\n===== YOUR BALANCE =====")
        print("Income:", total_income)
        print("Expenses:", total_expenses)
        print("Balance:", balance)

    def financial_report(self):

        total_income = self.income.total_income
        total_expenses = self.expenses.total_expenses()

        balance = total_income - total_expenses

        print("\n===== FINANCIAL REPORT =====")

        print("Username:", self.username)
        print("Income:", total_income)
        print("Expenses:", total_expenses)
        print("Remaining balance:", balance)
        print("Savings goal:", self.savings.savings_goal)

        print("\nEXPENSE CATEGORIES:")

        for category, amount in self.expenses.expenses.items():

            print(category, ":", amount)

        if balance < 0:
            print("WARNING: You have exceeded your income!")

        else:
            print("You are managing your money well!")