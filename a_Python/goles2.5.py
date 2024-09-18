import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('C:/Users/hecho/OneDrive/Escritorio/Snitch-IA\BBDD Ligas/Segunda/23-24/goles2.5.csv')

# Calcular el total de goles
df['Total goles'] = df['GolesLocal'] + df['GolesVisit']

# Aplicar el One-Hot Encoding (1 para más de 2.5 goles, 0 para menos o igual a 2.5 goles)
df['OneHotEncoding'] = df['Total goles'].apply(lambda x: 1 if x > 2.5 else 0)

# Guardar el DataFrame con las nuevas columnas en un nuevo archivo CSV
df.to_csv('C:/Users/hecho/OneDrive/Escritorio/Snitch-IA/BBDD Ligas/Segunda/23-24/resultado_goles2.5.csv', index=False)

# Calcular el porcentaje de partidos con más de 2.5 goles
total_partidos = len(df) # Suma todas las filas
partidos_mas_2_5_goles = df['OneHotEncoding'].sum() # Suma todos los valores 1 de la columna 'OneHotEncoding'
porcentaje_mas_2_5_goles = (partidos_mas_2_5_goles / total_partidos) * 100

print(f"El porcentaje de partidos con más de 2.5 goles es: {porcentaje_mas_2_5_goles:.2f}%")
