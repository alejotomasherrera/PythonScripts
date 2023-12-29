import os
from PyPDF2 import PdfWriter, PdfReader

# Ruta de la carpeta que contiene las carpetas de productos
ruta_base = 'Pdfs/craftsman'

# Directorio de salida dentro del proyecto de Python
directorio_proyecto = os.path.dirname(os.path.realpath(__file__))
ruta_salida = os.path.join(directorio_proyecto, 'pdfsmerges/craftsman_mergepdfsautomate')

# Crear el directorio de salida si no existe
os.makedirs(ruta_salida, exist_ok=True)

# Iterar sobre cada carpeta de productos
for nombre_producto in os.listdir(ruta_base):
    carpeta_producto = os.path.join(ruta_base, nombre_producto)

    # Verificar si la ruta es una carpeta
    if os.path.isdir(carpeta_producto):
        # Obtener la lista de archivos en la carpeta
        archivos_en_carpeta = os.listdir(carpeta_producto)

        # Ordenar los archivos para que los que contienen "ficha" estén primero
        archivos_ordenados = sorted(archivos_en_carpeta, key=lambda x: "ficha" not in x.lower())

        # Crear un objeto PdfWriter para combinar PDFs
        pdf_writer = PdfWriter()

        # Iterar sobre los archivos PDF en la carpeta del producto
        for archivo in archivos_ordenados:
            ruta_archivo = os.path.join(carpeta_producto, archivo)

            # Verificar si el archivo es un PDF
            if archivo.lower().endswith('.pdf'):
                # Abrir el PDF y agregar sus páginas al objeto PdfWriter
                with open(ruta_archivo, 'rb') as pdf_file:
                    pdf_reader = PdfReader(pdf_file)
                    for pagina in pdf_reader.pages:
                        pdf_writer.add_page(pagina)

        # Ruta para guardar el PDF combinado en la carpeta "pdfsmerge"
        pdf_combinado = os.path.join(ruta_salida, f'{nombre_producto}.pdf')

        # Guardar el PDF combinado
        with open(pdf_combinado, 'wb') as pdf_salida:
            pdf_writer.write(pdf_salida)

        print(f'PDF combinado para {nombre_producto}: {pdf_combinado}')

print(f'Todos los PDFs combinados fueron guardados en la carpeta {ruta_salida}')
