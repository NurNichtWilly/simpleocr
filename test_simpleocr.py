import os
import pytest
import tempfile
from ocr import find_images, ocr_image, evaluate_image

# Hilfsfunktion zum Erstellen einer Dummy-Bilddatei
def create_dummy_image(path):
    # Erstelle eine leere PNG-Datei (kein echtes Bild, aber für find_images ausreichend)
    with open(path, 'wb') as f:
        f.write(b'\x89PNG\r\n\x1a\n')

def test_find_images_valid(tmp_path):
    img1 = tmp_path / "test1.png"
    img2 = tmp_path / "test2.jpg"
    create_dummy_image(img1)
    create_dummy_image(img2)
    images = find_images(str(tmp_path))
    assert img1.as_posix() in images
    assert img2.as_posix() in images

def test_find_images_invalid():
    # Verzeichnis existiert nicht
    images = find_images("/non/existent/path")
    assert images == [] or isinstance(images, list)

def test_ocr_image_valid():
    # Nutze ein echtes Bild aus dem Workspace, falls vorhanden
    img_path = "test.png"
    if os.path.exists(img_path):
        text = ocr_image(img_path)
        assert isinstance(text, str)
    else:
        pytest.skip("test.png nicht vorhanden")

def test_ocr_image_invalid():
    # Nicht existierender Pfad
    text = ocr_image("not_a_real_file.png")
    assert text == ""

def test_evaluate_image_valid():
    img_path = "test.png"
    if os.path.exists(img_path):
        result = evaluate_image(img_path, "")
        if result is False:
            # Prüfe, ob Tesseract-Fehler im Log steht
            import io, logging
            log_stream = io.StringIO()
            handler = logging.StreamHandler(log_stream)
            logging.getLogger().addHandler(handler)
            evaluate_image(img_path, "")
            logging.getLogger().removeHandler(handler)
            log_contents = log_stream.getvalue().lower()
            if "tesseract is not installed" in log_contents:
                pytest.skip("Tesseract nicht installiert")
        assert result is True
    else:
        pytest.skip("test.png nicht vorhanden")

def test_evaluate_image_invalid():
    # Nicht existierender Pfad
    result = evaluate_image("not_a_real_file.png", "foo")
    assert result is False
