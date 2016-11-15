"""
create qr-code image
"""

import qrcode
from PIL import Image

def make_img(text):
    return qrcode.make(text)