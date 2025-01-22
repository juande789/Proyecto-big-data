from elasticsearch import Elasticsearch, helpers
import json
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Conexión a Elasticsearch
es = Elasticsearch(
    hosts=["https://localhost:9200"],
    basic_auth=("elastic", "q9TO8Kz2qs+0GFmOw7Ku"),
    verify_certs=False
)

# Carpeta con los archivos JSON
input_folder = "./elastic-data/"
state_file = "./elastic-data/state.json"  # Archivo para registrar progreso

def delete_index(index_name):
    """Eliminar índice si ya existe"""
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        print(f"Indice '{index_name}' eliminado.")

def load_json(file_path, index_name):
    """Leer archivo JSON y prepararlo para inserción"""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            doc = json.loads(line)
            yield {
                "_index": index_name,
                "_source": doc
            }

try:
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            index_name = file_name.replace("bulk_", "").replace(".json", "").lower()
            file_path = os.path.join(input_folder, file_name)

            # Eliminar índice si ya existe
            delete_index(index_name)

            # Insertar datos
            try:
                helpers.bulk(es, load_json(file_path, index_name))
                print(f"Datos de '{file_name}' insertados correctamente en el indice '{index_name}'.")
            except Exception as e:
                print(f"Error al insertar datos de '{file_name}': {e}")

except Exception as e:
    print(f"Error general: {e}")
