'''6 uzduotis'''
# •	Create a program that asks to enter the length and width of a rectangle.
# •	Create a function that takes length and width, calculates the area and perimeter, and returns them.
# •	Print the returned result to the terminal.
# •	Also, add a logger to the program and log the result (area and perimeter) to a file.

# lenght = int(input("type lenght of rectangle "))
# width = int(input("type width of rectangle "))
#
# def rectangle(x,y):
#     perimert = (x+y) * 2
#     area = x * y
#     return perimert, area
#
# answer = rectangle(lenght, width)
#
# print(f"Perimetr of rectangle of {lenght} and {width} is {answer[0]}")
# print(f"Area of rectangle of {lenght} and {width} is {answer[1]}")
'''7 uzduotis'''


class BankAccount:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance

    def add_money(self):
        how_money_add = int(input("How much money do you want to add? "))
        self.balance = self.balance + how_money_add
        return self.balance


h1 = BankAccount(232323, 34)
print(h1.add_money())
# while:
#     operation = input("1. add balance \ntype an operation what do you want:")


# 6 uzduotis
import logging
# Configure logger
logging.basicConfig(filename='rectangle.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# Function to calculate the area and perimeter of a rectangle
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    # Log the calculations
    logging.info(f"Rectangle - Length: {length}, Width: {width}")
    logging.info(f"Area: {area}, Perimeter: {perimeter}")
    return area, perimeter
# Prompt user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
# Calculate the area and perimeter of the rectangle
area, perimeter = calculate_rectangle_properties(length, width)
# Print the calculated results
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
# 7 uzduotis
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return "Deposit successful"
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return "Withdrawal successful"
    def get_balance(self):
        return self.balance
# Create a bank account object
account = BankAccount("1234567890")
# Deposit funds
print(account.deposit(1000))
# Withdraw funds
print(account.withdraw(500))
# Check account balance
balance = account.get_balance()
print("Account Balance:", balance)
# 8 uzduotis
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    def display_books(self):
        print(f"Books available in {self.name}:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} by {book.author}")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' by {self.author} checked out successfully.")
        else:
            print(f"Book '{self.title}' by {self.author} is currently not available.")
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.title}' by {self.author} returned.")
        else:
            print(f"Book '{self.title}' by {self.author} was not checked out.")
# Usage
library = Library("City Library")
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")
library.display_books()
book_to_check_out = library.books[0]
book_to_check_out.check_out()
library.display_books()
book_to_check_out.return_book()
library.display_books()
# 9 uzduotis
class Task:
    def __init__(self, description, status="To Do"):
        self.description = description
        self.status = status
    def display_info(self):
        print(f"Task: {self.description}")
        print(f"Status: {self.status}")
        print("--------------------")
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.description}' added to the To-Do List.")
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do List.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                task.display_info()
    def mark_as_done(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.status = "Done"
                print(f"Task '{task.description}' marked as Done.")
                return
        print(f"Task '{task_description}' not found in the To-Do List.")
todo_list = ToDoList()
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Done")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        task_description = input("Enter task description: ")
        new_task = Task(task_description)
        todo_list.add_task(new_task)
    elif choice == "2":
        todo_list.display_tasks()
    elif choice == "3":
        task_description = input("Enter task description to mark as done: ")
        todo_list.mark_as_done(task_description)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
# 10 uzduotis
class CoffeeMachine:
    def __init__(self):
        self.water_level = 100  # Initial water level
        self.coffee_beans_level = 50  # Initial coffee beans level
        self.milk_level = 30  # Initial milk level
    def brew_espresso(self):
        if self.water_level >= 30 and self.coffee_beans_level >= 15:
            print("Brewing Espresso...")
            self.water_level -= 30
            self.coffee_beans_level -= 15
            print("Espresso is ready!")
        else:
            print("Insufficient resources to brew Espresso. Please refill.")
    def brew_latte(self):
        if self.water_level >= 30 and self.coffee_beans_level >= 15 and self.milk_level >= 10:
            print("Brewing Latte...")
            self.water_level -= 30
            self.coffee_beans_level -= 15
            self.milk_level -= 10
            print("Latte is ready!")
        else:
            print("Insufficient resources to brew Latte. Please refill.")
    def refill_water(self, amount):
        self.water_level += amount
        print(f"Water refilled by {amount} units.")
    def refill_coffee_beans(self, amount):
        self.coffee_beans_level += amount
        print(f"Coffee beans refilled by {amount} units.")
    def refill_milk(self, amount):
        self.milk_level += amount
        print(f"Milk refilled by {amount} units.")
    def display_status(self):
        print(f"\nCurrent Water Level: {self.water_level} units")
        print(f"Current Coffee Beans Level: {self.coffee_beans_level} units")
        print(f"Current Milk Level: {self.milk_level} units")
coffee_machine = CoffeeMachine()
while True:
    print("\nActions:")
    print("1. Brew Espresso")
    print("2. Brew Latte")
    print("3. Refill Water")
    print("4. Refill Coffee Beans")
    print("5. Refill Milk")
    print("6. Display Status")
    print("0. Exit")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        coffee_machine.brew_espresso()
    elif choice == "2":
        coffee_machine.brew_latte()
    elif choice == "3":
        amount = int(input("Enter the amount to refill water: "))
        coffee_machine.refill_water(amount)
    elif choice == "4":
        amount = int(input("Enter the amount to refill coffee beans: "))
        coffee_machine.refill_coffee_beans(amount)
    elif choice == "5":
        amount = int(input("Enter the amount to refill milk: "))
        coffee_machine.refill_milk(amount)
    elif choice == "6":
        coffee_machine.display_status()
    elif choice == "0":
        print("Exiting the Coffee Machine. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a valid number.")