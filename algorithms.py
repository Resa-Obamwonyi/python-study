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


# Algorithm to return the sum of the number of vowels in  a string


def count_vowels(txt):
    return sum([1 for x in txt.lower() if x in 'aeiou'])


print(count_vowels("Olympus has fallen"))

# txt.lower converts the string to lower case to avoid errors
# sum() keyword sums everything up
# return 1 for everytime you find x in txt.lower and if x is also in the vowel string "aeiou"
