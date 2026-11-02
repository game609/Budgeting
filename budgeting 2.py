users = {}
admin_username = "admin"
admin_password = "admin123"
print("===== SMARTBUDGET =====")
print("1. Register")
print("2. Login")
choice = input("Choose an option: ")
if choice == "1":
    username = input("Create username: ")
    password = input("Create password: ")

    if username in users:
        print("Username already exists!")
    else:
        users[username] = {
            "password": password,
            "income": 0,
            "expenses": {},
            "savings_goal": 0
        }
        print("Account created successfully!")
if choice == "2" or choice == "1" and username in users:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username]["password"] == password:

        print("\nWELCOME TO SMARTBUDGET!")

        while True:
            print("\n===== MAIN MENU =====")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. Set Savings Goal")
            print("5. View Financial Report")
            print("6. Exit")

            option = input("Choose an option: ")
            if option == "1":
                income = float(input("Enter your income: "))
                users[username]["income"] += income
                print("Income added successfully!")
            elif option == "2":
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))

                expenses = users[username]["expenses"]

                expenses[category] = expenses.get(category, 0) + amount

                print("Expense recorded successfully!")
            elif option == "3":
                income = users[username]["income"]
                expenses = users[username]["expenses"]

                total_expenses = sum(expenses.values())
                balance = income - total_expenses

                print("Remaining balance:", balance)
            elif option == "4":
                goal = float(input("Enter savings goal: "))
                users[username]["savings_goal"] = goal

                print("Savings goal saved!")
            elif option == "5":
                income = users[username]["income"]
                expenses = users[username]["expenses"]

                total_expenses = sum(expenses.values())
                balance = income - total_expenses

                print("\n===== FINANCIAL REPORT =====")
                print("Username:", username)
                print("Total income:", income)
                print("Total expenses:", total_expenses)
                print("Remaining balance:", balance)
                print("Savings goal:",
                      users[username]["savings_goal"])

                print("\nEXPENSE CATEGORIES:")
                for category, amount in expenses.items():
                    print(category, ":", amount)

                if balance < 0:
                    print("WARNING: You have exceeded your income!")
                else:
                    print("You are managing your money well!")
            elif option == "6":
                print("Thank you for using SmartBudget!")
                break

            else:
                print("Invalid option. Try again.")

    else:
        print("Invalid username or password!")

else:
    if choice != "1":
        print("Invalid selection!")
  