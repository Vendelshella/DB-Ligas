def combinar_lineas_y_guardar(archivo_entrada, archivo_salida):
    # Abre el archivo de entrada en modo lectura
    with open(archivo_entrada, 'r') as f:
        # Lee todas las líneas del archivo
        lineas = f.readlines()

    # Abre el archivo de salida en modo escritura
    with open(archivo_salida, 'w') as f_salida:
        # Escribir el nombre de la columna en la primera línea
        f_salida.write('Fecha,GolesLocal,EquipoLocalID,GolesVisit,EquipoVisitID\n')

        # Itera sobre las líneas en grupos de cuatro
        for i in range(0, len(lineas), 5):
            # Toma el siguiente grupo de cuatro líneas
            grupo = lineas[i:i + 5]

            # Comprueba si hay exactamente 4 líneas en el grupo
            if len(grupo) == 5:
                # Quita los saltos de línea y une las líneas con comas
                linea_combinada = ','.join(linea.strip() for linea in grupo)
                # Escribe la línea combinada en el archivo de salida
                f_salida.write(linea_combinada + '\n')

    print(f"Las primeras 4 líneas se han combinado y guardado en {archivo_salida}")

# Especifica los nombres de los archivos de entrada y salida
archivo_entrada = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/archivos_procesados/b_archivo_sin_lineas_vacias.txt'
archivo_salida = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/archivos_procesados/c_archivo_para_csv.txt'

# Llama a la función con los nombres de archivo especificados
combinar_lineas_y_guardar(archivo_entrada, archivo_salida)
