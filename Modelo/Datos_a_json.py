import pandas as pd
df=pd.read_csv('Consumo_Energetico_Viviendas_Historico_Completo.csv')

nombre_archivo_json = 'Consumo_Energetico_Viviendas_Historico_Completo.json'
df.to_json(nombre_archivo_json, orient='records', lines=True)