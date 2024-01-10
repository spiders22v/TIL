import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지 불러오기
image = Image.open(r'32.이미지에서 글자추출하기\img.png')

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(image, lang='kor')

# 추출된 텍스트 출력
print(text)
