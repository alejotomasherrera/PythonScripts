import os

# Define la ruta de la carpeta donde están los archivos
ruta_carpeta = 'Partes Diarios'

# Obtén la lista de archivos en la carpeta
archivos = os.listdir(ruta_carpeta)

# Ordena la lista de archivos si es necesario (opcional)
# archivos.sort()

# Inicia un contador para los nombres de los archivos
contador = 1

for archivo in archivos:
    # Define la nueva ruta del archivo con el nuevo nombre
    nuevo_nombre = os.path.join(ruta_carpeta, str(contador))

    # Obtiene la extensión del archivo original (si es necesario)
    extension = os.path.splitext(archivo)[1]
    nuevo_nombre += extension

    # Renombra el archivo
    os.rename(os.path.join(ruta_carpeta, archivo), nuevo_nombre)

    # Incrementa el contador
    contador += 1
