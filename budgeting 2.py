
# SMARTBUDGET APP

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

    if username == admin_username or username in users:
        print("Username already exists!")
    else:
        users[username] = {
            "password": password,
            "income": 0,
            "expenses": {},
            "savings_goal": 0
        }
        print("Account created successfully!") 
elif choice == "2":
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == admin_username and password == admin_password:

        print("\n===== ADMIN DASHBOARD =====")

        while True:
            print("\n1. View All Users")
            print("2. View User Details")
            print("3. Total Registered Users")
            print("4. Exit Admin Dashboard")

            option = input("Choose option: ")

            if option == "1":
                print("\nREGISTERED USERS:")

                if len(users) == 0:
                    print("No users registered.")
                else:
                    for name in users:
                        print("-", name)

            elif option == "2":
                name = input("Enter username to view: ")

                if name in users:
                    user = users[name]

                    total_expenses = sum(
                        user["expenses"].values()
                    )

                    balance = user["income"] - total_expenses

                    print("\n===== USER DETAILS =====")
                    print("Username:", name)
                    print("Income:", user["income"])
                    print("Expenses:", total_expenses)
                    print("Balance:", balance)
                    print("Savings Goal:", user["savings_goal"])

                    print("\nEXPENSE CATEGORIES:")

                    for category, amount in user["expenses"].items():
                        print(category, ":", amount)

                else:
                    print("User not found!")

            elif option == "3":
                print("Total users:", len(users))

            elif option == "4":
                print("Admin logged out.")
                break
 
            else:
                print("Invalid option!")
    elif username in users and users[username]["password"] == password:

        print("\nWELCOME TO SMARTBUDGET!")

        while True:
            print("\n===== USER MENU =====")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. Set Savings Goal")
            print("5. View Financial Report")
            print("6. Logout")

            option = input("Choose option: ")

            if option == "1":
                amount = float(input("Enter income: "))
                users[username]["income"] += amount
                print("Income added!")

            elif option == "2":
                category = input("Expense category: ")
                amount = float(input("Expense amount: "))

                expenses = users[username]["expenses"]

                expenses[category] = (
                    expenses.get(category, 0) + amount
                )

                print("Expense recorded!")

            elif option == "3":
                income = users[username]["income"]
                expenses = sum(
                    users[username]["expenses"].values()
                )

                print("Balance:", income - expenses)

            elif option == "4":
                goal = float(input("Enter savings goal: "))
                users[username]["savings_goal"] = goal
                print("Savings goal saved!")

            elif option == "5":
                user = users[username]
                total = sum(user["expenses"].values())
                balance = user["income"] - total

                print("\n===== FINANCIAL REPORT =====")
                print("Income:", user["income"])
                print("Expenses:", total)
                print("Balance:", balance)
                print("Savings Goal:", user["savings_goal"])

                for category, amount in user["expenses"].items():
                    print(category, ":", amount)

            elif option == "6":
                print("Logged out successfully!")
                break

            else:
                print("Invalid option!")

    else:
        print("Invalid username or password!")

else:
    print("Invalid selection!")
