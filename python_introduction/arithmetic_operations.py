

def perform_operation():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    if operation == 'add':
        result = num1 + num2
    elif operation == "subtract":
        result = num1-num2
    elif operation == "multiply":
        result = num1*num2
    elif operation == "divide":
        if num2 == 0 and operation == "divide":
            print("Error: Division by zero is not allowed.")
        
        result = num1/num2
      
    print(f"The answer is: {result}")
perform_operation()