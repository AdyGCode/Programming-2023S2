from sense_hat import SenseHat
from time import sleep

# COLOUR NAME = ( RED, GREEN, BLUE) - three ints 0-255
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


def clear_leds(the_sense_hat, colour=BLACK):
    if not isinstance(the_sense_hat, SenseHat):
        print("Clear LEDs: Sense Hat is not initialised")
        raise TypeError

    pixels = [colour] * 64
    the_sense_hat.set_pixels(pixels)


def show_triangle(the_sense_hat, fg=WHITE, bg=BLACK):
    if not isinstance(the_sense_hat, SenseHat):
        print("Show Triangle: Sense Hat is not initialised")
        raise TypeError

    pixels = [
        bg, bg, bg, bg, bg, bg, bg, bg,
        bg, bg, bg, bg, bg, bg, bg, bg,
        bg, bg, bg, bg, bg, bg, bg, bg,
        bg, bg, bg, bg, fg, bg, bg, bg,
        bg, bg, bg, fg, fg, fg, bg, bg,
        bg, bg, fg, fg, fg, fg, fg, bg,
        bg, fg, fg, fg, fg, fg, fg, fg,
        bg, bg, bg, bg, bg, bg, bg, bg,
    ]

    the_sense_hat.set_pixels(pixels)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sense_hat = SenseHat()
    print(type(sense_hat))
    clear_leds(sense_hat, BLACK)
    sleep(2)
    clear_leds(sense_hat, GREEN)
    sleep(2)
    clear_leds(sense_hat, RED)
    sleep(2)
    clear_leds(sense_hat, YELLOW)
    sleep(2)
    show_triangle(sense_hat, RED, GREEN)
