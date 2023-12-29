import os
import csv
import qrcode

# Directorio de salida dentro del proyecto de Python
directorio_proyecto = os.path.dirname(os.path.realpath(__file__))
ruta_pdfs_merge = os.path.join(directorio_proyecto, 'pdfsreducidos')
ruta_imagenes_qr = os.path.join(directorio_proyecto, 'imagenes_qr/totem4qrs')

# Crear el directorio de salida para las imágenes QR si no existe
os.makedirs(ruta_imagenes_qr, exist_ok=True)

# Archivo CSV de entrada
archivo_csv_path = os.path.join(directorio_proyecto, 'csv-generators/csvGenerator-totem4.csv')

# Leer el archivo CSV
with open(archivo_csv_path, mode='r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)

    # Iterar sobre las filas del CSV
    for fila in lector_csv:
        # Obtener la URL y el título del QR
        url = fila['URL']
        qr_title = fila['QR Code Title (for reference)']

        # Reemplazar espacios en blanco con %20
        qr_title = qr_title.replace(' ', '%20')

        # Crear el objeto QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Crear la imagen QR
        img_qr = qr.make_image(fill_color="black", back_color="white")

        # Verificar si el archivo ya existe antes de guardarlo
        ruta_imagen_qr = os.path.join(ruta_imagenes_qr, f'{qr_title}.png')
        if os.path.exists(ruta_imagen_qr):
            print(f'El QR para {qr_title} ya existe en la carpeta: {ruta_imagen_qr}')
        else:
            img_qr.save(ruta_imagen_qr)
            print(f'QR generado para {qr_title}: {ruta_imagen_qr}')

print(f'Todas las imágenes QR fueron generadas en la carpeta ' + ruta_imagenes_qr)
