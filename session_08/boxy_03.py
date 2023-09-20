# Write a function to draw a box on the screen
# the function will be given a width (characters) and height (lines)
poem = ['My code fails.', 'I do not know why.', 'My code works.', 'I do not know why.']

max_width = 0
for line in poem:
    max_width = len(line) if len(line) > max_width else max_width

box_width = max_width + 4
box_height = len(poem) + 2


def draw_box_with_content(content=[], width=72, height=3):
    actual_width = width - 2
    top_line = f'+{"-" * actual_width}+'
    print(top_line)
    for line in content:
        mid_line = f'|{line:^{actual_width}}|'
        print(mid_line)
    print(top_line)


draw_box_with_content(poem, box_width, box_height)
