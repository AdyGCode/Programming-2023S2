my_string = 'dongar'
your_string = 'danger'
matching = ' ' * len(my_string)

for position in range(len(my_string)):
    if your_string[position] == my_string[position]:
        matching = matching[:position] + my_string[position] + matching[position + 1:]
print(matching, len(matching))

matching = ''
for position in range(len(my_string)):
    matching += my_string[position] if your_string[position] == my_string[position] else ' '
print(matching, len(matching))
# C#: matching += your_string[position] == my_string[position] ? my_string[position] : ' '


matching = ''
for position in range(len(my_string)):
    (' ', my_string[position])[your_string[position] == my_string[position]]
print(matching, len(matching))
