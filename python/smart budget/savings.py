class Savings:

    def __init__(self):
        self.savings_goal = 0

    def set_goal(self):

        try:
            goal = float(input("Enter savings goal: "))

            if goal > 0:
                self.savings_goal = goal
                print("Savings goal saved!")

            else:
                print("Invalid savings goal!")

        except ValueError:
            print("Please enter a valid number!")