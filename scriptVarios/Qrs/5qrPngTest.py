import os
import requests
from PIL import Image
from pyzbar.pyzbar import decode

# Directorio que contiene los archivos PNG con los códigos QR
directorio_qrs = 'imagenes_qr/totem3qrs'

# Función para obtener el enlace a partir de un código QR en una imagen
def obtener_enlace_desde_qr(ruta_imagen):
    try:
        # Decodificar el código QR
        resultado = decode(Image.open(ruta_imagen))

        # Obtener el enlace desde el resultado
        enlace = resultado[0].data.decode('utf-8')
        return enlace
    except Exception as e:
        print(f"Error al procesar el código QR en {ruta_imagen}: {e}")
        return None

# Función para probar si un enlace devuelve un código de estado 404
def probar_enlace(enlace):
    try:
        response = requests.head(enlace)
        return response.status_code == 404
    except requests.RequestException:
        return True  # Si hay un error de conexión, consideramos que el enlace está roto

cant = 0

# Iterar sobre archivos en el directorio de códigos QR
for nombre_archivo in os.listdir(directorio_qrs):
    ruta_qr = os.path.join(directorio_qrs, nombre_archivo)

    # Verificar si el archivo es un PNG
    if nombre_archivo.lower().endswith('.png'):
        # Obtener el enlace del código QR
        enlace_qr = obtener_enlace_desde_qr(ruta_qr)

        if enlace_qr:
            # Probar el enlace y mostrar el resultado
            if probar_enlace(enlace_qr):
                print(f"Error 404 para el enlace en {ruta_qr}: {enlace_qr}")
            else:
                print(f"Enlace válido para el código QR en {ruta_qr}: {enlace_qr}")
                cant += 1

print("Cantidad de registros validados: ", cant)