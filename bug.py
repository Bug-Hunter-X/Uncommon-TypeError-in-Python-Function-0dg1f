def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        return "Error: Invalid input types"
    except ZeroDivisionError:
        return "Error: Division by zero"

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, "2")) # Output: Error: Invalid input types
print(function_with_uncommon_error(10)) #Output: TypeError: function_with_uncommon_error() missing 1 required positional argument: 'b'