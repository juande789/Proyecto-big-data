from fastapi import FastAPI
from elasticsearch import Elasticsearch
from prophet import Prophet
from sklearn.cluster import KMeans
from pydantic import BaseModel
import pandas as pd
import pickle
import numpy as np
from typing import Dict

app = FastAPI()

# Conexión a Elasticsearch
es = Elasticsearch(
    hosts=["https://localhost:9200"],  # HTTPS porque el servidor requiere esto
    basic_auth=("elastic", "q9TO8Kz2qs+0GFmOw7Ku"),  # Contraseña actualizada
    verify_certs=False  # Evita problemas con certificados
)

# Configurar índices en Elasticsearch
def configurar_indices():
    indices = ["consumo_energetico_viviendas_historico_completo", "predicciones", "clusters"]
    for index in indices:
        if not es.indices.exists(index=index):
            es.indices.create(index=index)
            print(f"Índice '{index}' creado en Elasticsearch.")

# Llamar configuración de índices al iniciar la aplicación
configurar_indices()

@app.get("/")
async def root():
    return {"message": "EcoPenguin API está funcionando"}

@app.get("/search")
async def search_data(
    provincia: str = None,
    start_date: str = None,
    end_date: str = None
):
    query = {
        "query": {
            "bool": {
                "must": [],
                "filter": []
            }
        }
    }

    if provincia:
        query["query"]["bool"]["must"].append({
            "match": {"Provincia": provincia}
        })

    if start_date and end_date:
        query["query"]["bool"]["filter"].append({
            "range": {
                "Fecha": {
                    "gte": start_date,
                    "lte": end_date
                }
            }
        })

    try:
        response = es.search(index="consumo_energetico_viviendas_historico_completo", body=query)
        hits = [hit["_source"] for hit in response["hits"]["hits"]]
        return {"results": hits}
    except Exception as e:
        return {"error": str(e)}

# Modelo de entrada para predicciones
class PredictRequest(BaseModel):
    provincia: str
    periods: int = 30  # Valor por defecto si no se especifica

@app.post("/predict")
async def predict_energy(request: PredictRequest):
    provincia = request.provincia
    periods = request.periods

    try:
        query = {
            "query": {
                "match": {"Provincia": provincia}
            },
            "size": 10000
        }
        response = es.search(index="consumo_energetico_viviendas_historico_completo", body=query)
        hits = [hit["_source"] for hit in response["hits"]["hits"]]

        df = pd.DataFrame(hits)
        df["Fecha"] = pd.to_datetime(df["Fecha"])
        df = df[["Fecha", "Consumo energetico (kWh/m²)"]]
        df.rename(columns={"Fecha": "ds", "Consumo energetico (kWh/m²)": "y"}, inplace=True)

        model = Prophet()
        model.fit(df)

        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)

        result = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(periods)

        for _, row in result.iterrows():
            doc = row.to_dict()
            es.index(index="predicciones", document=doc)

        return result.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/estadisticas")
async def estadisticas_generales(provincia: str = None):
    try:
        query = {"size": 10000}
        if provincia:
            query["query"] = {"match": {"Provincia": provincia}}

        response = es.search(index="consumo_energetico_viviendas_historico_completo", body=query)
        hits = [hit["_source"] for hit in response["hits"]["hits"]]

        df = pd.DataFrame(hits)
        df = df[["Consumo energetico (kWh/m²)"]].dropna()

        media = df["Consumo energetico (kWh/m²)"].mean()
        moda = df["Consumo energetico (kWh/m²)"].mode().iloc[0] if not df.empty else None
        varianza = df["Consumo energetico (kWh/m²)"].var()

        return {
            "media": media,
            "moda": moda,
            "varianza": varianza,
        }
    except Exception as e:
        return {"error": str(e)}

# Cargar modelo y scaler desde archivos
with open("kmeans_model.pkl", "rb") as model_file:
    kmeans_model = pickle.load(model_file)

with open("scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

clusters = kmeans_model.cluster_centers_
recommendations = {
    0: "Evaluar posibles ajustes en potencia contratada para mayor eficiencia.",
    1: "Proponer optimización de electrodomésticos o tarifas energéticas.",
    2: "Incentivar el uso de energías renovables debido a su alta potencia contratada.",
    3: "Identificar qué prácticas o tecnologías adoptan para promoverlas en otros clusters.",
}

class ClusterRequest(BaseModel):
    consumo: float
    residentes: float
    potencia: float

@app.post("/analyze-cluster")
def analyze_cluster(request: ClusterRequest) -> Dict:
    user_data = np.array([[request.consumo, request.residentes, request.potencia]])
    user_data_scaled = scaler.transform(user_data)

    closest_cluster = kmeans_model.predict(user_data_scaled)[0]

    return {
        "cluster": int(closest_cluster),
        "recomendacion": recommendations[closest_cluster],
    }

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
