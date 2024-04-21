# Function decorator example:Function Decorator:Function decorators 
#are used to modify or enhance the behavior of functions. 
#They are defined using the @decorator_name syntax.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
