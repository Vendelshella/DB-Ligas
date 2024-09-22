import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Leer el archivo CSV
df = pd.read_csv('C:/Users/hecho/OneDrive/Escritorio/Snitch-IA/BBDD Ligas/Segunda/23-24/partidos23-24-rellenado.csv')

# Filtrar los datos con valores completos para entrenamiento
train_data_local = df.dropna(subset=['Pases Local'])
train_data_visit = df.dropna(subset=['Pases Visit'])

# Separar características y etiquetas para 'Pases Local'
X_train_local = train_data_local[['Posesion Local']]
y_train_local = train_data_local['Pases Local']

# Separar características y etiquetas para 'Pases Visit'
X_train_visit = train_data_visit[['Posesion Visit']]
y_train_visit = train_data_visit['Pases Visit']

# Dividir los datos en conjuntos de entrenamiento y prueba para evaluación
X_train_local_split, X_test_local_split, y_train_local_split, y_test_local_split = train_test_split(X_train_local, y_train_local, test_size=0.2, random_state=42)
X_train_visit_split, X_test_visit_split, y_train_visit_split, y_test_visit_split = train_test_split(X_train_visit, y_train_visit, test_size=0.2, random_state=42)

# Entrenar los modelos de regresión lineal
reg_local = LinearRegression()
reg_local.fit(X_train_local_split, y_train_local_split)

reg_visit = LinearRegression()
reg_visit.fit(X_train_visit_split, y_train_visit_split)

# Hacer predicciones en el conjunto de prueba
y_pred_local = reg_local.predict(X_test_local_split)
y_pred_visit = reg_visit.predict(X_test_visit_split)

# Calcular R² para 'Pases Local'
r2_local = r2_score(y_test_local_split, y_pred_local)

# Calcular R² para 'Pases Visit'
r2_visit = r2_score(y_test_visit_split, y_pred_visit)

print(f"Coeficiente de Determinación (R²) para 'Pases Local': {r2_local}")
print(f"Coeficiente de Determinación (R²) para 'Pases Visit': {r2_visit}")

'''
El R² es una métrica que indica la proporción de la varianza en la variable dependiente (número de pases) que es explicada por la variable independiente (posesión).
Un R² cercano a 1 indica un buen ajuste.
Análisis del resultado: Los valores alrededor de 0.7 a 0.8 sugieren que el modelo es bastante bueno pero no perfecto.
'''

# Filtrar datos faltantes para cada columna por separado
missing_data_local = df[df['Pases Local'].isna()] # Contiene las filas del DataFrame original df donde faltan valores en la columna 'Pases Local'.
missing_data_visit = df[df['Pases Visit'].isna()]

# Predecir valores faltantes para 'Pases Local' basados en la posesión local
X_missing_local = missing_data_local[['Posesion Local']] # Contiene únicamente la columna 'Posesion Local' del DataFrame missing_data_local.
df.loc[missing_data_local.index, 'Pases Local'] = reg_local.predict(X_missing_local).round().astype(int) # Sintaxis: df.loc[fila, columna]

# Predecir valores faltantes para 'Pases Visit' basados en la posesión visitante
X_missing_visit = missing_data_visit[['Posesion Visit']]
df.loc[missing_data_visit.index, 'Pases Visit'] = reg_visit.predict(X_missing_visit).round().astype(int)

# Guardar el archivo CSV con los valores completados
df.to_csv("C:/Users/hecho/OneDrive/Escritorio/Snitch-IA/BBDD Ligas/Segunda/23-24/partidos23-24-imputado-pases.csv", index=False)

print("Valores faltantes completados con regresión lineal y redondeados a enteros.")
