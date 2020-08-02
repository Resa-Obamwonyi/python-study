# Basic If Statement

is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a Tall Male")
elif is_male and not (is_tall):
    print("You are a Short Male")
elif not (is_male) and is_tall:
    print("You are not male, but are Tall")
else:
    print("You are not Male and are not Tall")


# If statements and Comparisons
# Return Maximum Number

def max_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3


print(max_num(39, 78, 5))
