import os
import csv
from urllib.parse import quote

# Directorio de salida dentro del proyecto de Python
directorio_proyecto = os.path.dirname(os.path.realpath(__file__))
ruta_pdfs_merge = os.path.join(directorio_proyecto, 'pdfsreducidos')

# Archivo CSV de salida
archivo_csv_path = os.path.join(directorio_proyecto, 'csv-generators/csvGenerator-totem4.csv')

# Lista para almacenar las filas del CSV
filas_csv = []

# URL base
url_base = 'http://siglo21myh.com/resources/images/pdfsqrs/totem4/'

# Iterar sobre cada archivo en la carpeta
for nombre_archivo in os.listdir(ruta_pdfs_merge):
    # Verificar si el archivo es un PDF
    if nombre_archivo.lower().endswith('.pdf'):
        # Construir la URL codificando el nombre del archivo
        url = f'{url_base}{quote(nombre_archivo)}'

        # Agregar la fila al CSV
        filas_csv.append([url, nombre_archivo])

# Escribir al archivo CSV
with open(archivo_csv_path, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    # Escribir la cabecera
    escritor_csv.writerow(['URL', 'QR Code Title (for reference)'])

    # Escribir las filas
    escritor_csv.writerows(filas_csv)

print(f'Archivo CSV creado con éxito: {archivo_csv_path}')
