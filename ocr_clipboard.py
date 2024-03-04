import subprocess
import time
import pyperclip
import pytesseract
from PIL import Image, ImageGrab

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def perform_ocr_on_clipboard_image():
    # Get image data from the clipboard and try to open
    try:
        image = ImageGrab.grabclipboard()
    except Exception as e:
        print("Error:", e)
        return

    # Perform OCR on the image and copy to clipboard
    text = pytesseract.image_to_string(image)
    pyperclip.copy(text)

    # Print the extracted text
    print(text)

def main():
    while True:
        # Check the clipboard for changes every second
        current_clipboard_data = pyperclip.paste()
       
        # If the clipboard contains image data, perform OCR
        try:
            perform_ocr_on_clipboard_image()
        except Exception as e:
            continue

        time.sleep(1)

if __name__ == "__main__":
    main()
