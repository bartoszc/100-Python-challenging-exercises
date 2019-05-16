def calculate(a, b=0):
    """Write a function to compute 5/0 and use try/except to catch the exceptions."""
    try:
        result = a/b
        print('Result:', result)
    except ZeroDivisionError as m:
        print(m)
    finally:
        print('In finally block for cleanup')


calculate(5, 0)
