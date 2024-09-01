from PIL import Image
import time
import os
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

# ASCII characters used to build the output text
ASCII_CHARS = ["█", "▓", "▒", "░", "■", "□"]

# Corresponding color for each ASCII character
ASCII_COLORS = [
    Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA,
    Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX
]

# Resize image while maintaining aspect ratio


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width / 1.65  # Adjust aspect ratio
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert image to grayscale


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to ASCII characters with corresponding colors


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_char = ASCII_CHARS[pixel // 25]  # Determine ASCII character
        # Determine corresponding color
        ascii_color = ASCII_COLORS[pixel // 25]
        ascii_str += ascii_color + ascii_char  # Combine color and character
    return ascii_str

# Convert image to ASCII


def image_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Format the ASCII string into lines of the correct width
    ascii_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:i + new_width]
                          for i in range(0, ascii_len, new_width)])
    return ascii_img

# Stream ASCII art character by character to terminal


def stream_ascii_art(ascii_art):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    for char in ascii_art:
        print(char, end='', flush=True)
        time.sleep(0.002)  # Adjust delay for effect

# Load image and convert to ASCII art


def main(image_path, width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return

    ascii_art = image_to_ascii(image, width)
    stream_ascii_art(ascii_art)


if __name__ == "__main__":
    image_path = "pepe_rasenganq.png"  # Replace with your image path
    main(image_path, 100)
