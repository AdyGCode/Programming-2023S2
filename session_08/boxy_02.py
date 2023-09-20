# Write a function to draw a box on the screen
# the function will be given a width (characters) and height (lines)

box_width = 20
box_height = 5


def draw_box(width=72, height=3):
    top_line = f'+{"-"*(width-2)}+'
    mid_line = f'|{" "*(width-2)}|'
    print(top_line)
    for line in range(height-2):
        print(mid_line)
    print(top_line)


draw_box(box_width, box_height)
draw_box()
draw_box(box_width)
draw_box(height=box_height)
draw_box(height=box_height, width=4)