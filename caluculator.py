import re

def calculate(expression):
    try:
        # Remove any spaces in the expression
        expression = expression.replace(" ", "")
        # Using regular expression to filter the input
        if not re.match(r'^[\d\+\-\*\/\(\)\.]*$', expression):
            return "Invalid input"
        
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

def main():
    print("Welcome to Simple Calculator")
    print("Enter 'quit' to exit")

    while True:
        user_input = input()

        if user_input.lower() == 'quit':
            break

        result = calculate(user_input)
        print("Result:", result)

if __name__ == "__main__":
    main()
