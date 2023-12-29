import pandas as pd

# Ruta del archivo Excel
file_path = '09-2023.xlsx'

# Leer el archivo Excel
df = pd.read_excel(file_path)

# Filtrar las descripciones en débitos que no contienen las cadenas "Transf" ni "Trf"
debit_filtered_df = df[~df['Descripción'].str.contains("Transf|Trf", na=False, regex=True)]

# Agrupar por 'Descripción' y sumar 'Débitos' junto con la primera fecha
grouped_debit = debit_filtered_df.groupby('Descripción').agg({'Fecha': 'first', 'Débitos': 'sum'}).reset_index()

# Reordenar las columnas para que 'Fecha' sea la primera
grouped_debit = grouped_debit[['Fecha', 'Descripción', 'Débitos']]

# Filtrar las descripciones en créditos que no contienen las cadenas "Transf" ni "Trf" y tienen un valor mayor a 0
credit_filtered_df = df[(~df['Descripción'].str.contains("Transf|Trf", na=False, regex=True)) & (df['Créditos'] > 0)]

# Agrupar por 'Descripción' y sumar 'Créditos' junto con la primera fecha
grouped_credit = credit_filtered_df.groupby('Descripción').agg({'Fecha': 'first', 'Créditos': 'sum'}).reset_index()

# Reordenar las columnas para que 'Fecha' sea la primera
grouped_credit = grouped_credit[['Fecha', 'Descripción', 'Créditos']]

# Ruta del archivo de salida
output_file_path = 'resultados_agrupados_fecha_primera_columna.xlsx'

# Utilizar un bloque with para manejar el escritor de Excel
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    # Exportar los datos filtrados y agrupados (débitos) a una hoja
    grouped_debit.to_excel(writer, sheet_name='Débitos Filtrados', index=False)

    # Exportar los datos de crédito filtrados y agrupados a otra hoja
    grouped_credit.to_excel(writer, sheet_name='Créditos', index=False)

print(f"Archivo exportado correctamente en: {output_file_path}")
