# neural-ocr

This is the repository for the AI project for the Applied Data Science Master's program.

Collaborators:  Amed B. Martin
                Orfeas Kalipolitis


Example usage:
    python scraper.py - to download fonts from 1001fonts
    python ocrV1.py --help
        to get some help about the potential arguments
    python ocrV1.py --east frozen_east_text_detection.pb \
            --image path/to/image --padding 0.05 --lang grc --psm 8
        to use the frozen_east_text_detection model for left to write text detection
        on the image on path/to/image using a padding of 0.05
        detecting ancient greek as the language
        and assuming each part found by the model contains a single word

Dependencies:
    Python3: bs4, wget, opencv-python, pytesseract, tesseract
    System: tesseract



