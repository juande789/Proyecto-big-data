import os
import requests
import csv
import time
from datetime import datetime, timedelta
# ========================================================
# Función para obtener datos de la API de REE (Balance Eléctrico)
# ========================================================
def obtener_datos_balance(year, month):
    url = f'https://apidatos.ree.es/es/datos/balance/balance-electrico?start_date={year}-{month:02d}-01T00:00&end_date={year}-{month:02d}-28T23:59&time_trunc=day'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code} al obtener datos de balance eléctrico para {year}-{month:02d}")
        return None

# ========================================================
# Función para guardar los datos de Balance Eléctrico en un archivo CSV
# ========================================================
def guardar_datos_balance(data, folder="./data1/", filename="balance_energia.csv"):
    # Crear la carpeta si no existe
    os.makedirs(folder, exist_ok=True)
    # Ruta completa del archivo
    file_path = os.path.join(folder, filename)
    
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Escribe el encabezado solo si el archivo está vacío
        if file.tell() == 0:
            writer.writerow(["date", "type", "value", "percentage"])
        
        for record in data.get('included', []):
            for entry in record['attributes']['content']:
                title = entry['attributes']['title']
                for value_entry in entry['attributes']['values']:
                    date = value_entry['datetime']
                    value = value_entry['value']
                    percentage = value_entry.get('percentage', 'N/A')
                    writer.writerow([date, title, value, percentage])

# ========================================================
# Función para obtener datos de la API de REE (Evolución de Demanda)
# ========================================================
def obtener_datos_demanda(year, month):
    url = f'https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={year}-{month:02d}-01T00:00&end_date={year}-{month:02d}-28T23:59&time_trunc=day'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code} al obtener datos de demanda para {year}-{month:02d}")
        return None

# ========================================================
# Función para obtener datos de la API de REE (Evolución de Demanda)
# ========================================================
def obtener_datos_demanda(year, month):
    url = f'https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={year}-{month:02d}-01T00:00&end_date={year}-{month:02d}-28T23:59&time_trunc=day'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code} al obtener datos de demanda para {year}-{month:02d}")
        return None

def guardar_datos_demanda(data, year, month, filename_prefix="./data1/demanda_evolucion"):
    filename = f"{filename_prefix}_{year}_{month:02d}.csv"
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["date", "value", "percentage"])

        if 'included' in data:
            for record in data['included']:
                if 'attributes' in record and 'values' in record['attributes']:
                    values = record['attributes']['values']
                    for value_entry in values:
                        date = value_entry.get('datetime', 'N/A')
                        value = value_entry.get('value', 'N/A')
                        percentage = value_entry.get('percentage', 'N/A')
                        writer.writerow([date, value, percentage])
# ========================================================
# Función para obtener datos de la API de REE (Precios de Mercado)
# ========================================================
def obtener_datos_precios(year, month, day):
    url = f'https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date={year}-{month:02d}-{day:02d}T00:00&end_date={year}-{month:02d}-{day:02d}T23:59&time_trunc=hour'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code} al obtener datos de precios para {year}-{month:02d}-{day:02d}")
        return None
    
# Función para guardar los datos obtenidos en un archivo CSV

def guardar_datos_precios(data, year, month, filename_prefix="./data1/precios_mercado"):
    # Verificar y crear la carpeta si no existe
    folder_path = os.path.dirname(filename_prefix)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Directorio creado: {folder_path}")
    
    # Crear el nombre del archivo
    filename = f"{filename_prefix}_{year}_{month:02d}.csv"
    
    # Escribir los datos en el archivo CSV
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Escribir encabezado solo si el archivo está vacío
        if file.tell() == 0:
            writer.writerow(["date", "title", "value", "percentage"])
        
        # Procesar y escribir los datos
        if 'included' in data:
            for record in data['included']:
                if 'attributes' in record:
                    attributes = record['attributes']
                    title = attributes.get('title', 'N/A')
                    if 'values' in attributes:
                        for value_entry in attributes['values']:
                            date = value_entry.get('datetime', 'N/A')
                            value = value_entry.get('value', 'N/A')
                            percentage = value_entry.get('percentage', 'N/A')
                            writer.writerow([date, title, value, percentage])

