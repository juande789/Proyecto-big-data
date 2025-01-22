from elasticsearch import Elasticsearch, helpers
import json
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Conexión a Elasticsearch
es = Elasticsearch(
    hosts=["https://localhost:9200"],
    basic_auth=("elastic", "q9TO8Kz2qs+0GFmOw7Ku"),
    verify_certs=False  # Desactiva la verificación de certificados en desarrollo
)

# Carpeta con los archivos JSON
input_folder = "./elastic-data1/"
state_file = "./elastic-data1/state.json"  # Archivo para registrar progreso

# Leer estado de progreso
if os.path.exists(state_file):
    with open(state_file, "r", encoding="utf-8") as f:
        processed_files = set(json.load(f))
else:
    processed_files = set()

def load_json(file_path, index_name):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            doc = json.loads(line)
            yield {
                "_index": index_name,
                "_source": doc
            }

try:
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json") and file_name not in processed_files:
            index_name = file_name.replace("bulk_", "").replace(".json", "").lower()
            file_path = os.path.join(input_folder, file_name)
            try:
                helpers.bulk(es, load_json(file_path, index_name))
                print(f"Datos de '{file_name}' insertados correctamente en el indice '{index_name}'.")
                # Registrar el archivo como procesado
                processed_files.add(file_name)
                with open(state_file, "w", encoding="utf-8") as f:
                    json.dump(list(processed_files), f)
            except Exception as e:
                print(f"Error al insertar datos de '{file_name}': {e}")
except Exception as e:
    print(f"Error general: {e}")