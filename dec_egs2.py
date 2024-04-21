# Class decorator example:Class decorators are used to modify or enhance the behavior of classes. 
#They are defined similar to function decorators, but they receive a class instead of a function.

def my_class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            print("New method added by the decorator.")
    return NewClass

@my_class_decorator
class MyClass:
    def original_method(self):
        print("Original method of MyClass.")

obj = MyClass()
obj.original_method()
obj.new_method()
