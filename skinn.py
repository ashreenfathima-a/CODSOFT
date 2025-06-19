from PIL import Image
import matplotlib.pyplot as plt
captions = {
    "dry.jpg": "Dry skin type",
    "normal.jpg": "Normal skin type",
    "oily.jpg": "Oily skin type"
}

def show_image_with_caption(image_filename):
    caption = captions.get(image_filename, "No caption available")
    try:
        img = Image.open(image_filename)
        plt.imshow(img)
        plt.axis("off")
        plt.title("Caption: " + caption)
        plt.show()
    except FileNotFoundError:
        print(f"Error: {image_filename} not found. Please check the filename or path.")
show_image_with_caption("dry.jpg")
show_image_with_caption("normal.jpg")
show_image_with_caption("oily.jpg")
