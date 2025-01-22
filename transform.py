import os
import pandas as pd

# Nombre de la carpeta donde está el archivo CSV
data_folder = "data"
# Nombre de la carpeta donde se guardará el archivo JSON
elastic_data_folder = "elastic-data"
# Nombre del archivo CSV
csv_file = "Consumo_Energetico_Viviendas_Historico_Completo.csv"
# Nombre del archivo JSON
json_file = "Consumo_Energetico_Viviendas_Historico_Completo.json"

def transform_csv_to_json():
    # Verificar si la carpeta 'data' existe
    if not os.path.exists(data_folder):
        print(f"La carpeta '{data_folder}' no existe. Ejecuta primero el script 'load.py'.")
        return

    # Ruta completa del archivo CSV
    csv_path = os.path.join(data_folder, csv_file)

    # Verificar si el archivo CSV existe
    if not os.path.exists(csv_path):
        print(f"El archivo '{csv_file}' no se encontró en la carpeta '{data_folder}'.")
        return

    # Leer el archivo CSV
    print(f"Leyendo el archivo CSV '{csv_path}'...")
    data = pd.read_csv(csv_path)

    # Crear la carpeta 'elastic-data' si no existe
    if not os.path.exists(elastic_data_folder):
        os.makedirs(elastic_data_folder)
        print(f"Carpeta '{elastic_data_folder}' creada.")

    # Ruta completa del archivo JSON
    json_path = os.path.join(elastic_data_folder, json_file)

    # Guardar los datos en formato JSON
    print(f"Guardando los datos transformados en '{json_path}'...")
    data.to_json(json_path, orient="records", lines=True, force_ascii=False)
    print("Transformacion completada y archivo JSON guardado.")

if __name__ == "__main__":
    transform_csv_to_json()