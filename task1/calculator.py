def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

# ANSI escape codes for colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_calculator_header():
    print(f"{Colors.OKBLUE} ___________________ ")
    print("|                   |")
    print("|    {Colors.BOLD}CALCULATOR{Colors.ENDC}{Colors.OKBLUE}    |")
    print("|___________________|")
    print("|                   |")
    print("|    {Colors.OKGREEN}By oussema hmida{Colors.ENDC}{Colors.OKBLUE}     |")
    print("|___________________|{Colors.ENDC}")

def print_operations_menu():
    print(f"{Colors.OKCYAN} ___________________ ")
    print("|   + For Addition   |")
    print("| - For Subtraction  |")
    print("| / For Division     |")
    print("| * For Multiplication|")
    print("|___________________|{Colors.ENDC}")

print_calculator_header()

while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print_operations_menu()
    
    o = input("Choose one from options: ")
    
    if o == '+':
        result = add(a, b)
    elif o == '-':
        result = subtract(a, b)
    elif o == '/':
        result = divide(a, b)
    elif o == '*':
        result = multiply(a, b)
    else:
        result = f"{Colors.FAIL}Error!!!! Wrong input{Colors.ENDC}"
    
    print(f"{Colors.WARNING} ___________________ ")
    print(f"|      Result:      |")
    print(f"|       {result}       |")
    print("|___________________|{Colors.ENDC}")
    
    another = input("Do you want to perform another calculation? (yes/no): ")
    if another.lower() != 'yes':
        break
