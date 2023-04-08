import pyqrcode
import png
link = "https://www.linkedin.com/in/gaurav-saini-8a9209238/"
qr_code = pyqrcode.create(link)
qr_code.png("linkedin.png", scale=5)