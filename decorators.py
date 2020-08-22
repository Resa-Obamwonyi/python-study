#assigning functions to variables
def decorate(num):
    return num + 1


add_one = decorate
print(add_one(6))



#defining a function inside another function
def funcOne(num):
    def funcTwo(num):
        return num + 1

    result = funcTwo(num)
    return result

print(funcOne(6))



#passing functions as arguments to other functions
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))



#returning a function inside another function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello())



# Nested Functions have access to the Enclosing Function's Variable Scope
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")


# simple decorator that converts a sentence to uppercase
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def say_hi():
    return 'Did this work?'

#assign thr decorator function to a variable, using the function to be work upon as the argument.
decorate = uppercase_decorator(say_hi)

#print the variable to screen.
print(decorate())