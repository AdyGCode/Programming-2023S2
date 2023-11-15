from sense_hat import SenseHat
from time import sleep

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLANK = (0, 0, 0)
BLACK = BLANK


def clear_leds(the_sense_hat, colour=BLANK):
    if type(the_sense_hat) == 'SenseHat':
        print("Clear LEDs: Sense Hat is not initialised")
        return

    pixels = [colour] * 64
    the_sense_hat.set_pixels(pixels)


def show_triangle(the_sense_hat, fg=WHITE, bg=BLACK):
    if type(the_sense_hat) == 'SenseHat':
        print("Show Triangle: Sense Hat is not initialised")
        return

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
    clear_leds(sense_hat, BLANK)
    sleep(0.5)
    clear_leds(sense_hat, GREEN)
    sleep(0.5)
    clear_leds(sense_hat, RED)
    sleep(0.5)
    clear_leds(sense_hat, YELLOW)
    sleep(0.5)
    show_triangle(sense_hat, RED,GREEN)
