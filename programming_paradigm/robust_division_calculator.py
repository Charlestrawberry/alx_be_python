def safe_divide(numerator, denominator):
    try: 
        num = float(numerator)
        denom = float(denominator)

    except ValueError:
        return "Error: Input must be a number"
    
    try:
        result = num /denom
        return f"result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
