# Problem: Count the occurances of the letters of the alphabet in a provided string
import string

the_string = "The Quick Brown Fox, in all it's ruddy colour, Jumps Over the Lazy Dog! ❤️"
lowercase_string = the_string.lower()
string_length = len(lowercase_string)

string_letters = list(lowercase_string)
string_letters.sort()

counts = {}

for count in range(string_length):
    current_letter = string_letters[count]
    if current_letter in counts:
        counts[current_letter] += 1
    else:
        counts[current_letter] = 1

for letter in counts:
    print(f"{letter}: {counts[letter]} ")

