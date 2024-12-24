import os
import sys
from src.ocr_engine import extract_text_from_image
from src.preprocess import preprocess_image
from PIL import Image


sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
import constants


inputs = os.path.join(os.getcwd(), constants.INPUT_PATH)
def main():
    # Load the image from the file path
    for filename in os.listdir(inputs):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            input_path = os.path.join(inputs, filename)
            im = Image.open(input_path)
            im.show()
            # Preprocess the image

            preprocessed = preprocess_image(input_path)
            text = extract_text_from_image(preprocessed)
            print(f'Text from filename: {filename} - {text} \n')

if __name__ == "__main__":
    main()

