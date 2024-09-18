import csv

# Nombre del archivo de entrada (txt) y de salida (csv)
input_file = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/archivos_procesados/c_archivo_para_csv.txt'
output_file = 'C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/scrap_matches_stadistics/clean_txt_matches/archivos_procesados/d_archivo_final.csv'

# Abre el archivo de texto para leer y el archivo CSV para escribir
with open(input_file, 'r') as txt_file, open(output_file, 'w', newline='') as csv_file:
    # Crea un lector y un escritor de CSV
    csv_writer = csv.writer(csv_file)
    
    # Itera sobre cada línea del archivo de texto
    for line in txt_file:
        # Divide la línea en campos usando la coma como delimitador
        fields = line.strip().split(',')
        
        # Escribe los campos en el archivo CSV
        csv_writer.writerow(fields)

print(f"Archivo '{output_file}' creado exitosamente.")
