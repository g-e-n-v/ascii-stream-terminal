from ascii_magic import AsciiArt
import time
import os

ASCII_CHARS = ["█", "▓", "▒", "░", "■", "□"]

my_art = AsciiArt.from_image('pepe_rasenganq.png')
chars = my_art.to_ascii(columns=100, char='▒')


def stream_ascii_art(ascii_art):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    for char in ascii_art:
        print(char, end='', flush=True)
        time.sleep(0.0001)  # Adjust delay for effect


stream_ascii_art(chars)
