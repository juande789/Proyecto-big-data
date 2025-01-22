######################################################
#SCRIPTS DOCKER
######################################################
#Para crear la imagen primero hay que especificar la ruta donde se encuentra el archivo con los scripts y el dockerfile, por ejemplo:
cd "C:\Users\JHOSU\OneDrive - Universidad Europea de Madrid\Escritorio\Doble Grado UEM\3º Tercero de carrera\1º Semestre\Big Data I\EcoPenguin"

#Instrucciones para crear el elastic search
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.15.3
docker run --name elastic-EcoPenguin  --net elastic -p 9200:9200 -itd -m 2GB docker.elastic.co/elasticsearch/elasticsearch:8.15.3

#Crea la imagen con los scripts de python para descargar los datos y hacer un eda para limpiarlos, una vez vez limpios con el elastic.py se insertan en elasticsearch
docker build -f ecopenguin.dockerfile -t ecopenguin-scripts .
# Script de elastic (Importante leer antes de hacer docker run)
es = Elasticsearch(
    #En la conexion a elastic recuerda que debes cambiar tu host y contraseña antes de hacer el docker run 
    #para que el script de insertar los datos en elastic no de error
    #Esto se cambia en el script elastic.py
    hosts=["https://localhost:9200"],
    basic_auth=("elastic", "q9TO8Kz2qs+0GFmOw7Ku"),
    verify_certs=False  # Desactiva la verificación de certificados en desarrollo
)
#IMPORTANTE!! ANTES DE HACER EL DOCKER RUN ANTERIOR CREA LAS DOS IMAGENES(Imagen de scripts-smartlife e imagen de elastic-smartlife)
#Ejecutamos el proyecto 
docker run -itd --name docker-ecopenguin ecopenguin-scripts

#Vemos que imagenes tenemos y comprobamos que se ha creado correctamente
docker images

######################################################
#POSTMAN
######################################################
#Visualizo los elementos que se han insertado
GET: https://localhost:9200/consumo_energetico_viviendas_historico_completo/
#Cuento cuantos datos tiene ese indice
GET: https://localhost:9200/consumo_energetico_viviendas_historico_completo/_count
GET: https://localhost:9200/consumo_energetico_viviendas_historico_completo/_search?size=10

#Paso 0
#Ejecutar lo isguientes pasos hay que instalar las siguientes librerias
#Para ejecutar los comandos del backend y forntend necesitaras las siguientes librerias
pip install fastapi
pip install uvicorn
pip install npm
pip install node

#Antes de ejecutar el comando para crear la api cambiar la contraseña de elastic de los siguiente scripts: 
#    en la carpeta backend: main, train_clustering, 
#    en la carpeta de modelos: datos_elastic, modelo_elastic 
#    y por ultimo el script llamado elastic.py

#Paso 1: Crear la api con el backend
#Primero tienes que ubicar la carpeta donde tengas el backend en mi caso es:
#cd "C:\Users\JHOSU\OneDrive\Doble Grado UEM\3º Tercero de carrera\1º Semestre\Big Data I\EcoPenguin\backend"
#Para crear la api hay que ejecutar el siguiente comando "uvicorn main:app" una vez ya ubicado en la carpeta del backend

#Paso 2: Crear el frontend
#Para que el comando funcione tienes que tener instalado https://nodejs.org/ en node.js para ejecutar archivos java script y crear un servidor local
#Esto instalará todas las dependencias listadas en el archivo package.json.

#Ahora para el frontend te ubicas en la carpeta que tengas guardado como el backend, en mi caso es:
#cd "C:\Users\JHOSU\OneDrive\Doble Grado UEM\3º Tercero de carrera\1º Semestre\Big Data I\EcoPenguin\frontend"
#Para crear el frontend hay que ejecutar el siguiente comando "npm start" una vez ya ubicado en la carpeta del frontend

