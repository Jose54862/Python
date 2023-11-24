from pytube import YouTube
from sys import argv

# Obtener el enlace del video de la línea de comandos
link = argv[1]

# Crear una instancia de la clase YouTube con el enlace
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

# Obtener la mejor resolución del video
yd = yt.streams.get_highest_resolution()

# Descargar el video en la carpeta especificada
# Utiliza barras inclinadas hacia adelante o una cadena cruda (r"") para la ruta
download_path = r"C:/Users/wuxio/OneDrive/桌面/Python/Videos"
yd.download(download_path)
