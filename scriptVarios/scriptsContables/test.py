import pandas as pd

# Ruta del archivo Excel
file_path = '09-2023.xlsx'

# Leer el archivo Excel
df = pd.read_excel(file_path)

# Mostrar los nombres de las columnas para verificar
print("Nombres de las columnas en el archivo:", df.columns.tolist())
