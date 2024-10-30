pip install requests pandas

import requests

# Definir los términos de búsqueda
search_terms = ["Google Home", "Apple TV", "Amazon Fire TV"]
item_ids = []

# Obtener los ítems para cada término de búsqueda
for term in search_terms:
    offset = 0
    while True:
        url = f"https://api.mercadolibre.com/sites/MLA/search?q={term}&limit=50&offset={offset}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            results = data['results']
            if not results:  # Si no hay más resultados, salir del bucle
                break
            for item in results:
                item_ids.append(item['id'])
            offset += 50  # Aumentar el offset para la siguiente página
        else:
            print(f"Error en la búsqueda para {term}: {response.status_code}")
            break

# Mostrar la lista de Item_Id obtenidos
print(f"Total de Item_Id obtenidos: {len(item_ids)}")
print(item_ids)

import requests
import pandas as pd

# Vamos a obtener los detalles de un ítem
def obtener_detalles_item(item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Retorna el JSON del ítem
    else:
        print(f"Error al obtener el ítem {item_id}: {response.status_code}")
        return None

# Obtener detalles de todos los ítems
detalles_items = []
for item_id in item_ids:
    detalles = obtener_detalles_item(item_id)
    if detalles:  # Solo agregar si se obtuvieron detalles
        detalles_items.append(detalles)

# Mostrar la cantidad de ítems obtenidos
print(f"Total de ítems detallados obtenidos: {len(detalles_items)}")

# Crear un DataFrame a partir de los detalles obtenidos
df_items = pd.DataFrame(detalles_items)

# Imprimir las columnas disponibles
print("Columnas disponibles en el DataFrame:")
print(df_items.columns)

# Definir las columnas que queremos
columnas_relevantes = ['id', 'title', 'price', 'condition', 'sold_quantity', 'category_id', 'available_quantity', 'currency_id']

# Filtrar solo las columnas que están disponibles
columnas_presentes = [col for col in columnas_relevantes if col in df_items.columns]

# Seleccionar solo las columnas relevantes
df_relevantes = df_items[columnas_presentes]

# Escribir el DataFrame a un archivo CSV
df_relevantes.to_csv('detalles_items.csv', index=False, encoding='utf-8')

print("Detalles de los ítems guardados en 'detalles_items.csv'.")

