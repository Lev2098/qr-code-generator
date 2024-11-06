import qrcode
from PIL import Image

# URL для якого треба створити QR-код
url = "example.com"

# Створення QR-коду
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Створення зображення QR-коду
img = qr.make_image(fill='black', back_color='white')

# Збереження зображення
img.save("qrcode.png")

# Відкриття зображення для перегляду
img.show()
