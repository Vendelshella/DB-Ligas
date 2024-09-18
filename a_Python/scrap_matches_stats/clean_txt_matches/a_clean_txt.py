import re

ID_teams = {
            'AMOREBIETAAMOREBIETA' : 'AMOREBIETA',
            'GRANADAGRANADA' : 'GRANADA',
            'U. D. LAS PALMASU. D. LAS PALMAS' : 'PALMAS',
            'LEVANTELEVANTE' : 'LEVANTE',
            'ALAVESALAVES' : 'ALAVES',
            'ALCORCONALCORCON' : 'ALCORCON',
            'EIBAREIBAR' : 'EIBAR',
            'ELCHE C. F.ELCHE C. F.' : 'ELCHE',
            'CD ELDENSECD ELDENSE' : 'ELDENSE',
            'RCD ESPANYOLRCD ESPANYOL' : 'ESPANYOL',
            'ALBACETEALBACETE' : 'ALBACETE',
            'FC ANDORRAFC ANDORRA' : 'ANDORRA',
            'REAL OVIEDOREAL OVIEDO' : 'OVIEDO',
            'CARTAGENACARTAGENA' : 'CARTAGENA',
            'TENERIFETENERIFE' : 'TENERIFE',
            'BURGOSBURGOS' : 'BURGOS',
            'RACING DE SANTANDERRACING DE SANTANDER' :'SANTANDER',
            'REAL ZARAGOZAREAL ZARAGOZA' : 'ZARAGOZA',
            'LEGANESLEGANES' : 'LEGANES',
            'S. D. HUESCAS. D. HUESCA' : 'HUESCA',
            'MIRANDESMIRANDES' : 'MIRANDES',
            'RACING FERROLRACING FERROL' : 'FERROL',
            'SPORTING GIJONSPORTING GIJON' : 'GIJON',
            'VALLADOLIDVALLADOLID' : 'VALLADOLID',
            'VILLARREAL BVILLARREAL B' : 'VILLARREALB',
            'PONFERRADINAPONFERRADINA' : 'PONFERRADINA',
            'MALAGAMALAGA' : 'MALAGA',
            'UD IBIZAUD IBIZA' : 'IBIZA',
            'CD LUGOCD LUGO' : 'LUGO'
        }

def clean_and_uppercase_txt(input_file, output_file, frases_a_eliminar, partes_a_reemplazar, ID_teams):
    # Tabla de traducción para reemplazar vocales acentuadas por no acentuadas
    tabla_traduccion = str.maketrans('ÁÉÍÓÚáéíóú', 'AEIOUaeiou')
    
    # Leer el contenido del archivo de texto
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Abrir el archivo de salida para escribir
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            # Verificar si la línea contiene alguna de las frases a eliminar (completas)
            if not any(frase in line for frase in frases_a_eliminar):
                # Reemplazar las partes específicas dentro de la línea
                for parte in partes_a_reemplazar:
                    line = re.sub(re.escape(parte), '', line)
                # Convertir la línea a mayúsculas
                line = line.upper()
                # Reemplazar vocales acentuadas por no acentuadas
                line = line.translate(tabla_traduccion)
                # Reemplazar cada equipo por su ID
                for key, value in ID_teams.items():
                    line = re.sub(re.escape(key), value, line)

                # Escribir la línea modificada en el archivo de salida
                file.write(line)

    print(f"Se ha creado un nuevo archivo '{output_file}' con las frases eliminadas, partes reemplazadas, texto en mayúsculas y vocales acentuadas reemplazadas.")

# Configurar nombres de archivo y frases a eliminar
input_file = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/partidos.txt'
output_file = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/archivos_procesados/a_archivo_limpio.txt'
frases_a_eliminar = [
    'Resumen del partido',
    'Fin',
    'Jornada',
    'Resultado global'
]
partes_a_reemplazar = [
    'Tarjetas rojas'
]

# Llamar a la función para limpiar el texto, convertirlo a mayúsculas y reemplazar vocales acentuadas
clean_and_uppercase_txt(input_file, output_file, frases_a_eliminar, partes_a_reemplazar, ID_teams)

print(f"Se ha creado un nuevo archivo '{output_file}' con las frases eliminadas, partes reemplazadas, texto en mayúsculas y vocales acentuadas reemplazadas.")


'''
Copiar los txt a limpiar de google: https://www.google.com/search?q=liga+segunda+division+2022-23&rlz=1C1UEAD_esES1044ES1044&oq=&gs_lcrp=EgZjaHJvbWUqBggCEEUYOzIHCAAQABiPAjINCAEQLhiDARixAxiABDIGCAIQRRg7MgYIAxAjGCcyBggEEEUYOzIHCAUQABiABDIGCAYQRRg8MgYIBxBFGDzSAQg2NzE2ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8#sie=lg;/g/11szbxr4z7;2;/m/0d55r5;tbbs;hd;;;;2023-04-02T12:00:00Z&wptab=si:ACC90nzMYCYlkgFB5ZdPNg5MNw2Sn8ztJuIAa71gr4X55JeN6FdoxblFUOS8KYMl336u9VZr6vfme3O9gaYgIXw1oPR7Q5Ly4mtKbwfF82J4z0JyadSE_q6KMTW6LyRvC_Q7HJgmO767L8KN3FUqdy8pDoZcFjUzBuL4sOFlBboC42GdIjD5c60u49zg1u2exAD9_bQ183JbKCDnrkuBZNPfZ9Wm61lbi-tGz1AFu2GQ6dh_Pmh3kgCfUvuRk-TzoVaTwup1XnMcMrObPsU0_f464QbicCIpQJuXgykLeRFpz-icsYR7Eas%3D
'''