expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = input("Enter amount: ")

        expenses.append((item, amount))

        with open("expenses.txt", "a") as file:
            file.write(f"{item} - ₹{amount}\n")

        print("Expense Added!")

    elif choice == "2":
        try:
            with open("expenses.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No expenses added yet.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")
