class Income:

    def __init__(self):
        self.total_income = 0

    def add_income(self):
        try:
            amount = float(input("Enter your income: "))

            if amount > 0:
                self.total_income += amount
                print("Income added successfully!")

            else:
                print("Invalid income!")

        except ValueError:
            print("Please enter a valid number!")