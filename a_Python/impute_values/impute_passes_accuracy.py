# Tras imputar el número de pases, imputamos la precisión de pases con un árbol de decisión
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Leer el archivo
df = pd.read_csv('C:/Users/hecho/OneDrive/Escritorio/Snitch-IA/BBDD Ligas/Segunda/23-24/partidos23-24-imputado-pases.csv')

# Filas con datos complets
df_complete = df.dropna(subset=['Precision de pases Local', 'Precision de pases Visit'])

# Filas con datos que faltan
df_missing = df[(df['Precision de pases Local'].isnull()) | (df['Precision de pases Visit'].isnull())]

# Definir características
features = ['GolesLocal', 'Tiros Local', 'Tiros a puerta Local', 'Posesion Local', 'Pases Local', 'Faltas Local', 'Tarjetas amarillas Local', 'Tarjetas rojas Local', 'Fueras de juego Local', 'Saques de esquina Local','GolesVisit', 'Tiros Visit', 'Tiros a puerta Visit', 'Posesion Visit', 'Pases Visit', 'Faltas Visit', 'Tarjetas amarillas Visit', 'Tarjetas rojas Visit', 'Fueras de juego Visit', 'Saques de esquina Visit']

# Características de entrenamiento con los datos completos
X_train = df_complete[features]
# Características con los datos que faltan
X_missing = df_missing[features]

# Variables objetivo con los datos completos
y_train_local = df_complete['Precision de pases Local']
y_train_visit = df_complete['Precision de pases Visit']

# Crear los modelos
model_local = DecisionTreeRegressor(random_state=42)
model_visit = DecisionTreeRegressor(random_state=42)

# Entrenar los modelos
model_local.fit(X_train, y_train_local)
model_visit.fit(X_train, y_train_visit)

# Hacer predicciones
pred_local = model_local.predict(X_missing)
pred_visit = model_visit.predict(X_missing)

# Convertir predicciones en Series para asegurar la alineación con el índice
predict_local_series = pd.Series(pred_local, index=df_missing.index)
predict_visit_series = pd.Series(pred_visit, index=df_missing.index)

# Imputar los valores faltantes para ambos objetivos
df.loc[df['Precision de pases Local'].isnull(), 'Precision de pases Local'] = predict_local_series
df.loc[df['Precision de pases Visit'].isnull(), 'Precision de pases Visit'] = predict_visit_series

# Combinar los datos completos y los imputados
df_imputed = df.copy()

# Redondear a dos decimales el resultado de la imputación
df_imputed['Precision de pases Local'] = df_imputed['Precision de pases Local'].round(2)
df_imputed['Precision de pases Visit'] = df_imputed['Precision de pases Visit'].round(2)

# Crear archivo csv resultado
df_imputed.to_csv('C:/Users/hecho/OneDrive/Escritorio/Snitch-IA/BBDD Ligas/Segunda/23-24/partidos23-24-imputado-prec-pases.csv', index=False)

# Histogramas de los valores completos e imputados
plt.figure(figsize=(14,8))

# Histograma equipo local
# Valores completos
plt.subplot(2, 2, 1)
plt.hist(df_complete['Precision de pases Local'], bins=20, color='blue', alpha=0.7)
plt.title('Distribución de valores completos Local')

# Valores imputados
plt.subplot(2, 2, 2)
plt.hist(df_imputed['Precision de pases Local'], bins=20, color='green', alpha=0.7)
plt.title('Distribución de valores imputados Local')

# Histograma equipo visitante
# Valores completos
plt.subplot(2, 2, 3)
plt.hist(df_complete['Precision de pases Visit'], bins=20, color='blue', alpha=0.7)
plt.title('Distribución de valores completos Visitante')

# Valores imputados
plt.subplot(2, 2, 4)
plt.hist(df_imputed['Precision de pases Visit'], bins=20, color='green', alpha=0.7)
plt.title('Distribución de valores imputados Visitante')

plt.show()