# Nombre del archivo original
archivo_entrada = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/archivos_procesados/a_archivo_limpio.txt'

# Nombre del archivo de salida
archivo_salida = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/archivos_procesados/b_archivo_sin_lineas_vacias.txt'

# Abrir el archivo de entrada en modo lectura y el archivo de salida en modo escritura
with open(archivo_entrada, 'r') as archivo_lectura, open(archivo_salida, 'w') as archivo_escritura:
    # Leer línea por línea
    for linea in archivo_lectura:
        # Eliminar los espacios en blanco al inicio y final de cada línea
        linea = linea.strip()
        # Si la línea no está vacía, escríbela en el archivo de salida
        if linea:
            archivo_escritura.write(linea + '\n')

print(f'Las líneas vacías han sido eliminadas y el resultado se ha guardado en {archivo_salida}.')
