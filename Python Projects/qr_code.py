# Generate a QR code using the qrcode library
# Dependencies to install: 'pip install qrcode'


import qrcode
from PIL import Image

data = "https://www.facebook.com/share/p/1DV1DC1Lht/"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)
image = qr.make_image(fill = 'black', back_color = 'white')

image.save("qrcode.png")
image.open("qrcode.png")