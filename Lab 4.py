# try/except - the basics
print("try/except - the basics")
try:
    age = int(input("Enter age: "))
    result = 100 / age

except ValueError:
    print("That's not a number.")

except ZeroDivisionError:
    print("Age can't be zero.")

# else and finally 
print("else and finally ")

try:
    age = int(input("Enter age: "))
    result = 100 / age

except ValueError:
    print("Please enter a number.")

except ZeroDivisionError:
    print("Age cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")

#Decorator:A decorator is a function that adds extra functionality to another function without changing the original function.
print("Decorator")
def my_decorator(func):

    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")

    return wrapper


@my_decorator
def greet(name):
    print("Hello", name)


greet("Wisam")

#Raising Your Own Exceptions
print("Raising Your Own Exceptions")
class AgeError(Exception):
    pass


try:
    age = 15

    if age < 18:
        raise AgeError("You must be 18 or older")

except AgeError as e:
    print("Error:", e)