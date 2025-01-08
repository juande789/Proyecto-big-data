# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los scripts de Python al contenedor
COPY extract.py eda.py elastic.py ./

# Instala las dependencias necesarias
RUN pip install --no-cache-dir pandas requests elasticsearch

# Comando por defecto para ejecutar los scripts secuencialmente
CMD ["bash", "-c", "python extract.py && python eda.py && python elastic.py"]
