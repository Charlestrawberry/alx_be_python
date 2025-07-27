def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "enter correct value"
    else:
        return "Invalid operation. Please choose add, subtract, multiply, or divide."       
    

perform_operation(10, 5, "add")  
    