# ========================================================
# Función para descargar datos adicionales de la API
# ========================================================
def datos_adiconales(
    lang='es',
    base_url_template='https://apidatos.ree.es/{}/datos/{}/{}',
    start_year=2007,
    end_year=2023,
    categories_widgets=None
):
    """
    Descarga datos desde la API de Red Eléctrica de España y los guarda en archivos CSV dentro de la carpeta 'data1'.
    
    Parámetros:
        lang (str): Idioma de los datos. Por defecto 'es'.
        base_url_template (str): Plantilla de la URL base para la API.
        start_year (int): Año inicial para la consulta.
        end_year (int): Año final para la consulta.
        categories_widgets (list): Lista de tuplas (categoría, widget) para consultar.
    """
    # Crear la carpeta 'data1' si no existe
    if not os.path.exists('./data1/'):
        os.makedirs('./data1/')

    if categories_widgets is None:
        categories_widgets = []

    for category, widget in categories_widgets:
        url = base_url_template.format(lang, category, widget)

        for year in range(start_year, end_year + 1):
            start_date = f'{year}-01-01T00:00'
            end_date = f'{year}-12-31T23:59'

            current_year = datetime.now().year
            current_date = datetime.now().strftime('%Y-%m-%dT%H:%M')
            if year == current_year:
                end_date = current_date

            params = {
                'start_date': start_date,
                'end_date': end_date,
                'time_trunc': 'day',
                'geo_trunc': 'electric_system',
                'geo_limit': 'peninsular',
                'geo_ids': '8741'
            }

            response = requests.get(url, params=params)

            if response.status_code == 200:
                print(f'Solicitud exitosa para {category}/{widget} en {year}.')
                data = response.json()
            else:
                print(f'Error en {category}/{widget} para el año {year}: {response.status_code}')
                print(response.text)
                continue

            csv_filename = os.path.join('./data1/', f'data_{lang}_{category}_{widget}_{year}.csv')
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Indicator', 'Datetime', 'Value']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for indicator in data.get('included', []):
                    attributes = indicator.get('attributes', {})
                    title = attributes.get('title', 'No Title')

                    if 'values' in attributes:
                        values = attributes.get('values', [])
                        for value_entry in values:
                            datetime_str = value_entry.get('datetime')
                            value = value_entry.get('value')
                            writer.writerow({
                                'Indicator': title,
                                'Datetime': datetime_str,
                                'Value': value
                            })

            print(f'Datos de {category}/{widget} para {year} guardados en {csv_filename}.\n')
