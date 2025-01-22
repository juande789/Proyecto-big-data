from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle
import os  # Para manejar la ubicación de los archivos

# Conexión a Elasticsearch
es = Elasticsearch(
    hosts=["https://localhost:9200"],
    basic_auth=("elastic", "q9TO8Kz2qs+0GFmOw7Ku"),
    verify_certs=False
)

# Índice seleccionado
index_name = "consumo_energetico_viviendas_historico_completo"

# Consulta para obtener todos los datos
query = {
    "query": {"match_all": {}},
    "size": 10000  # Ajusta si tienes más documentos
}

# Obtener datos desde Elasticsearch
response = es.search(index=index_name, body=query)
hits = response["hits"]["hits"]

if not hits:
    raise ValueError("No se encontraron datos en Elasticsearch.")

# Convertir resultados en un DataFrame
df = pd.DataFrame([hit["_source"] for hit in hits])

# Filtrar columnas relevantes
required_columns = [
    "Consumo energetico (kWh/m²)",
    "Media de residentes",
    "Potencia contratada (kW)"
]
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Faltan columnas necesarias en los datos: {required_columns}")

df = df[required_columns].dropna()

if df.empty:
    raise ValueError("No hay datos suficientes después de filtrar y eliminar valores nulos.")

# Estandarización de datos
scaler = StandardScaler()
features_scaled = scaler.fit_transform(df)

# Entrenar modelo KMeans
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(features_scaled)

# Guardar el modelo y el scaler como archivos binarios en el mismo directorio
output_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(output_dir, "kmeans_model.pkl")
scaler_path = os.path.join(output_dir, "scaler.pkl")

with open(model_path, "wb") as f:
    pickle.dump(kmeans, f)

with open(scaler_path, "wb") as f:
    pickle.dump(scaler, f)

print(f"Modelo KMeans y scaler guardados correctamente en: {output_dir}")
