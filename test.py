import re

pattern = r'(\d+)'

output = re.search(pattern, '/books/2020/names')

print(output.groups())

# I should get this tuple printed out => (2020,)