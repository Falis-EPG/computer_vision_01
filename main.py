# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YbHFadtSKjCuWr0wA9YKYvPpV9PPEwOW
"""

import pytesseract
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import os

img = cv2.imread('/content/text-recognize/Imagens/Aula1-teste.png')
cv2_imshow(img)

texto = pytesseract.image_to_string(img)
print(texto)

img = cv2.imread('/content/text-recognize/Imagens/Aula1-ocr.png')
cv2_imshow(img)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2_imshow(rgb)

texto = pytesseract.image_to_string(rgb)
print(texto)

img = cv2.imread('/content/text-recognize/Imagens/Aula2-undersampling.png')
texto = pytesseract.image_to_string(img)
print(texto)

texto = pytesseract.image_to_string(img, lang='por')
print(texto)

img = cv2.imread('/content/text-recognize/Imagens/Aula2-trecho-livro.png')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2_imshow(rgb)

os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata'
texto = pytesseract.image_to_string(rgb, lang='por')
print(texto)

from PIL import Image
import matplotlib.pyplot as plt
from pytesseract import Output

img = Image.open('/content/text-recognize/Imagens/Aula2-livro.png')
plt.imshow(img);

print(pytesseract.image_to_osd(img))

img = cv2.imread('/content/text-recognize/Imagens/Aula3-testando.png')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2_imshow(rgb)

resultado = pytesseract.image_to_data(rgb, lang='por', output_type=Output.DICT)
resultado

min_conf = 40 #@param {type: 'slider', min: 0, max:100}

img_copia = rgb.copy()

def caixa_texto(resultado, img, cor=(255, 100, 0)):
  x = resultado['left'][i]
  y = resultado['top'][i]
  w = resultado['width'][i]
  h = resultado['height'][i]
  cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)

  return x, y, img

for i in range(len(resultado['text'])):
  confiaca = int(resultado['conf'][i])
  if confiaca > min_conf:
    x, y, img = caixa_texto(resultado, img_copia)
    texto = resultado['text'][i]
    cv2.putText(img_copia, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)

cv2_imshow(img_copia)

caixa_texto(resultado, rgb)