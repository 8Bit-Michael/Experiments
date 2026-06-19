expenses = [] 
# if you were to do a continue, since the main code is in a while loop and you jut run a function would it inherintly just loop
def add_expense():
    expense_name = input("enter the expense title: ")
    expense_amount = float(input("enter the expense amount: "))
    expenses.append((expense_name, expense_amount))
    print("Expense recorded successfully!")

def all_expenses():
    print("All Expenses:")
    for name, amount in expenses: # Loop through the list of expenses and print each one
            print(f"expense: {name} | Amount: ${amount:.2f}")

def total_expenses():
    total_expense = sum(amount for _, amount in expenses)
    print(f"Total expenses: ${total_expense:.2f}")

def largest_expense():
    most_expensive = 0
    most_expensive_name = ""
    for name, amount in expenses:
        if amount > most_expensive: 
            most_expensive = amount
            most_expensive_name = name    
    print(f"Most expensive expense: {most_expensive_name} (${most_expensive:.2f})")

def remove_expense():
    if not expenses:
        print("No expenses to remove.")
    else:
        print("Expenses:")
        for i, (name, amount) in enumerate(expenses):
            print(f"{i + 1}. {name}: ${amount:.2f}")
        try:
            index = int(input("Enter the number of the expense to remove: ")) - 1 
            # gets index to delete
            if 0 <= index < len(expenses): # if index is valid and within the range of the expenses list
                removed_expense = expenses.pop(index)
                print(f"Expense removed: {removed_expense[0]} (${removed_expense[1]:.2f})")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def save_to_file():
    if not expenses:
        print("No expenses to save.")
    else:
        with open("expenses.txt", "w") as f:
            for name, amount in expenses:
                f.write(f"{name}: ${amount:.2f}\n")
        print("Expenses saved to expenses.txt")

while __name__ == '__main__':
    user_selection = input('Welcome to the Expense Tracker!\n'
                           '1. Add an expense\n'
                           '2. View all expenses\n'
                           '3. View total expenses\n'
                           '4. Largest expense\n'
                           '5. Remove expense\n'
                           '6. Exit\n'
                           '7. Save expenses to file\n'
                           'Please select an option: ')
if user_selection == '1':
    add_expense()

elif user_selection == '2':
    all_expenses()
elif user_selection == '3':
    total_expenses()
elif user_selection == '4': # Largest expense
    largest_expense()
elif user_selection == '5': # Remove expense
    remove_expense()
elif user_selection == '6': # Exit
    print("Exiting the Expense Tracker. Goodbye!")
    exit
elif user_selection == '7': # Save expenses to file
    save_to_file()
    