######################################################
# Script de elastic (Importante leer antes de hacer docker run)
######################################################
es = Elasticsearch(
    #En la conexion a elastic recuerda que debes cambiar tu host y contraseña antes de hacer el docker run 
    #para que el script de insertar los datos en elastic no de error
    #Esto se cambia en el script elastic.py
    hosts=["https://localhost:9200"],
    basic_auth=("elastic", "z_KZpPqMoB5dQxM+ExjV"),
    verify_certs=False  # Desactiva la verificación de certificados en desarrollo
)

######################################################
#SCRIPTS DOCKER
######################################################
#Para crear la imagen primero hay que especificar la ruta donde se encuentra el archivo con los scripts y el dockerfile, por ejemplo:
cd "C:\Users\JHOSU\OneDrive - Universidad Europea de Madrid\Escritorio\Doble Grado UEM\3º Tercero de carrera\1º Semestre\Big Data I\docker_SmartLife\scriptsDocker"
#Crea la imagen con los scripts de python para descargar los datos y hacer un eda para limpiarlos, una vez vez limpios con el elastic.py se insertan en elasticsearch
docker build -f smartlife.dockerfile -t docker-scripts .

#Instrucciones para crear el elastic search
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.15.3
docker run --name elastic-smartlife  --net elastic -p 9200:9200 -itd -m 2GB docker.elastic.co/elasticsearch/elasticsearch:8.15.3
#Vemos que imagenes tenemos y comprobamos que se ha creado correctamente
docker images
#IMPORTANTE!! ANTES DE HACER EL DOCKER RUN ANTERIOR CREA LAS DOS IMAGENES(Imagen de scripts-smartlife e imagen de elastic-smartlife)
#Ejecutamos el proyecto 
docker run -itd --name docker-smartlife docker-scripts

######################################################
#POSTMAN
######################################################
#Compruebo cuantos elementos se han insertado
GET: https://localhost:9200/df_balance_energetico/_search
#Cuento cuantos datos tiene ese indice
GET: https://localhost:9200/df_balance_energetico/_count
GET: https://localhost:9200/df_demanda_evolucion/_count
GET: https://localhost:9200/df_precios_mercado/_count
