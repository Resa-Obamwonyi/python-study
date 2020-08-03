# Algorithm to covert integers to words
phone_no = input("Enter Phone Number: ")
digit_map = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
    }

output = ""

for number in phone_no:
    output += digit_map.get(number) + " "

print(output)

#