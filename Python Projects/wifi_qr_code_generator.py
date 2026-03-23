# The dependencies to install is pip install wifi_qrcode_generator.


import wifi_qrcode_generator.generator
from PIL import Image

ssid = "Tech P"
password = "thevalueofpiis3.14"
security = "WPA"

from wifi_qr_code_generator.generator import wifi_qrcode
qr = wifi_qrcode(ssid, False, security, password)

qr.make_image().save("wifi_qr.png")
Image.open("wifi_qr.png")