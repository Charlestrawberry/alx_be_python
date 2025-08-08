class Calculator:
    calculation_type = "Arithmetic Operations" #class attribute
        
    @staticmethod 
    def add(a, b):
        sum = a + b
        return sum
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

if __name__ == "__main__":
    # using the @static mthd
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # using the @class mthd
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
