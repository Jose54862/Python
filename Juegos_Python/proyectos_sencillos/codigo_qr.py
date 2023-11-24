import qrcode
from PIL import Image

data = "No te lo pierdas."

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Invertir los colores: blanco a negro y negro a blanco
img = img.convert("RGBA")
data = img.getdata()
new_data = [(255, 255, 255, 255) if item[0] == 0 else (0, 0, 0, 255) for item in data]
img.putdata(new_data)

# Ruta de archivo válida en formato Windows
img.save("C:\\Users\\wuxio\\OneDrive\\文档\\QR_Code\\random.png")