# ========================================================
# Bucle principal para iterar por año y mes y descargar datos
# ========================================================
if __name__ == "__main__":

    #Descargar datos de precios del mercado
    print("Iniciando descarga de datos de Precios de Mercado...")
    for year in range(2014, 2023):  # Cambia los años según sea necesario
        for month in range(1, 13):   # Iterar de enero a diciembre
            start_date = datetime(year, month, 1)
            end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            current_date = start_date
    
            while current_date <= end_date:
                day = current_date.day
                print(f"Obteniendo datos de Precios de Mercado para {year}-{month:02d}-{day:02d}")
                datos_precios = obtener_datos_precios(year, month, day)
                if datos_precios:
                    guardar_datos_precios(datos_precios, year, month)
                current_date += timedelta(days=1)
                time.sleep(1)  # Respetar un retraso entre solicitudes
    print("Descarga de datos de Precios de Mercado finalizada.\n")

    # Descargar datos de balance eléctrico
    print("Iniciando descarga de datos de Balance Electrico...")
    for year in range(2019, 2023):
        for month in range(1, 13):
            print(f"Obteniendo datos de Balance Electrico para {year}-{month:02d}")
            datos_balance = obtener_datos_balance(year, month)
            if datos_balance:
                guardar_datos_balance(datos_balance)
            time.sleep(1)
    print("Descarga de datos de Balance Electrico finalizada.\n")
    
    # Descargar datos de evolución de demanda
    print("Iniciando descarga de datos de Evolucion de Demanda...")
    for year in range(2013, 2024):
        for month in range(1, 13):
            print(f"Obteniendo datos de Evolucion de Demanda para {year}-{month:02d}")
            datos_demanda = obtener_datos_demanda(year, month)
            if datos_demanda:
                guardar_datos_demanda(datos_demanda, year, month)
            time.sleep(1)
    print("Descarga de datos de Evolucion de Demanda finalizada.")

    # Uso de la función para descargar datos adicionales
    print("Iniciando descarga de datos adicionales con función generalizada...")
    categories_widgets = [
        ('balance', 'balance-electrico'),
        ('demanda', 'evolucion'),
        ('demanda', 'variacion-componentes'),
        ('demanda', 'variacion-componentes-movil'),
        ('demanda', 'ire-general'),
        ('demanda', 'ire-general-anual'),
        ('demanda', 'ire-general-movil'),
        ('demanda', 'ire-industria'),
        ('demanda', 'ire-industria-anual'),
        ('demanda', 'ire-industria-movil'),
        ('demanda', 'ire-servicios'),
        ('demanda', 'ire-servicios-anual'),
        ('demanda', 'ire-servicios-movil'),
        ('demanda', 'ire-otras'),
        ('demanda', 'ire-otras-anual'),
        ('demanda', 'ire-otras-movil'),
        ('demanda', 'demanda-maxima-diaria'),
        ('demanda', 'demanda-maxima-horaria'),
        ('demanda', 'perdidas-transporte'),
        ('demanda', 'potencia-maxima-instantanea'),
        ('demanda', 'variacion-demanda'),
        ('demanda', 'potencia-maxima-instantanea-variacion'),
        ('demanda', 'potencia-maxima-instantanea-variacion-historico'),
        ('demanda', 'demanda-tiempo-real'),
        ('demanda', 'variacion-componentes-anual'),
        ('generacion', 'estructura-renovables'),
        ('generacion', 'estructura-generacion-emisiones-asociadas'),
        ('generacion', 'evolucion-estructura-generacion-emisiones-asociadas'),
        ('generacion', 'no-renovables-detalle-emisiones-CO2'),
        ('generacion', 'maxima-renovable'),
        ('generacion', 'potencia-instalada'),
        ('generacion', 'maxima-renovable-historico'),
        ('generacion', 'maxima-sin-emisiones-historico'),
        ('intercambios', 'francia-frontera'),
        ('intercambios', 'portugal-frontera'),
        ('intercambios', 'marruecos-frontera'),
        ('intercambios', 'andorra-frontera'),
        ('intercambios', 'lineas-francia'),
        ('intercambios', 'lineas-portugal'),
        ('intercambios', 'lineas-marruecos'),
        ('intercambios', 'lineas-andorra'),
        ('intercambios', 'francia-frontera-programado'),
        ('intercambios', 'portugal-frontera-programado'),
        ('intercambios', 'marruecos-frontera-programado'),
        ('intercambios', 'andorra-frontera-programado'),
        ('intercambios', 'enlace-baleares'),
        ('intercambios', 'frontera-fisicos'),
        ('intercambios', 'todas-fronteras-fisicos'),
        ('intercambios', 'frontera-programados'),
        ('intercambios', 'todas-fronteras-programados'),
        ('transporte', 'energia-no-suministrada-ens'),
        ('transporte', 'indice-indisponibilidad'),
        ('transporte', 'tiempo-interrupcion-medio-tim'),
        ('transporte', 'kilometros-lineas'),
        ('transporte', 'indice-disponibilidad'),
        ('transporte', 'numero-cortes'),
        ('transporte', 'ens-tim'),
        ('transporte', 'indice-disponibilidad-total'),
        ('mercados', 'componentes-precio-energia-cierre-desglose'),
        ('mercados', 'componentes-precio'),
        ('mercados', 'energia-gestionada-servicios-ajuste'),
        ('mercados', 'energia-restricciones'),
        ('mercados', 'precios-restricciones'),
        ('mercados', 'reserva-potencia-adicional'),
        ('mercados', 'banda-regulacion-secundaria'),
        ('mercados', 'energia-precios-regulacion-secundaria'),
        ('mercados', 'energia-precios-regulacion-terciaria'),
        ('mercados', 'energia-precios-gestion-desvios'),
        ('mercados', 'coste-servicios-ajuste'),
        ('mercados', 'volumen-energia-servicios-ajuste-variacion'),
        ('mercados', 'precios-mercados-tiempo-real'),
        ('mercados', 'energia-precios-ponderados-gestion-desvios-before'),
        ('mercados', 'energia-precios-ponderados-gestion-desvios'),
        ('mercados', 'energia-precios-ponderados-gestion-desvios-after')
    ]

    try:
        datos_adiconales(
            lang='es',
            start_year=2007,
            end_year=2023,
            categories_widgets=categories_widgets
        )
    except Exception as e:
        print(f"Error en la descarga de datos adicionales: {e}")
    print("Descarga de datos adicionales finalizada.")
