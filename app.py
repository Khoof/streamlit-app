import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def main():
    print(Fore.CYAN + "\n🌟 Welcome to the Interactive CLI Calculator 🌟")
    
    while True:
        print(Fore.YELLOW + "\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input(Fore.GREEN + "\nEnter your choice (1/2/3/4/5): ")

        if choice == '5':
            print(Fore.MAGENTA + "Thanks for using the calculator. Goodbye! 👋")
            sys.exit()

        if choice not in ['1', '2', '3', '4']:
            print(Fore.RED + "Invalid choice. Please try again.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = add(num1, num2)
            symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            symbol = '/'

        print(Fore.BLUE + f"\n🧮 Result: {num1} {symbol} {num2} = {result}")

        again = input(Fore.CYAN + "\nDo you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print(Fore.MAGENTA + "Alright! See you next time ✌️")
            break

if __name__ == "__main__":
    main()
