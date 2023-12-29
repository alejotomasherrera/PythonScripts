import pandas as pd

# Lee los dos archivos CSV con el delimitador correcto
archivo_sistema_interno = pd.read_csv('stock_update.csv', delimiter=';')
archivo_wordpress = pd.read_csv('archivo_wordpress.csv')

# Encuentra los SKU que están en stock_update pero no en WordPress
sku_faltantes_en_wordpress = archivo_sistema_interno[~archivo_sistema_interno['SKU'].isin(archivo_wordpress['SKU'])]

# Guarda el nuevo archivo CSV con los SKU faltantes en WordPress
# Usa una ruta completa donde tengas permisos de escritura
sku_faltantes_en_wordpress.to_csv(r'sku_faltantes_en_wordpress.csv', index=False)

print("SKU faltantes en WordPress guardados en 'sku_faltantes_en_wordpress.csv'")
