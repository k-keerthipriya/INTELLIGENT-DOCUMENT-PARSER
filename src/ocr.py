import pytesseract
from pytesseract import Output
import cv2

def run_ocr(image_path: str):
    img = cv2.imread(image_path)
    data = pytesseract.image_to_data(img, output_type=Output.DICT)

    words = []
    boxes = []

    for i in range(len(data['text'])):
        if data['text'][i].strip() == "":
            continue

        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        words.append(data['text'][i])
        boxes.append([x, y, x + w, y + h])

    return words, boxes, img
