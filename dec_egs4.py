# Decorator with control flow example:Decorator with Control Flow:Decorators can modify the 
#control flow of functions by conditionally executing the original function or bypassing it altogether.
def conditional_decorator(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                print("Decorator condition is not met. Skipping function call.")
        return wrapper
    return decorator

@conditional_decorator(condition=True)
def conditional_function():
    print("This function is conditionally executed.")

conditional_function()

@conditional_decorator(condition=False)
def conditional_function():
    print("This function is conditionally executed.")

conditional_function()
