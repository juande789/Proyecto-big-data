import os
import pandas as pd
from datetime import datetime
import json

########################################################################
#   LIMPIAR BALANCE ENERGÉTICO                                         #
########################################################################

# Verificar la existencia del archivo CSV
csv_path = "./data1/balance_energia.csv"
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"El archivo '{csv_path}' no existe.")

try:
    df_balance_energetico = pd.read_csv(csv_path)
except Exception as e:
    print(f"Error al cargar el archivo CSV: {e}")
    exit()

# Convert 'date' column to datetime with UTC handling
df_balance_energetico['date'] = pd.to_datetime(df_balance_energetico['date'], utc=True)
df_balance_energetico['date'] = df_balance_energetico['date'].dt.strftime('%Y-%m-%d')
# Eliminar duplicados si es necesario
df_balance_energetico.drop_duplicates(inplace=True)

########################################################################
#    LIMPIAR DEMANDA EVOLUCIÓN                                         #                                                   
########################################################################

# Lista para almacenar los DataFrames
dataframes = []

# Generar las rutas y leer los archivos
for year in range(2013, 2024):  # Años desde 2011 hasta 2023
    for month in range(1, 13):  # Meses del 1 al 12
        # Formatear el mes como 01, 02, etc.
        month_str = f"{month:02d}"
        # Generar la ruta del archivo
        file_path = f"./data1/demanda_evolucion_{year}_{month_str}.csv"
        try:
            # Leer el archivo CSV
            df = pd.read_csv(file_path)
            # Agregar una columna para indicar el año y mes
            df["Year"] = year
            df["Month"] = month
            # Agregar el DataFrame a la lista
            dataframes.append(df)
        except FileNotFoundError:
            # Si el archivo no existe, pasar al siguiente
            print(f"Archivo no encontrado: {file_path}")
            continue

