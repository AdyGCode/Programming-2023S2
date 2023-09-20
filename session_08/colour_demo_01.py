from colored import fg, Fore, Back, Style
import colored
import math

color = fg('blue')
print (color + 'Hello World !!!')

print(f'{Fore.white}{Back.green}Colored is Awesome!!!{Style.reset}')
print (f'{Fore.black}{Back.red}{Style.blink}EEEEK!{Style.reset}')

# https://dslackw.gitlab.io/colored
real = 100*math.pi
integer = 1234567890
string = "hello there"

print(f'Integer: {integer:20}')
print(f'Real   : |{real:20.5f}|{real:20.5}|{real:.5}|{real:.5f}|')
print(f'String : |{string:^20}|{string:<20}|{string:>20}|')

print(f'+{"-"*10}+')
print(f'|{" "*10}|')
print(f'+{"-"*10}+')