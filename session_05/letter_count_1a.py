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
count_e = 0
count_f = 0
count_g = 0
count_h = 0
lowercase_string = the_string.lower()

for letter in lowercase_string:
    count_a += 1 if letter == 'a' else 0
    count_b += 1 if letter == 'b' else 0
    count_c += 1 if letter == 'c' else 0
    count_d += 1 if letter == 'd' else 0
    count_e += 1 if letter == 'e' else 0
    count_f += 1 if letter == 'f' else 0
    count_g += 1 if letter == 'g' else 0
    count_h += 1 if letter == 'h' else 0

print(f"A: {count_a}, B: {count_b}, C: {count_c}, D: {count_d}")
print(f"E: {count_e}, F: {count_f}, G: {count_g}, H: {count_h}")

