#This script loads an image and provides a text-based output of the image
#using the Tesseract OCR engine.
import os
import argparse
import logging
from typing import List

import matplotlib.image as mpimg
import pytesseract


#This function takes an image and returns a string of text
def ocr_image(image: str) -> str:
    """Nimmt einen Bilddateipfad und gibt den extrahierten Text zurück."""
    try:
        lang = detect_language(image)
        text = pytesseract.image_to_string(image, lang=lang)
        logging.info(f"OCR für {image} erfolgreich.")
        return text
    except Exception as e:
        logging.error(f"Fehler bei OCR für {image}: {e}")
        return ""

#this function takes an image and the string and evaluates how well the string matches the image
def evaluate_image(image: str, string: str) -> bool:
    try:
        lang = detect_language(image)
        text = pytesseract.image_to_string(image, lang=lang)
        return string in text
    except Exception as e:
        logging.error(f"Fehler bei der Auswertung von {image}: {e}")
        return False

#find images in the project folder and return a list of images
def find_images(directory: str) -> List[str]:
    images = []
    for file in os.listdir(directory):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            images.append(os.path.join(directory, file))
    return images

#detect the language of the image using Tesseract's image_to_osd method
def detect_language(image: str) -> str:
    try:
        osd = pytesseract.image_to_osd(image)
        lang = osd.split("Script: ")[1].split("\n")[0]
        return lang
    except Exception as e:
        logging.warning(f"Sprache konnte nicht erkannt werden für {image}: {e}")
        return "eng"

#start the script and load the images
def main():
    parser = argparse.ArgumentParser(description="OCR für Bilder in einem Verzeichnis.")
    parser.add_argument('--input_dir', required=True, help='Verzeichnis mit Eingabebildern')
    parser.add_argument('--output_dir', required=True, help='Verzeichnis für Ausgabedateien')
    parser.add_argument('--export_format', default='txt', help='Exportformat (Standard: txt)')
    parser.add_argument('--loglevel', default='INFO', help='Logging-Level (DEBUG, INFO, WARNING, ERROR)')
    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel.upper(), format='%(asctime)s %(levelname)s: %(message)s')

    if not os.path.isdir(args.input_dir):
        logging.error(f"Eingabeverzeichnis nicht gefunden: {args.input_dir}")
        return
    if not os.path.isdir(args.output_dir):
        try:
            os.makedirs(args.output_dir)
            logging.info(f"Ausgabeverzeichnis erstellt: {args.output_dir}")
        except Exception as e:
            logging.error(f"Konnte Ausgabeverzeichnis nicht erstellen: {e}")
            return

    images = find_images(args.input_dir)
    if not images:
        logging.warning(f"Keine Bilder im Verzeichnis {args.input_dir} gefunden.")
        return

    for image_path in images:
        try:
            text = ocr_image(image_path)
            base = os.path.splitext(os.path.basename(image_path))[0]
            out_file = os.path.join(args.output_dir, f"{base}.{args.export_format}")
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(text)
            logging.info(f"Ergebnis gespeichert: {out_file}")
        except Exception as e:
            logging.error(f"Fehler bei der Verarbeitung von {image_path}: {e}")

if __name__ == "__main__":
    main()
