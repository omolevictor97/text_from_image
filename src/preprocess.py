from PIL import Image, ImageEnhance
import os

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L') # convert to grayscale
    image = ImageEnhance.Contrast(image).enhance(2.0) # Enhance contrast

    return image
