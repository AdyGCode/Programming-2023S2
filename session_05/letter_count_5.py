# Problem: Count the occurances of the letters of the alphabet in a provided string
#
# Loop through each letter in the string
#   add one to the count for the letter
# Display the counts

the_string = "The Quick Brown Fox Jumps Over the Lazy Dog"
lowercase_string = the_string.lower()
string_length = len(lowercase_string)
ascii_a = ord('a')  # Find the ASCII number for the given character
ascii_z = ord('z')
# 0 .. 127 (ASCII) 0 .. 255 (Extended ASCII)
# 32 = SPACE, 7 = BELL

string_letters = list(lowercase_string)

counts = [0] * (ascii_z - ascii_a+1)
letters = []
for letter in range(ascii_a, ascii_z + 1):
    letters.append(chr(letter))

for index in range(ascii_z-ascii_a+1):
    letter = letters[index]
    for count in range(string_length):
        if letter == string_letters[count]:
            counts[index] += 1
            string_letters[count] = " "

for count in range(26):
    print(f"{chr(ascii_a + count)}: {counts[count]} ", end="")
    if count % 5 == 4:
        print()
