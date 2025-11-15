operation = ("+,-,*,/")

num1 = int(input("Enter the first number:" ))
num2 = int(input("Enter the second number:" ))  
operation = input("Choose the operation (+, -, *, /): ")    
if num2 == 0 and operation == '/':
        print("Cannot divide by zero.")
match operation:
        case '+':
            print("The result is", num1 + num2)
        case '-':
            print("The result is", num1 - num2)
        case '*':
            print("The result is", num1 * num2)
        case '/': 
            num2 != 0
            print("The result is", num1 / num2)

    