import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# El propósito de este programa es corroborar que exite una relación lineal entre la posesión y el número de pases.
# Si esto se verifica, los valores de los pases faltantes se imputarán basándose en esta relación lineal.

# Cargar el archivo CSV
data = pd.read_csv('C:/Users/hecho/OneDrive/Escritorio/Snitch-IA/BBDD Ligas/Segunda/22-23/partidos22-23-rellenado.csv')

df = pd.DataFrame(data)

# Eliminar las filas donde falten datos
df = df.dropna(subset=['Posesion Local', 'Pases Local', 'Posesion Visit', 'Pases Visit'])

# Crear dos gráficos de dispersión: uno para local y otro para visitante
plt.figure(figsize=(12, 6))

# Gráfico de dispersión para el equipo local
plt.subplot(1, 2, 1)  # 1 fila, 2 columnas, 1ª posición
plt.scatter(df['Posesion Local'], df['Pases Local'], color='blue')

# Cálculo de la regresión lineal para el equipo local
m_local, b_local = np.polyfit(df['Posesion Local'], df['Pases Local'], 1)
plt.plot(df['Posesion Local'], m_local * df['Posesion Local'] + b_local, color='red', linestyle='--', label='Regresión Lineal Local')

plt.title('Equipo Local: Posesión vs Pases')
plt.xlabel('Posesión (%)')
plt.ylabel('Pases')
# plt.legend()

# Gráfico de dispersión para el equipo visitante
plt.subplot(1, 2, 2)  # 1 fila, 2 columnas, 2ª posición
plt.scatter(df['Posesion Visit'], df['Pases Visit'], color='blue')

# Cálculo de la regresión lineal para el equipo visitante
m_visit, b_visit = np.polyfit(df['Posesion Visit'], df['Pases Visit'], 1)
plt.plot(df['Posesion Visit'], m_visit * df['Posesion Visit'] + b_visit, color='red', linestyle='--', label='Regresión Lineal Visitante')

plt.title('Equipo Visitante: Posesión vs Pases')
plt.xlabel('Posesión (%)')
plt.ylabel('Pases')
# plt.legend()

# Mostrar la gráfica
plt.show()
