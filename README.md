# Base de Datos de Ligas de Fútbol Españolas

## Descripción

Esta base de datos contiene información sobre las ligas de fútbol españolas de Primera y Segunda División. Está diseñada para proporcionar datos históricos y actuales que se utilizarán para entrenar una inteligencia artificial que prediga resultados de partidos.

## Estructura de la Base de Datos

La base de datos está organizada en las siguientes tablas:

- **Jugadores**: Información sobre los jugadores de los equipos.

- **Equipos**: Información sobre los equipos de las ligas.

- **Partidos**: Datos sobre los partidos jugados.

## Imputación de Datos

Actualmente, algunos datos faltantes están siendo imputados mediante diferentes métodos:

- **Número de Pases**: Se está utilizando regresión lineal para imputar valores faltantes en el número de pases realizados por los jugadores.
- **Porcentaje de Precisión en los Pases**: Este método aún está en desarrollo. Se planea utilizar el método de K-Nearest Neighbors para imputar el porcentaje de precisión en los pases, basándose en datos similares de otros jugadores.

## Datos

Los datos están disponibles en formato CSV y se actualizan semanalmente.

## Uso

Para usar esta base de datos, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone [URL del repositorio]
   ```

2. **Importa los datos**:
   - Para CSV: Usa un script de importación o una herramienta como [nombre de la herramienta].
   - Para SQL: Ejecuta el script SQL proporcionado.

3. **Consulta los datos**:
   - Puedes usar herramientas de análisis de datos como [nombre de la herramienta] para consultar y explorar la base de datos.

## Planes Futuros

- **Mejoras en la Base de Datos**: Refinar la estructura de la base de datos según los requisitos del modelo de IA.
- **Desarrollo de Métodos de Imputación**: Completar el desarrollo del método de imputación basado en K-Nearest Neighbors y otros métodos de imputación.
- **Documentación**: Ampliar la documentación para incluir ejemplos de consultas y análisis.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos para contribuir:

1. **Fork** el repositorio.
2. **Crea** una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. **Realiza** tus cambios.
4. **Envía** un pull request.

## Contacto

Para preguntas o comentarios, contacta a Sonia en hechodeoroverde@gmail.com.
