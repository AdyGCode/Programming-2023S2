# Write a function to draw a box on the screen
# the function will be given a width (characters) and height (lines)
poem = ['My code fails.', 'I do not know why.', 'My code works.', 'I do not know why.']

box_width = 10
box_height = len(poem)


def draw_box_with_content(content=[], width=72, height=3):
    max_width = width
    box_height = height
    content_height= len(content)
    for line in poem:
        max_width = len(line) if len(line) > max_width else max_width
    box_width = max_width + 4
    actual_width = box_width - 2

    box_height = (content_height
                  + 2) if content_height > box_height else box_height

    top_line = f'+{"-" * actual_width}+'

    print(top_line)
    for line in content:
        mid_line = f'|{line:^{actual_width}}|'
        print(mid_line)
    for line in range(content_height, box_height):
        mid_line = f'|{" "*actual_width}|'
        print(mid_line)
    print(top_line)


draw_box_with_content(poem, box_width, box_height)
print()
draw_box_with_content(poem, 60, 0)
