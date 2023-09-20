# Problem: Count the occurances of the letters of the alphabet in a provided string
import string

the_string = "The Quick Brown Fox, in all it's ruddy colour, Jumps Over the Lazy Dog! ❤️"
lowercase_string = the_string.lower()
string_length = len(lowercase_string)
ascii_a = ord('a')  # Find the ASCII number for the given character
ascii_z = ord('z')
# 0 .. 127 (ASCII) 0 .. 255 (Extended ASCII)
# 32 = SPACE, 7 = BELL


string_letters = list(lowercase_string)

counts = {}
for letter in string.ascii_lowercase:
    counts[letter]=0
for numbers in string.digits:
    counts[numbers]=0
for symbol in string.punctuation:
    counts[symbol]=0

discarded = 0

for count in range(string_length):
    current_letter = string_letters[count]
    if current_letter in string.punctuation or current_letter.isalnum():
        counts[current_letter] += 1
    else:
        discarded += 1

for letter in counts:
    print(f"{letter}: {counts[letter]} ")

print(f"Discarded: {discarded}")
