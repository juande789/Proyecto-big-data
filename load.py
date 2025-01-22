import os
import shutil

# Nombre del archivo CSV
csv_file = "Consumo_Energetico_Viviendas_Historico_Completo.csv"

# Nombre de la carpeta donde se guardará el archivo
data_folder = "data"

def create_data_folder_and_move_csv():
    # Crear la carpeta 'data' si no existe
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f"Carpeta '{data_folder}' creada.")

    # Mover el archivo CSV a la carpeta 'data'
    if os.path.exists(csv_file):
        shutil.move(csv_file, os.path.join(data_folder, csv_file))
        print(f"Archivo '{csv_file}' movido a la carpeta '{data_folder}'.")
    else:
        print(f"El archivo '{csv_file}' no se encontró en el directorio actual.")

if __name__ == "__main__":
    create_data_folder_and_move_csv()
