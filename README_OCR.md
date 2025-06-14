# SimpleOCR

A simple OCR script using Tesseract, with command-line interface, error handling, and logging.

## Usage

```bash
python ocr.py --input_dir <input_directory> --output_dir <output_directory> [--export_format txt]
```

- `--input_dir`: Verzeichnis mit den zu verarbeitenden Bildern (PNG/JPG).
- `--output_dir`: Zielverzeichnis für die Textergebnisse.
- `--export_format`: (Optional) Exportformat, Standard: `txt`.

## Voraussetzungen
- Python 3.7+
- Tesseract-OCR installiert und im PATH
- Python-Pakete: matplotlib, pytesseract

Installieren Sie die Abhängigkeiten mit:

```bash
pip install -r requirements.txt
```

## Beispiel

```bash
python ocr.py --input_dir ./ --output_dir ./results
```

## Tests ausführen

Um die Tests auszuführen, stellen Sie sicher, dass pytest installiert ist:

```bash
pip install pytest
```

Führen Sie dann die Tests mit folgendem Befehl aus:

```bash
pytest test_simpleocr.py
```

Die Tests prüfen die Kernfunktionen `find_images`, `ocr_image` und `evaluate_image` auf gültige und ungültige Eingaben.

## Lizenz
MIT License
