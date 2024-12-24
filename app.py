import streamlit as st
from PIL import Image
from src.ocr_engine import extract_text_from_image
from src.preprocess import preprocess_image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


st.title('Text Extraction from Images')
st.divider()
uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    image = image.convert('L')

    st.image(image, caption='Uploaded Image')
    text = pytesseract.image_to_string(image)
    st.write(text)

st.divider()
st.markdown("<h2> You can take live Image below </h2>", unsafe_allow_html = True)

if st.button('Capture Image'):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error('WebCam not accessible!')
    else:
        st.text("Hit 'Space' to capture an image and 'Q' to quit")

        while True:
            ret, frame = cap.read()

            if not ret:
                st.error('Failed to capture image')
                break
            #cv2.imshow('WebFrame', frame)#
            #listen for keyboard instruction

            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '): # Use space to capture
                captured_frame = frame
                st.image(captured_frame, channels="BGR", caption="Captured Image")
                cap.release()
                cv2.destroyAllWindows()
                break
            elif key == ord('q'): # Use Q to quit
                cap.release()
                cv2.destroyAllWindows()
                break

if "captured_frame" in locals():
    pil_image = Image.fromarray(cv2.cvtColor(captured_frame, cv2.COLOR_BGR2RGB))
    st.image(pil_image, caption="Captured Image")

    text = pytesseract.image_to_string(pil_image)
    st.write('Extracted Text: \n')
    st.write(text)
            



