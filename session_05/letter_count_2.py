# Problem: Count the occurances of the letters of the alphabet in a provided string
#
# Loop through each letter in the string
#   add one to the count for the letter
# Display the counts

the_string = "The Quick Brown Fox Jumps Over the Lazy Dog"
counts = [0]*26
lowercase_string = the_string.lower()
ascii_a = ord('a')  # Find the ASCII number for the given character
# 0 .. 127 (ASCII) 0 .. 255 (Extended ASCII)
# 32 = SPACE, 7 = BELL

for letter in lowercase_string:
    if letter.isalpha():
        counts[ord(letter) - ascii_a] += 1

for count in range(26):
    print(f"{chr(ascii_a + count)}: { counts[count]} ", end="")
    if count%5 == 4:
        print()
