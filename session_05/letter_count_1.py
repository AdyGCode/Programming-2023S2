# Proble: Count the occurances of the letters of the alphabet in a provided string
#
# Loop through each letter in the string
#   add one to the count for the letter
# Display the counts

the_string = "The Quick Brown Fox Jumped Over the Lazy Dog"
count_a = 0
count_b = 0
count_c = 0
count_d = 0
lowercase_string = the_string.lower()

for letter in lowercase_string:
    if letter == 'a':
        count_a += 1
    if letter == 'b':
        count_b += 1
    if letter == 'c':
        count_c += 1
    if letter == 'd':
        count_d += 1

print(f"A: {count_a}, B: {count_b}, C: {count_c}, D: {count_d}")
