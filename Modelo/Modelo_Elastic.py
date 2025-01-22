from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt
import seaborn as sns

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
    "query": {
        "match_all": {}
    },
    "size": 10000  # Ajusta el tamaño si tienes más documentos
}

# Obtener datos desde Elasticsearch
response = es.search(index=index_name, body=query)
hits = response["hits"]["hits"]

# Convertir resultados en un DataFrame
data = [hit["_source"] for hit in hits]
df = pd.DataFrame(data)

# Verificar datos cargados
print("\nDatos cargados desde Elasticsearch:")
print(df.head())

# Selección de características para clustering (ajustar según dataset)
# Consideraremos solo columnas numéricas y sin valores nulos
features = df.select_dtypes(include=np.number).dropna(axis=1)
print("\nCaracterísticas seleccionadas para clustering:")
print(features.columns)

# Estandarización de los datos
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Encontrar el número óptimo de clusters con Elbow Method
inertia = []
range_n_clusters = range(2, 11)  # Probar de 2 a 10 clusters
for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Graficar el método del codo
plt.figure(figsize=(8, 5))
plt.plot(range_n_clusters, inertia, marker='o')
plt.xlabel("Número de clusters")
plt.ylabel("Inercia (Suma de Distancias al Centro)")
plt.title("Método del Codo")
plt.show()

# Ajuste del modelo K-Means con el número óptimo de clusters (ejemplo: 4)
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
clusters = kmeans.fit_predict(features_scaled)

# Añadir los clusters al DataFrame
df["Cluster"] = clusters

# Métricas de evaluación
silhouette_avg = silhouette_score(features_scaled, clusters)
davies_bouldin = davies_bouldin_score(features_scaled, clusters)
print(f"\nCoeficiente de Silhouette: {silhouette_avg:.2f}")
print(f"Índice de Davies-Bouldin: {davies_bouldin:.2f}")

# Visualización de Clusters (solo si las primeras 2 características son representativas)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x=features_scaled[:, 0], y=features_scaled[:, 1],
    hue=clusters, palette="Set1", s=50
)
plt.xlabel("Característica 1 (Estandarizada)")
plt.ylabel("Característica 2 (Estandarizada)")
plt.title(f"Visualización de Clusters (K-Means, {optimal_clusters} Clusters)")
plt.legend(title="Cluster")
plt.show()
