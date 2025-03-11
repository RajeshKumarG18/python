num1 = 2
num2 = 4

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return (num1 - num2)
    elif operator == '*':
        return (num1 * num2)
    elif operator == '/':
        return num1 / num2
def main():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /):")
        result = calculate(num1, num2, operator)
        print(f"The result is: {result}")
if __name__ == "__main__":
    main()