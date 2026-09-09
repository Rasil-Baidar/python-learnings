def divide(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a)/float(b)

def exception_lesson():
    try:
        result = divide(10, 0)
        print(result)
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Division completed")