# Combinar todos los DataFrames en uno solo
df_demanda_evolucion = pd.concat(dataframes, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_demanda_evolucion['date'] = pd.to_datetime(df_demanda_evolucion['date'], utc=True)
df_demanda_evolucion['date'] = df_demanda_evolucion['date'].dt.strftime('%Y-%m-%d')

########################################################################
#    LIMPIAR Precios Mercado                                           #                                                     
########################################################################

# Lista para almacenar los DataFrames
dataframes = []

# Generar las rutas y leer los archivos
for year in range(2014, 2023):  # Años desde 2014 hasta 2022
    for month in range(1, 13):  # Meses del 1 al 12
        # Formatear el mes como 01, 02, etc.
        month_str = f"{month:02d}"
        # Generar la ruta del archivo
        file_path = f"./data1/precios_mercado_{year}_{month_str}.csv"
        try:
            # Leer el archivo CSV
            df = pd.read_csv(file_path)
            # Agregar una columna para indicar el año y mes
            df["Year"] = year
            df["Month"] = month
            # Agregar el DataFrame a la lista
            dataframes.append(df)
        except FileNotFoundError:
            # Si el archivo no existe, pasar al siguiente
            print(f"Archivo no encontrado: {file_path}")
            continue

# Combinar todos los DataFrames en uno solo
df_precios_mercado = pd.concat(dataframes, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_precios_mercado['date'] = pd.to_datetime(df_precios_mercado['date'], utc=True)
df_precios_mercado['date'] = df_precios_mercado['date'].dt.strftime('%Y-%m-%d')

#####################################
#   LIMPIAR EVOLUCIÓN DE LA DEMANDA #                  
#                                   #
#####################################

#Pon laS rutas del archivo del docker
evolucion_demanda_2011=pd.read_csv("./data1/data_es_demanda_evolucion_2011.csv")
evolucion_demanda_2012=pd.read_csv("./data1/data_es_demanda_evolucion_2012.csv")
evolucion_demanda_2013=pd.read_csv("./data1/data_es_demanda_evolucion_2013.csv")
evolucion_demanda_2014=pd.read_csv("./data1/data_es_demanda_evolucion_2014.csv")
evolucion_demanda_2015=pd.read_csv("./data1/data_es_demanda_evolucion_2015.csv")
evolucion_demanda_2016=pd.read_csv("./data1/data_es_demanda_evolucion_2016.csv")
evolucion_demanda_2017=pd.read_csv("./data1/data_es_demanda_evolucion_2017.csv")
evolucion_demanda_2018=pd.read_csv("./data1/data_es_demanda_evolucion_2018.csv")
evolucion_demanda_2019=pd.read_csv("./data1/data_es_demanda_evolucion_2019.csv")
evolucion_demanda_2020=pd.read_csv("./data1/data_es_demanda_evolucion_2020.csv")
evolucion_demanda_2021=pd.read_csv("./data1/data_es_demanda_evolucion_2021.csv")
evolucion_demanda_2022=pd.read_csv("./data1/data_es_demanda_evolucion_2022.csv")
evolucion_demanda_2023=pd.read_csv("./data1/data_es_demanda_evolucion_2023.csv")


# Combinar los dataframes
dataframes = [
    evolucion_demanda_2011, evolucion_demanda_2012, evolucion_demanda_2013, 
    evolucion_demanda_2014, evolucion_demanda_2015, evolucion_demanda_2016, 
    evolucion_demanda_2017, evolucion_demanda_2018, evolucion_demanda_2019, 
    evolucion_demanda_2020, evolucion_demanda_2021, evolucion_demanda_2022, 
    evolucion_demanda_2023
]

# Combinar todos los dataframes en uno solo
combined_evolucion_demanda = pd.concat(dataframes, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
# Convert 'date' column to datetime with UTC handling
combined_evolucion_demanda['Datetime'] = pd.to_datetime(combined_evolucion_demanda['Datetime'], utc=True)
# Format the datetime to 'YYYY-MM-DD'
combined_evolucion_demanda['Datetime'] = combined_evolucion_demanda['Datetime'].dt.strftime('%Y-%m-%d')

#####################################
#   LIMPIAR PERDIDAS DE TRANSPORTE  #                  
#                                   #
#####################################

#Pon laS rutas del archivo del docker
df_perdidas_transporte_2014=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2014.csv")
df_perdidas_transporte_2015=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2015.csv")
df_perdidas_transporte_2016=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2016.csv")
df_perdidas_transporte_2017=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2017.csv")
df_perdidas_transporte_2018=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2018.csv")
df_perdidas_transporte_2019=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2019.csv")
df_perdidas_transporte_2020=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2020.csv")
df_perdidas_transporte_2021=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2021.csv")
df_perdidas_transporte_2022=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2022.csv")
df_perdidas_transporte_2023=pd.read_csv("./data1/data_es_demanda_perdidas-transporte_2023.csv")

# Combinar los dataframes en uno solo
df_perdidas_transporte_list = [
    df_perdidas_transporte_2014, df_perdidas_transporte_2015, df_perdidas_transporte_2016,
    df_perdidas_transporte_2017, df_perdidas_transporte_2018, df_perdidas_transporte_2019,
    df_perdidas_transporte_2020, df_perdidas_transporte_2021, df_perdidas_transporte_2022,
    df_perdidas_transporte_2023
]
# Combinar todos los dataframes en uno solo
df_perdidas_transporte_combined = pd.concat(df_perdidas_transporte_list, ignore_index=True)
df_perdidas_transporte_combined = df_perdidas_transporte_combined[df_perdidas_transporte_combined['Indicator'] != 'Demanda']
# Convert 'date' column to datetime with UTC handling
df_perdidas_transporte_combined['Datetime'] = pd.to_datetime(df_perdidas_transporte_combined['Datetime'], utc=True)
# Format the datetime to 'YYYY-MM-DD'
df_perdidas_transporte_combined['Datetime'] = df_perdidas_transporte_combined['Datetime'].dt.strftime('%Y-%m-%d')

###############################################
#   LIMPIAR VARIACION DE COMPONENTES MOVILES  #                  
#                                             #
###############################################

#Pon laS rutas del archivo del docker
df_variacion_componentes_moviles_2011=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2011.csv")
df_variacion_componentes_moviles_2012=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2012.csv")
df_variacion_componentes_moviles_2013=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2013.csv")
df_variacion_componentes_moviles_2014=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2014.csv")
df_variacion_componentes_moviles_2015=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2015.csv")
df_variacion_componentes_moviles_2016=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2016.csv")
df_variacion_componentes_moviles_2017=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2017.csv")
df_variacion_componentes_moviles_2018=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2018.csv")
df_variacion_componentes_moviles_2019=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2019.csv")
df_variacion_componentes_moviles_2020=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2020.csv")
df_variacion_componentes_moviles_2021=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2021.csv")
df_variacion_componentes_moviles_2022=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2022.csv")
df_variacion_componentes_moviles_2023=pd.read_csv("./data1/data_es_demanda_variacion-componentes-movil_2023.csv")

# Combinar los dataframes en uno solo
df_variacion_componentes_moviles_list = [
    df_variacion_componentes_moviles_2011, df_variacion_componentes_moviles_2012, 
    df_variacion_componentes_moviles_2013, df_variacion_componentes_moviles_2014, 
    df_variacion_componentes_moviles_2015, df_variacion_componentes_moviles_2016, 
    df_variacion_componentes_moviles_2017, df_variacion_componentes_moviles_2018, 
    df_variacion_componentes_moviles_2019, df_variacion_componentes_moviles_2020, 
    df_variacion_componentes_moviles_2021, df_variacion_componentes_moviles_2022, 
    df_variacion_componentes_moviles_2023
]
df_variacion_componentes_moviles_combined = pd.concat(df_variacion_componentes_moviles_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_variacion_componentes_moviles_combined['Datetime'] = pd.to_datetime(df_variacion_componentes_moviles_combined['Datetime'], utc=True)
df_variacion_componentes_moviles_combined['Datetime'] = df_variacion_componentes_moviles_combined['Datetime'].dt.strftime('%Y-%m-%d')

# IMPORTANTE: VOY A GUARDAR EN DATAFRAMES DISTINTOS ESTE DATAFRAMES SEGÚN EL TIPO DE INDICATOR XQ NO TIENEN NADA QUE VER UNOS CON OTROS
# A CONTINUACIÓN PONGO LA EXPLICACIÓN DE CADA UNO DE ELLOS

# Laboralidad: Indica cómo los días laborales impactan en la demanda eléctrica. 
# Por ejemplo, los días laborales típicamente tienen una mayor demanda debido a la actividad industrial y 
# comercial en comparación con fines de semana o festivos.
df_laboralidad_combined = df_variacion_componentes_moviles_combined[df_variacion_componentes_moviles_combined['Indicator'] == 'Laboralidad']
# Temperatura: Refleja la relación entre las variaciones en la temperatura y su impacto en la demanda eléctrica. 
# Las temperaturas extremas (frío o calor) suelen incrementar el uso de sistemas de calefacción o aire acondicionado.
df_temperatura_combined = df_variacion_componentes_moviles_combined[df_variacion_componentes_moviles_combined['Indicator'] == 'Temperatura']
# Demanda corregida: Es una medida de la demanda eléctrica ajustada para eliminar el efecto de factores externos, 
# como condiciones climáticas o días especiales, proporcionando una visión más precisa de la tendencia subyacente.
df_demanda_corregida_combined = df_variacion_componentes_moviles_combined[df_variacion_componentes_moviles_combined['Indicator'] == 'Demanda corregida']
# Variación de la demanda: Representa los cambios en la demanda eléctrica en comparación con un período anterior. 
# Este indicador puede usarse para analizar patrones de crecimiento o reducción en el consumo eléctrico.
df_variacion_demanda_combined = df_variacion_componentes_moviles_combined[df_variacion_componentes_moviles_combined['Indicator'] == 'Variación de la demandadf_variacion_componentes_moviles_combined']

###############################################
#  LIMPIAR ESTRUCTURA GENERACION ELECTRICA     #                  
#                                             #
###############################################

#Pon laS rutas del archivo del docker
df_estructura_generacionelectrica_2011=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2011.csv")
df_estructura_generacionelectrica_2012=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2012.csv")
df_estructura_generacionelectrica_2013=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2013.csv")
df_estructura_generacionelectrica_2014=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2014.csv")
df_estructura_generacionelectrica_2015=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2015.csv")
df_estructura_generacionelectrica_2016=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2016.csv")
df_estructura_generacionelectrica_2017=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2017.csv")
df_estructura_generacionelectrica_2018=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2018.csv")
df_estructura_generacionelectrica_2019=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2019.csv")
df_estructura_generacionelectrica_2020=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2020.csv")
df_estructura_generacionelectrica_2021=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2021.csv")
df_estructura_generacionelectrica_2022=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2022.csv")
df_estructura_generacionelectrica_2023=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2023.csv")

# Combinar todos los DataFrames
df_estructura_generacionelectrica_list = [
    df_estructura_generacionelectrica_2011, df_estructura_generacionelectrica_2012, df_estructura_generacionelectrica_2013,
    df_estructura_generacionelectrica_2014, df_estructura_generacionelectrica_2015, df_estructura_generacionelectrica_2016,
    df_estructura_generacionelectrica_2017, df_estructura_generacionelectrica_2018, df_estructura_generacionelectrica_2019,
    df_estructura_generacionelectrica_2020, df_estructura_generacionelectrica_2021, df_estructura_generacionelectrica_2022,
    df_estructura_generacionelectrica_2023
]
df_estructura_generacionelectrica_combined = pd.concat(df_estructura_generacionelectrica_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_estructura_generacionelectrica_combined['Datetime'] = pd.to_datetime(df_estructura_generacionelectrica_combined['Datetime'], utc=True)
df_estructura_generacionelectrica_combined['Datetime'] = df_estructura_generacionelectrica_combined['Datetime'].dt.strftime('%Y-%m-%d')

###############################################
#     LIMPIAR ESTRUCTURA GENERACION EMISIONES #                  
#                                             #
###############################################

#Pon laS rutas del archivo del docker
df_generacion_emisiones_2011=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2011.csv")
df_generacion_emisiones_2012=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2012.csv")
df_generacion_emisiones_2013=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2013.csv")
df_generacion_emisiones_2014=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2014.csv")
df_generacion_emisiones_2015=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2015.csv")
df_generacion_emisiones_2016=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2016.csv")
df_generacion_emisiones_2017=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2017.csv")
df_generacion_emisiones_2018=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2018.csv")
df_generacion_emisiones_2019=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2019.csv")
df_generacion_emisiones_2020=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2020.csv")
df_generacion_emisiones_2021=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2021.csv")
df_generacion_emisiones_2022=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2022.csv")
df_generacion_emisiones_2023=pd.read_csv("./data1/data_es_generacion_estructura-generacion-emisiones-asociadas_2023.csv")

# Combinar todos los DataFrames
df_generacion_emisiones_list = [
    df_generacion_emisiones_2011, df_generacion_emisiones_2012, df_generacion_emisiones_2013,
    df_generacion_emisiones_2014, df_generacion_emisiones_2015, df_generacion_emisiones_2016,
    df_generacion_emisiones_2017, df_generacion_emisiones_2018, df_generacion_emisiones_2019,
    df_generacion_emisiones_2020, df_generacion_emisiones_2021, df_generacion_emisiones_2022,
    df_generacion_emisiones_2023
]
df_generacion_emisiones_combined = pd.concat(df_generacion_emisiones_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_generacion_emisiones_combined['Datetime'] = pd.to_datetime(df_generacion_emisiones_combined['Datetime'], utc=True)
df_generacion_emisiones_combined['Datetime'] = df_generacion_emisiones_combined['Datetime'].dt.strftime('%Y-%m-%d')

################################################
#     LIMPIAR ESTRUCTURA GENERACION RENOVABLES #                  
#                                              #
################################################

df_generacion_renovables_2011=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2011.csv")
df_generacion_renovables_2012=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2012.csv")
df_generacion_renovables_2013=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2013.csv")
#df_generacion_renovables_2014=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2014.csv")
df_generacion_renovables_2015=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2015.csv")
df_generacion_renovables_2016=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2016.csv")
df_generacion_renovables_2017=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2017.csv")
df_generacion_renovables_2018=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2018.csv")
df_generacion_renovables_2019=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2019.csv")
df_generacion_renovables_2020=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2020.csv")
df_generacion_renovables_2021=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2021.csv")
df_generacion_renovables_2022=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2022.csv")
df_generacion_renovables_2023=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2023.csv")

# Combinar todos los DataFrames
df_generacion_renovables_list = [
    df_generacion_renovables_2011, df_generacion_renovables_2012, df_generacion_renovables_2013
    #df_generacion_renovables_2014
    ,df_generacion_renovables_2015, df_generacion_renovables_2016,
    df_generacion_renovables_2017, df_generacion_renovables_2018, df_generacion_renovables_2019,
    df_generacion_renovables_2020, df_generacion_renovables_2021, df_generacion_renovables_2022,
    df_generacion_renovables_2023
]
df_generacion_renovables_combined = pd.concat(df_generacion_renovables_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_generacion_renovables_combined['Datetime'] = pd.to_datetime(df_generacion_renovables_combined['Datetime'], utc=True)
df_generacion_renovables_combined['Datetime'] = df_generacion_renovables_combined['Datetime'].dt.strftime('%Y-%m-%d')

################################################
#     LIMPIAR ESTRUCTURA GENERACION EMISIONES  #                  
#                                              #
################################################

df_evolucion_generacion_emisiones_2014=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2014.csv")
df_evolucion_generacion_emisiones_2015=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2015.csv")
df_evolucion_generacion_emisiones_2016=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2016.csv")
df_evolucion_generacion_emisiones_2017=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2017.csv")
df_evolucion_generacion_emisiones_2018=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2018.csv")
df_evolucion_generacion_emisiones_2019=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2019.csv")
df_evolucion_generacion_emisiones_2020=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2020.csv")
df_evolucion_generacion_emisiones_2021=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2021.csv")
df_evolucion_generacion_emisiones_2022=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2022.csv")
df_evolucion_generacion_emisiones_2023=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2023.csv")

# Combinar todos los DataFrames
df_evolucion_generacion_emisiones_list = [
    df_evolucion_generacion_emisiones_2014, df_evolucion_generacion_emisiones_2015,
    df_evolucion_generacion_emisiones_2016, df_evolucion_generacion_emisiones_2017,
    df_evolucion_generacion_emisiones_2018, df_evolucion_generacion_emisiones_2019,
    df_evolucion_generacion_emisiones_2020, df_evolucion_generacion_emisiones_2021,
    df_evolucion_generacion_emisiones_2022, df_evolucion_generacion_emisiones_2023
]
df_evolucion_generacion_emisiones_combined = pd.concat(df_evolucion_generacion_emisiones_list, ignore_index=True)

# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_evolucion_generacion_emisiones_combined['Datetime'] = pd.to_datetime(df_evolucion_generacion_emisiones_combined['Datetime'], utc=True)
df_evolucion_generacion_emisiones_combined['Datetime'] = df_evolucion_generacion_emisiones_combined['Datetime'].dt.strftime('%Y-%m-%d')

#############################################################
#     LIMPIAR ESTRUCTURA GENERACION ESTRUCTURAS RENOVABLES  #                  
#                                                           #
#############################################################

df_generacion_estructura_renovables_2011=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2011.csv")
df_generacion_estructura_renovables_2012=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2012.csv")
df_generacion_estructura_renovables_2013=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2013.csv")
df_generacion_estructura_renovables_2014=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2014.csv")
df_generacion_estructura_renovables_2015=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2015.csv")
df_generacion_estructura_renovables_2016=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2016.csv")
df_generacion_estructura_renovables_2017=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2017.csv")
df_generacion_estructura_renovables_2018=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2018.csv")
df_generacion_estructura_renovables_2019=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2019.csv")
df_generacion_estructura_renovables_2020=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2020.csv")
df_generacion_estructura_renovables_2021=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2021.csv")
df_generacion_estructura_renovables_2022=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2022.csv")
df_generacion_estructura_renovables_2023=pd.read_csv("./data1/data_es_generacion_estructura-renovables_2023.csv")

# Combinar todos los DataFrames
df_generacion_estructura_renovables_list = [
    df_generacion_estructura_renovables_2011, df_generacion_estructura_renovables_2012, 
    df_generacion_estructura_renovables_2013, df_generacion_estructura_renovables_2014,
    df_generacion_estructura_renovables_2015, df_generacion_estructura_renovables_2016,
    df_generacion_estructura_renovables_2017, df_generacion_estructura_renovables_2018,
    df_generacion_estructura_renovables_2019, df_generacion_estructura_renovables_2020,
    df_generacion_estructura_renovables_2021, df_generacion_estructura_renovables_2022,
    df_generacion_estructura_renovables_2023
]

df_generacion_estructura_renovables_combined = pd.concat(df_generacion_estructura_renovables_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_generacion_estructura_renovables_combined['Datetime'] = pd.to_datetime(df_generacion_estructura_renovables_combined['Datetime'], utc=True)
df_generacion_estructura_renovables_combined['Datetime'] = df_generacion_estructura_renovables_combined['Datetime'].dt.strftime('%Y-%m-%d')

#############################################################
#    LIMPIAR GENERACION Y EVOLUCION DE EMISIONES            # 
#                                                           #                                                        
#############################################################

df_generacion_y_evolucion_emisiones_2014=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2014.csv")
df_generacion_y_evolucion_emisiones_2015=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2015.csv")
df_generacion_y_evolucion_emisiones_2016=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2016.csv")
df_generacion_y_evolucion_emisiones_2017=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2017.csv")
df_generacion_y_evolucion_emisiones_2018=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2018.csv")
df_generacion_y_evolucion_emisiones_2019=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2019.csv")
df_generacion_y_evolucion_emisiones_2020=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2020.csv")
df_generacion_y_evolucion_emisiones_2021=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2021.csv")
df_generacion_y_evolucion_emisiones_2022=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2022.csv")
df_generacion_y_evolucion_emisiones_2023=pd.read_csv("./data1/data_es_generacion_evolucion-estructura-generacion-emisiones-asociadas_2023.csv")
# Combinar todos los DataFrames
df_generacion_y_evolucion_emisiones_list = [
    df_generacion_y_evolucion_emisiones_2014, df_generacion_y_evolucion_emisiones_2015,
    df_generacion_y_evolucion_emisiones_2016, df_generacion_y_evolucion_emisiones_2017,
    df_generacion_y_evolucion_emisiones_2018, df_generacion_y_evolucion_emisiones_2019,
    df_generacion_y_evolucion_emisiones_2020, df_generacion_y_evolucion_emisiones_2021,
    df_generacion_y_evolucion_emisiones_2022, df_generacion_y_evolucion_emisiones_2023
]
df_generacion_y_evolucion_emisiones_combined = pd.concat(df_generacion_y_evolucion_emisiones_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_generacion_y_evolucion_emisiones_combined['Datetime'] = pd.to_datetime(df_generacion_y_evolucion_emisiones_combined['Datetime'], utc=True)
df_generacion_y_evolucion_emisiones_combined['Datetime'] = df_generacion_y_evolucion_emisiones_combined['Datetime'].dt.strftime('%Y-%m-%d')
#Pon laS rutas del archivo del docker
df_evolucion_generacion_no_renovable_2011=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2011.csv")
df_evolucion_generacion_no_renovable_2012=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2012.csv")
df_evolucion_generacion_no_renovable_2013=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2013.csv")
df_evolucion_generacion_no_renovable_2014=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2014.csv")
df_evolucion_generacion_no_renovable_2015=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2015.csv")
df_evolucion_generacion_no_renovable_2016=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2016.csv")
df_evolucion_generacion_no_renovable_2017=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2017.csv")
df_evolucion_generacion_no_renovable_2018=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2018.csv")
df_evolucion_generacion_no_renovable_2019=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2019.csv")
df_evolucion_generacion_no_renovable_2020=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2020.csv")
df_evolucion_generacion_no_renovable_2021=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2021.csv")
df_evolucion_generacion_no_renovable_2022=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2022.csv")
df_evolucion_generacion_no_renovable_2023=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2023.csv")
# Combinar todos los DataFrames
df_evolucion_generacion_no_renovable_list = [
    df_evolucion_generacion_no_renovable_2011, df_evolucion_generacion_no_renovable_2012,
    df_evolucion_generacion_no_renovable_2013, df_evolucion_generacion_no_renovable_2014,
    df_evolucion_generacion_no_renovable_2015, df_evolucion_generacion_no_renovable_2016,
    df_evolucion_generacion_no_renovable_2017, df_evolucion_generacion_no_renovable_2018,
    df_evolucion_generacion_no_renovable_2019, df_evolucion_generacion_no_renovable_2020,
    df_evolucion_generacion_no_renovable_2021, df_evolucion_generacion_no_renovable_2022,
    df_evolucion_generacion_no_renovable_2023
]
df_evolucion_generacion_no_renovable_combined = pd.concat(df_evolucion_generacion_no_renovable_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_evolucion_generacion_no_renovable_combined['Datetime'] = pd.to_datetime(df_evolucion_generacion_no_renovable_combined['Datetime'], utc=True)
df_evolucion_generacion_no_renovable_combined['Datetime'] = df_evolucion_generacion_no_renovable_combined['Datetime'].dt.strftime('%Y-%m-%d')

#############################################################
#    LIMPIAR Generacion y evolucion no renovables           # 
#                                                           #                                                        
#############################################################

df_emisiones_no_renovables_2011=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2011.csv")
df_emisiones_no_renovables_2012=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2012.csv")
df_emisiones_no_renovables_2013=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2013.csv")
df_emisiones_no_renovables_2014=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2014.csv")
df_emisiones_no_renovables_2015=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2015.csv")
df_emisiones_no_renovables_2016=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2016.csv")
df_emisiones_no_renovables_2017=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2017.csv")
df_emisiones_no_renovables_2018=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2018.csv")
df_emisiones_no_renovables_2019=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2019.csv")
df_emisiones_no_renovables_2020=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2020.csv")
df_emisiones_no_renovables_2021=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2021.csv")
df_emisiones_no_renovables_2022=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2022.csv")
df_emisiones_no_renovables_2023=pd.read_csv("./data1/data_es_generacion_no-renovables-detalle-emisiones-CO2_2023.csv")
# Combinar todos los DataFrames
df_emisiones_no_renovables_list = [
    df_emisiones_no_renovables_2011, df_emisiones_no_renovables_2012,
    df_emisiones_no_renovables_2013, df_emisiones_no_renovables_2014,
    df_emisiones_no_renovables_2015, df_emisiones_no_renovables_2016,
    df_emisiones_no_renovables_2017, df_emisiones_no_renovables_2018,
    df_emisiones_no_renovables_2019, df_emisiones_no_renovables_2020,
    df_emisiones_no_renovables_2021, df_emisiones_no_renovables_2022,
    df_emisiones_no_renovables_2023
]
df_emisiones_no_renovables_combined = pd.concat(df_emisiones_no_renovables_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_emisiones_no_renovables_combined['Datetime'] = pd.to_datetime(df_emisiones_no_renovables_combined['Datetime'], utc=True)
df_emisiones_no_renovables_combined['Datetime'] = df_emisiones_no_renovables_combined['Datetime'].dt.strftime('%Y-%m-%d')

#############################################################
#    LIMPIAR Generacion y evolucion no renovables           # 
#                                                           #                                                        
#############################################################

df_generacion_potencia_2015=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2015.csv")
df_generacion_potencia_2016=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2016.csv")
df_generacion_potencia_2017=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2017.csv")
df_generacion_potencia_2018=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2018.csv")
df_generacion_potencia_2019=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2019.csv")
df_generacion_potencia_2020=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2020.csv")
df_generacion_potencia_2021=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2021.csv")
df_generacion_potencia_2022=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2022.csv")
df_generacion_potencia_2023=pd.read_csv("./data1/data_es_generacion_potencia-instalada_2023.csv")

# Combinar todos los DataFrames
df_generacion_potencia_list = [
    df_generacion_potencia_2015, df_generacion_potencia_2016, df_generacion_potencia_2017,
    df_generacion_potencia_2018, df_generacion_potencia_2019, df_generacion_potencia_2020,
    df_generacion_potencia_2021, df_generacion_potencia_2022, df_generacion_potencia_2023
]
df_generacion_potencia_combined = pd.concat(df_generacion_potencia_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_generacion_potencia_combined['Datetime'] = pd.to_datetime(df_generacion_potencia_combined['Datetime'], utc=True)
df_generacion_potencia_combined['Datetime'] = df_generacion_potencia_combined['Datetime'].dt.strftime('%Y-%m-%d')

#############################################################
#    Intercambios energeticos con Andorra                   # 
#                                                           #                                                        
#############################################################

df_intercambios_energeticos_andorra_2014=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2014.csv")
df_intercambios_energeticos_andorra_2015=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2015.csv")
df_intercambios_energeticos_andorra_2016=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2016.csv")
df_intercambios_energeticos_andorra_2017=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2017.csv")
df_intercambios_energeticos_andorra_2018=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2018.csv")
df_intercambios_energeticos_andorra_2019=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2019.csv")
df_intercambios_energeticos_andorra_2020=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2020.csv")
df_intercambios_energeticos_andorra_2021=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2021.csv")
df_intercambios_energeticos_andorra_2022=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2022.csv")
df_intercambios_energeticos_andorra_2023=pd.read_csv("./data1/data_es_intercambios_andorra-frontera-programado_2023.csv")

# Combinar todos los DataFrames
df_intercambios_energeticos_andorra_list = [
    df_intercambios_energeticos_andorra_2014, df_intercambios_energeticos_andorra_2015,
    df_intercambios_energeticos_andorra_2016, df_intercambios_energeticos_andorra_2017,
    df_intercambios_energeticos_andorra_2018, df_intercambios_energeticos_andorra_2019,
    df_intercambios_energeticos_andorra_2020, df_intercambios_energeticos_andorra_2021,
    df_intercambios_energeticos_andorra_2022, df_intercambios_energeticos_andorra_2023
]
df_intercambios_energeticos_andorra_combined = pd.concat(df_intercambios_energeticos_andorra_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_intercambios_energeticos_andorra_combined['Datetime'] = pd.to_datetime(df_intercambios_energeticos_andorra_combined['Datetime'], utc=True)
df_intercambios_energeticos_andorra_combined['Datetime'] = df_intercambios_energeticos_andorra_combined['Datetime'].dt.strftime('%Y-%m-%d')

##############################################################
##    Intercambios energeticos con Baleares                  # 
##                                                           #                                                        
##############################################################

df_intercambios_energeticos_baleares_2011=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2011.csv")
df_intercambios_energeticos_baleares_2012=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2012.csv")
df_intercambios_energeticos_baleares_2013=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2013.csv")
df_intercambios_energeticos_baleares_2014=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2014.csv")
df_intercambios_energeticos_baleares_2015=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2015.csv")
df_intercambios_energeticos_baleares_2016=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2016.csv")
df_intercambios_energeticos_baleares_2017=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2017.csv")
df_intercambios_energeticos_baleares_2018=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2018.csv")
df_intercambios_energeticos_baleares_2019=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2019.csv")
df_intercambios_energeticos_baleares_2020=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2020.csv")
df_intercambios_energeticos_baleares_2021=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2021.csv")
df_intercambios_energeticos_baleares_2022=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2022.csv")
df_intercambios_energeticos_baleares_2023=pd.read_csv("./data1/data_es_intercambios_enlace-baleares_2023.csv")

# Combinar todos los DataFrames
df_intercambios_energeticos_baleares_list = [
    df_intercambios_energeticos_baleares_2011, df_intercambios_energeticos_baleares_2012,
    df_intercambios_energeticos_baleares_2013, df_intercambios_energeticos_baleares_2014,
    df_intercambios_energeticos_baleares_2015, df_intercambios_energeticos_baleares_2016,
    df_intercambios_energeticos_baleares_2017, df_intercambios_energeticos_baleares_2018,
    df_intercambios_energeticos_baleares_2019, df_intercambios_energeticos_baleares_2020,
    df_intercambios_energeticos_baleares_2021, df_intercambios_energeticos_baleares_2022,
    df_intercambios_energeticos_baleares_2023
]
df_intercambios_energeticos_baleares_combined = pd.concat(df_intercambios_energeticos_baleares_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_intercambios_energeticos_baleares_combined['Datetime'] = pd.to_datetime(df_intercambios_energeticos_baleares_combined['Datetime'], utc=True)
df_intercambios_energeticos_baleares_combined['Datetime'] = df_intercambios_energeticos_baleares_combined['Datetime'].dt.strftime('%Y-%m-%d')

##############################################################
##    Intercambios energeticos con Francia                   # 
##                                                           #                                                        
##############################################################

df_intercambios_energeticos_francia_2014=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2014.csv")
df_intercambios_energeticos_francia_2015=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2015.csv")
df_intercambios_energeticos_francia_2016=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2016.csv")
df_intercambios_energeticos_francia_2017=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2017.csv")
df_intercambios_energeticos_francia_2018=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2018.csv")
df_intercambios_energeticos_francia_2019=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2019.csv")
df_intercambios_energeticos_francia_2020=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2020.csv")
df_intercambios_energeticos_francia_2021=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2021.csv")
df_intercambios_energeticos_francia_2022=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2022.csv")
df_intercambios_energeticos_francia_2023=pd.read_csv("./data1/data_es_intercambios_francia-frontera-programado_2023.csv")


# Combinar todos los DataFrames
df_intercambios_energeticos_francia_list = [
    df_intercambios_energeticos_francia_2014, df_intercambios_energeticos_francia_2015,
    df_intercambios_energeticos_francia_2016, df_intercambios_energeticos_francia_2017,
    df_intercambios_energeticos_francia_2018, df_intercambios_energeticos_francia_2019,
    df_intercambios_energeticos_francia_2020, df_intercambios_energeticos_francia_2021,
    df_intercambios_energeticos_francia_2022, df_intercambios_energeticos_francia_2023
]

# Combinar todos los DataFrames
df_intercambios_energeticos_francia_combined = pd.concat(df_intercambios_energeticos_francia_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_intercambios_energeticos_francia_combined['Datetime'] = pd.to_datetime(df_intercambios_energeticos_francia_combined['Datetime'], utc=True)
df_intercambios_energeticos_francia_combined['Datetime'] = df_intercambios_energeticos_francia_combined['Datetime'].dt.strftime('%Y-%m-%d')

##############################################################
##    Intercambios energeticos Frontera                      # 
##                                                           #                                                        
##############################################################

df_intercambios_energeticos_frontera_2014=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2014.csv")
df_intercambios_energeticos_frontera_2015=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2015.csv")
df_intercambios_energeticos_frontera_2016=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2016.csv")
df_intercambios_energeticos_frontera_2017=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2017.csv")
df_intercambios_energeticos_frontera_2018=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2018.csv")
df_intercambios_energeticos_frontera_2019=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2019.csv")
df_intercambios_energeticos_frontera_2020=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2020.csv")
df_intercambios_energeticos_frontera_2021=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2021.csv")
df_intercambios_energeticos_frontera_2022=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2022.csv")
df_intercambios_energeticos_frontera_2023=pd.read_csv("./data1/data_es_intercambios_frontera-programados_2023.csv")

# Combinar todos los DataFrames
df_intercambios_energeticos_frontera_list = [
    df_intercambios_energeticos_frontera_2014, df_intercambios_energeticos_frontera_2015,
    df_intercambios_energeticos_frontera_2016, df_intercambios_energeticos_frontera_2017,
    df_intercambios_energeticos_frontera_2018, df_intercambios_energeticos_frontera_2019,
    df_intercambios_energeticos_frontera_2020, df_intercambios_energeticos_frontera_2021,
    df_intercambios_energeticos_frontera_2022, df_intercambios_energeticos_frontera_2023
]
df_intercambios_energeticos_frontera_combined = pd.concat(df_intercambios_energeticos_frontera_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_intercambios_energeticos_frontera_combined['Datetime'] = pd.to_datetime(df_intercambios_energeticos_frontera_combined['Datetime'], utc=True)
df_intercambios_energeticos_frontera_combined['Datetime'] = df_intercambios_energeticos_frontera_combined['Datetime'].dt.strftime('%Y-%m-%d')

##############################################################
##    Intercambios energeticos con Marruecos                 # 
##                                                           #                                                        
##############################################################

df_intercambios_energeticos_marruecos_2014=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2014.csv")
df_intercambios_energeticos_marruecos_2015=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2015.csv")
df_intercambios_energeticos_marruecos_2016=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2016.csv")
df_intercambios_energeticos_marruecos_2017=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2017.csv")
df_intercambios_energeticos_marruecos_2018=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2018.csv")
df_intercambios_energeticos_marruecos_2019=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2019.csv")
df_intercambios_energeticos_marruecos_2020=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2020.csv")
df_intercambios_energeticos_marruecos_2021=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2021.csv")
df_intercambios_energeticos_marruecos_2022=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2022.csv")
df_intercambios_energeticos_marruecos_2023=pd.read_csv("./data1/data_es_intercambios_marruecos-frontera-programado_2023.csv")
# Combinar todos los DataFrames
df_intercambios_energeticos_marruecos_list = [
    df_intercambios_energeticos_marruecos_2014, df_intercambios_energeticos_marruecos_2015,
    df_intercambios_energeticos_marruecos_2016, df_intercambios_energeticos_marruecos_2017,
    df_intercambios_energeticos_marruecos_2018, df_intercambios_energeticos_marruecos_2019,
    df_intercambios_energeticos_marruecos_2020, df_intercambios_energeticos_marruecos_2021,
    df_intercambios_energeticos_marruecos_2022, df_intercambios_energeticos_marruecos_2023
]
df_intercambios_energeticos_marruecos_combined = pd.concat(df_intercambios_energeticos_marruecos_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_intercambios_energeticos_marruecos_combined['Datetime'] = pd.to_datetime(df_intercambios_energeticos_marruecos_combined['Datetime'], utc=True)
df_intercambios_energeticos_marruecos_combined['Datetime'] = df_intercambios_energeticos_marruecos_combined['Datetime'].dt.strftime('%Y-%m-%d')

##############################################################
##   Limpiar  Intercambios energeticos con Portugal          # 
##                                                           #                                                        
##############################################################

df_intercambios_energeticos_portugal_2014=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2014.csv")
df_intercambios_energeticos_portugal_2015=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2015.csv")
df_intercambios_energeticos_portugal_2016=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2016.csv")
df_intercambios_energeticos_portugal_2017=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2017.csv")
df_intercambios_energeticos_portugal_2018=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2018.csv")
df_intercambios_energeticos_portugal_2019=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2019.csv")
df_intercambios_energeticos_portugal_2020=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2020.csv")
df_intercambios_energeticos_portugal_2021=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2021.csv")
df_intercambios_energeticos_portugal_2022=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2022.csv")
df_intercambios_energeticos_portugal_2023=pd.read_csv("./data1/data_es_intercambios_portugal-frontera-programado_2023.csv")

# Combinar todos los DataFrames
df_intercambios_energeticos_portugal_list = [
    df_intercambios_energeticos_portugal_2014, df_intercambios_energeticos_portugal_2015,
    df_intercambios_energeticos_portugal_2016, df_intercambios_energeticos_portugal_2017,
    df_intercambios_energeticos_portugal_2018, df_intercambios_energeticos_portugal_2019,
    df_intercambios_energeticos_portugal_2020, df_intercambios_energeticos_portugal_2021,
    df_intercambios_energeticos_portugal_2022, df_intercambios_energeticos_portugal_2023
]
df_intercambios_energeticos_portugal_combined = pd.concat(df_intercambios_energeticos_portugal_list, ignore_index=True)
# Convertir la fecha al formato de fecha estándar YYYY-MM-DD 
df_intercambios_energeticos_portugal_combined['Datetime'] = pd.to_datetime(df_intercambios_energeticos_portugal_combined['Datetime'], utc=True)
df_intercambios_energeticos_portugal_combined['Datetime'] = df_intercambios_energeticos_portugal_combined['Datetime'].dt.strftime('%Y-%m-%d')

########################################################################
#    EXPORTAR TODOS LOS DATAFRAMES LIMPIOS EN JSON                     #                                                      
########################################################################

# Ruta de salida para los archivos limpios
clean_data_folder = "./clean-data1/"
# Ruta de salida para los archivos bulk de ElasticSearch
elastic_data_folder = "./elastic-data1/"

# Crea las carpetas si no existen
os.makedirs(clean_data_folder, exist_ok=True)
os.makedirs(elastic_data_folder, exist_ok=True)

# DataFrames a exportar
dataframes = {
    "df_balance_energetico": df_balance_energetico,
    "df_demanda_evolucion": df_demanda_evolucion,
    "df_precios_mercado": df_precios_mercado,
    "combined_evolucion_demanda": combined_evolucion_demanda,
    "df_perdidas_transporte_combined": df_perdidas_transporte_combined,
    "df_laboralidad_combined": df_laboralidad_combined,
    "df_temperatura_combined": df_temperatura_combined,
    "df_demanda_corregida_combined": df_demanda_corregida_combined,
    "df_estructura_generacionelectrica_combined": df_estructura_generacionelectrica_combined,
    "df_generacion_emisiones_combined": df_generacion_emisiones_combined,
    "df_generacion_renovables_combined": df_generacion_renovables_combined,
    "df_evolucion_generacion_emisiones_combined": df_evolucion_generacion_emisiones_combined,
    "df_generacion_estructura_renovables_combined": df_generacion_estructura_renovables_combined,
    "df_generacion_y_evolucion_emisiones_combined": df_generacion_y_evolucion_emisiones_combined,
    "df_evolucion_generacion_no_renovable_combined": df_evolucion_generacion_no_renovable_combined,
    "df_emisiones_no_renovables_combined": df_emisiones_no_renovables_combined,
    "df_generacion_potencia_combined": df_generacion_potencia_combined,
    "df_intercambios_energeticos_andorra_combined": df_intercambios_energeticos_andorra_combined,
    "df_intercambios_energeticos_baleares_combined": df_intercambios_energeticos_baleares_combined,
    "df_intercambios_energeticos_francia_combined": df_intercambios_energeticos_francia_combined,
    "df_intercambios_energeticos_frontera_combined": df_intercambios_energeticos_frontera_combined,
    "df_intercambios_energeticos_marruecos_combined": df_intercambios_energeticos_marruecos_combined,
    "df_intercambios_energeticos_portugal_combined": df_intercambios_energeticos_portugal_combined
}

# Paso 1: Exportar DataFrames a JSON (clean data)
for nombre, dataframe in dataframes.items():
    try:
        # Ruta para los datos limpios
        ruta_json_clean = os.path.join(clean_data_folder, f"{nombre}.json")
        # Exportar a JSON
        dataframe.to_json(ruta_json_clean, orient="records", lines=True, force_ascii=False)
        print(f"Exportado: {nombre} a {ruta_json_clean}")
    except Exception as e:
        print(f"Error al exportar {nombre}: {e}")

# Paso 2: Convertir los archivos JSON a formato bulk para ElasticSearch
for file_name in os.listdir(clean_data_folder):
    if file_name.endswith(".json"):
        input_file = os.path.join(clean_data_folder, file_name)
        output_file = os.path.join(elastic_data_folder, f"bulk_{file_name}")
        
        try:
            with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
                for line in infile:
                    # Carga el documento JSON y escribe en formato bulk
                    doc = json.loads(line)
                    metadata = {"index": {"_index": file_name.replace(".json", "")}}  # Usa el nombre del archivo como índice
                    outfile.write(json.dumps(metadata) + "\n")
                    outfile.write(json.dumps(doc) + "\n")
            print(f"Archivo procesado y guardado como {output_file}")
        except Exception as e:
            print(f"Error al procesar {file_name}: {e}")

print("Exportacion y conversion a formato bulk completadas.")