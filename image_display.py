# image_display.py
from PIL import Image

def display_image(image_path):
    try:
        image = Image.open(image_path)

        # Resize the image to fit the terminal width
        terminal_width = 80
        aspect_ratio = image.width / image.height
        new_width = min(terminal_width, image.width)
        new_height = int(new_width / aspect_ratio)

        resized_image = image.resize((new_width, new_height))
        resized_image.show()

    except Exception as e:
        print(f"Error: {e}")
