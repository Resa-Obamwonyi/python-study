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

#assign the decorator function to a variable, using the function to be work upon as the argument.
decorate = uppercase_decorator(say_hi)

#print the variable to screen.
print(decorate())




#short method of applying decorator to a function
@uppercase_decorator #just write the decorate like this just before the function to be decorated.

def testMethod():
    return "i am testing the new method"

print(testMethod())




# defining decorators with arguments, the arguments are passed in the wrapper 
# and will be passed to the decorated function during execution call
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")




#defining general purpose args using "*args" and "**kwargs"
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

#using positional arguments
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a,b):
    print(a,b)

#using keyword arguments
@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")


function_with_no_argument()
function_with_arguments("Hey", "Hello")
function_with_keyword_arguments(first_name="Resa", last_name="Obamwonyi")




#passing arguments to a decorator
def decorator_maker_with_args(arg1, arg2, arg3):
    def decorator(function):
        def decorator_wrapper_function(func_arg1, func_arg2, func_arg3):
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function".format(arg1, arg2, arg3, func_arg1, func_arg2, func_arg3))
            return function(func_arg1, func_arg2, func_arg3)
        return decorator_wrapper_function
    return decorator


@decorator_maker_with_args("Plant", "Air", "Trees")
def function_to_be_decorated(arg1, arg2, arg3):
    print("I think this shows my decoration arguments")

function_to_be_decorated("Fish", "Eggs", "Somethings")





#using functools to save meta data and reduce debugging issues. 
import functools #do not forget to import

def new_uppercase_decorator(func):
    @functools.wraps(func) #just drop this here with the proper arguments
    def wrapper():
        return func().upper()
    return wrapper
@new_uppercase_decorator

def new_say_hi():
    "This will say hi"
    return 'hello there'

print(new_say_hi())