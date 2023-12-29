
import pandas as pd
import re  # Import the regex module
import unicodedata
# Texto crudo proporcionado por el usuario.
raw_text = """
Desde Hasta Duración Fase Código Resúmen Operativo 
06:00 06:15 0,25 I2-CEME CEMENT Compañía Halliburton termina cementación etapa Intermedia 2:Desplaza con 328 bbl. Despresuriza, observando cierre de elementos.
06:15 06:45 0,50 I2-CABEZCABEZA Realiza BU test, no levanta presión. Realiza flow check, observa pozo estático.
06:45 07:30 0,75 I2-CABEZDCEMENT Desmonta cabeza de cementación y líneas.
07:30 08:00 0,50 I2-CABEZCSGMANIORetira casing de maniobra, levanta csg con crossover y limpia bodega con Vactor.
08:00 08:15 0,25 I2-CABEZRNON Realiza charla de seguridad con personal del turno entrante.
08:15 09:00 0,75 I2-CABEZCABEZA Profundiza lavador, lava alojamiento del empaquetador.
09:00 12:30 3,50 I2-CABEZCABEZA Arma empaquetador y bajante. Profundiza el mismo.Realiza PH de sellos inferior con P 7500 psi, sellos intermedio con P 10000 psi.Libera snapring y realiza prueba de tensión con 10 klb ok, coloca tpn de 11" y prueba sellos superiores con 10 M psi okObservaciones: realizando prueba de liberación de snapring observa desenrosque de crossover, levanta y torquea nuevamente, profundiza y finaliza operación ok.
12:30 14:00 1,50 I2-CABEZDENTUB Personal de Cía Nabors desmonta CRT y elementos de entubación
14:00 16:00 2,00 I2-CABEZDOBLEPIN Cambia doble pin NC 50 x XT39
16:00 18:00 2,00 I2-CABEZRAMBOP Cambia RAM parcial superior 7" x Variable y pba con 350 y 8800 psi
18:00 18:30 0,50 I2-CABEZMANEQU Realiza mantenimiento preventivo al TDS
18:30 19:15 0,75 I2-CABEZMWB Retira tapón de tapón de prueba e instala wear bushing.
19:15 20:15 1,00 I2-CABEZACOND Lava piso de trabajo.
20:15 20:30 0,25 P-ARMA RNON Realiza reunión de seguridad y operativa previo a armar BHA direccional.
20:30 23:00 2,50 P-ARMA ARMA Compañía SLB arma BHA direccional,, vortex.
23:00 23:15 0,25 P-ARMA BAJA Baja 1 tiro hwdp 4". Mientras desconecta observa pérdida de aceite en grabber. 23:15 01:15 2,00 P-ARMA BAJA Retira grabber. 01:15 03:00 1,75 P-ARMA BAJA Baja herramienta hasta 456 m. Llena interior de acuerdo a procedimiento RSS.
03:00 03:30 0,50 P-ARMA PBHA Cia SLB prueba conjunto RSS.* Bombea lodo base a 1730 gr/lt.* Q: 220 gpm - PRES: 2514 psi
03:30 05:00 1,50 P-ARMA BAJA Continua bajando herramienta desde 456 m hasta 1016 m. Llena interior de acuerdo a procedimiento RSS.
05:00 06:00 1,00 P-ARMA BAJA Cambia grabber en curso
"""

# Patrones para las columnas
patron_fila = re.compile(r'(\d{2}:\d{2})\s(\d{2}:\d{2})\s([\d,]+)\s(\S+)\s(\S+)\s(.+?)(?=\s\d{2}:\d{2}|\Z)', re.DOTALL)

# Encontramos todas las coincidencias del patrón en el texto
matches = patron_fila.findall(raw_text)

# Creamos un DataFrame con las coincidencias
df = pd.DataFrame(matches, columns=['Desde', 'Hasta', 'Duración', 'Fase', 'Código', 'Resumen Operativo'])

# Convertimos las comas en puntos en la columna 'Duración'
df['Duración'] = df['Duración'].str.replace(',', '.')

# Normalizamos los caracteres
df['Resumen Operativo'] = df['Resumen Operativo'].apply(
    lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('ascii')
)

# Exportamos el DataFrame a un archivo CSV, añadiendo los datos al final del archivo existente
csv_path = 'operativo.csv'
df.to_csv(csv_path, mode='a', index=False, sep=';', encoding='utf-8-sig', header=False)

print(f"Los datos han sido añadidos al archivo CSV existente: {csv_path}")