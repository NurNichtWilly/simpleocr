#This script loads an image and provides a text-based output of the image
#using the Tesseract OCR engine.


import matplotlib.image as mpimg
import pytesseract


#This function takes an image and returns a string of text
def ocr_image(image):
    #load the image using the Tesseract OCR engine
    text = pytesseract.image_to_string(image, lang='eng')
    print(text)
    return text

#this function takes an image and the string and evaluates how well the string matches the image
def evaluate_image(image, string):
    #load the image using the Tesseract OCR engine
    text = pytesseract.image_to_string(image, lang='eng')
    #print(text)
    #print(string)
    #print(text.find(string))
    if text.find(string) != -1:
        return True
    else:
        return False


#start the script and load the image
if __name__ == "__main__":
    export_format = 'sql'
    image = 'test.png'
    text = ocr_image('test.png')
    #save the image as a markdown file
    with open('export.'+export_format, 'w') as f:
        f.write(text)
    print("Image saved as test.md")
    print(evaluate_image('test.png', text))

