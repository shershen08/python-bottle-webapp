"""
create qr-code image
"""

import qrcode
from PIL import Image

import base64
from io import BytesIO
buffer = BytesIO()

def make_img(text):
    img = qrcode.make(text)
    img.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue())
    return img_str