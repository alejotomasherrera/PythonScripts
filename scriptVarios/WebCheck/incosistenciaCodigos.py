import pandas as pd

# Lee los dos archivos CSV con el delimitador correcto
archivo_sistema_interno = pd.read_csv('stock_update.csv', delimiter=';')
archivo_wordpress = pd.read_csv('archivo_wordpress.csv')

# Inicializa una lista para almacenar los SKU y nombres distintos de WordPress
sku_distintos_wordpress = []

# Itera sobre cada SKU del archivo de WordPress
for index, row in archivo_wordpress.iterrows():
    sku_wordpress = row['SKU']

    # Verifica si el SKU de WordPress no está en el sistema interno
    if sku_wordpress not in archivo_sistema_interno['SKU'].values:
        # Agrega el SKU y nombre a la lista
        sku_distintos_wordpress.append({'SKU': sku_wordpress, 'Nombre': row['Nombre']})

# Crea un DataFrame a partir de la lista de SKU y nombres distintos de WordPress
nuevo_archivo = pd.DataFrame(sku_distintos_wordpress)

# Guarda el nuevo archivo CSV con los SKU y nombres distintos de WordPress
nuevo_archivo.to_csv('sku_distintos_wordpress.csv', index=False)

print("SKU distintos de WordPress guardados en 'sku_distintos_wordpress.csv'")
