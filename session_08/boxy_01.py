# Write a function to draw a box on the screen
# the function will be given a width (characters) and height (lines)

box_width = 20
box_height = 5

# top line
top_line = f'+{"-"*(box_width-2)}+'
mid_line = f'|{" "*(box_width-2)}|'


print('123456789012345678901234567890')
print(top_line)
for line in range (box_height-2):
    print(mid_line)
print(top_line)
