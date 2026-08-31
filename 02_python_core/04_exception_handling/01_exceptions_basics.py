
def safe_divide(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")

    except TypeError:
        print("❌ Error: Inputs must be numbers!")

    else:
        print(f"Result of {a} / {b} = {result}")

def safe_read(file_path):

    try:
        with open(file_path, 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' does not exist!")

    else:
        print(content.strip())


# Test calls
safe_divide(10, 2)
safe_divide(10, 0)
safe_read("02_python_core/04_exception_handling/test.txt")