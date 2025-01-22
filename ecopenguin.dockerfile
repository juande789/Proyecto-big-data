# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los scripts de Python al contenedor
COPY load.py transform.py elastic.py train_clustering.py ./
# Copia los scripts de Python al contenedor
COPY extractData1.py edaData1.py elasticData1.py ./
# Copia el archivo CSV al contenedor
COPY Consumo_Energetico_Viviendas_Historico_Completo.csv ./

# Copiar el archivo de requerimientos si existe o instalar directamente
COPY requirements.txt requirements.txt
# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar los scripts secuencialmente
CMD ["bash", "-c", "python extractData1.py && python edaData1.py && load.py && python transform.py && train_clustering.py && python elastic.py && python elasticData1.py "]
