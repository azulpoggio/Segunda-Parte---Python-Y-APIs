import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('detalles_items.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Resumen estadístico de los datos
print(df.describe())

#Verificamos datos faltantes
print(df.isnull().sum())

#Histograma de la distribución de precios
import matplotlib.pyplot as plt

plt.hist(df['price'], bins=20)
plt.title('Distribución de precios')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.show()