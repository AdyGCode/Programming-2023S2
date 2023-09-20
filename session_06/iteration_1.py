my_list = [2, 3, 5, 7, 9]
total = 0

for value in my_list:
    total += value
print(total)

total = sum(my_list)
print(total)

my_dictionary = {
    'name': 'Adrian',
    'age': 24,
    'location': 'Perth'
}

for key in my_dictionary:
    print(key, my_dictionary[key])

for key, value in my_dictionary.items():
    print(key, value)

