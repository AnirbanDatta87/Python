def add(a, b):
    """Function to add two numbers."""
    c = a+b
    return f'Sum = {c}.'
    
def fibonacci(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result