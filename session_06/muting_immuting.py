number = 7
print(id(number))
number = 9
print(id(number))

my_number = 10
your_number = my_number
print(id(my_number), id(your_number))
print(my_number is your_number)
your_number += 1
print(id(my_number), id(your_number))

letters = '1234567890123456789012345678901234567890'
a = letters
b = '1234567890123456789012345678901234567890'
print(a is b)

name = "Adrian"
print(name)
name = name[:4] + "B" + name[5:]
print(name)
print(name[2:4])

# name[min:max]
# result size = max - min
# eg name[2:4] = 4-2 = 2 characters
#    ri

for count in range(1, 100):
    pass
print(count)

