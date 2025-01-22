from elasticsearch import Elasticsearch

# Conexión a Elasticsearch
es = Elasticsearch(
    hosts=["https://localhost:9200"],
    basic_auth=("elastic", "q9TO8Kz2qs+0GFmOw7Ku"),
    verify_certs=False
)

# Obtener todos los índices
indices = es.cat.indices(format="json")  # Devuelve una lista de índices en formato JSON

# Imprimir los nombres de los índices
print("Lista de indices en Elasticsearch:")
for index in indices:
    print(index["index"])
