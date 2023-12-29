import csv
import requests

# Archivo CSV de entrada
archivo_csv_path = 'csv-generators/csvGenerator-totem4.csv'
cant = 0
# Leer el archivo CSV
with open(archivo_csv_path, mode='r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    # Iterar sobre las filas del CSV
    for fila in lector_csv:
        # Obtener la URL de la primer columna
        url = fila[0]

        # Verificar el enlace
        try:
            respuesta = requests.head(url, timeout=10)
            if respuesta.status_code == 404:
                print(f'Error 404 para URL: {url}')
            else:
                print(f'Enlace válido: {url}')
                cant += 1
        except requests.RequestException as e:
            print(f'Error al verificar el enlace {url}: {str(e)}')

print("La cantidad de registros validos son:", cant)