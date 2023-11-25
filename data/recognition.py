import pytesseract
from PIL import Image
from data.enums import RecognitionMode

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_text(file_name:str, mode:RecognitionMode=RecognitionMode.Number) -> str:
    match mode:
        case RecognitionMode.Number:
            config = f'--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
        case RecognitionMode.All:
            config = None
    ocr_result = pytesseract.image_to_string(Image.open(file_name), config=config)
    return ocr_result