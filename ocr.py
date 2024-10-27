#This script loads an image and provides a text-based output of the image
#using the Tesseract OCR engine.
import os

import matplotlib.image as mpimg
import pytesseract


#This function takes an image and returns a string of text
def ocr_image(image):
    #load the image using the Tesseract OCR engine
    lang = detect_language(image)
    text = pytesseract.image_to_string(image, lang=lang)
    print(text)
    return text

#this function takes an image and the string and evaluates how well the string matches the image
def evaluate_image(image, string):
    #load the image using the Tesseract OCR engine
    lang = detect_language(image)
    text = pytesseract.image_to_string(image, lang=lang)
    #print(text)
    #print(string)
    #print(text.find(string))
    if text.find(string) != -1:
        return True
    else:
        return False

#find images in the project folder and return a list of images
def find_images():
    #find all images in the project folder
    images = []
    for file in os.listdir("."):
        if file.endswith(".png") or file.endswith(".jpg"):
            images.append(file)
    return images

#detect the language of the image using Tesseract's image_to_osd method
def detect_language(image):
    osd = pytesseract.image_to_osd(image)
    lang = osd.split("Script: ")[1].split("\n")[0]
    return lang

#start the script and load the images
if __name__ == "__main__":
    images = find_images()
    export_format = 'txt'

    #loop through all images and run the OCR engine on each
    for image in images:
        #run the OCR engine on the image
        text = ocr_image(image)
        image = image[:-4]
        with open(image + '.' + export_format, 'w') as f:
            f.write(text)
            print("Image saved as " + image + '.' + export_format)
            print(evaluate_image('test.png', text))
