{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b1d2fed7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in ./opt/anaconda3/lib/python3.9/site-packages (2.28.1)\n",
      "Requirement already satisfied: pandas in ./opt/anaconda3/lib/python3.9/site-packages (1.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (3.3)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (2.0.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (1.26.13)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in ./opt/anaconda3/lib/python3.9/site-packages (from requests) (2024.8.30)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in ./opt/anaconda3/lib/python3.9/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in ./opt/anaconda3/lib/python3.9/site-packages (from pandas) (2022.1)\n",
      "Requirement already satisfied: numpy>=1.18.5 in ./opt/anaconda3/lib/python3.9/site-packages (from pandas) (1.21.5)\n",
      "Requirement already satisfied: six>=1.5 in ./opt/anaconda3/lib/python3.9/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b85a23fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total de Item_Id obtenidos: 335\n",
      "['MLA1448342367', 'MLA1135498793', 'MLA1616758962', 'MLA1426601681', 'MLA1398793543', 'MLA1616759000', 'MLA1597574484', 'MLA1398767505', 'MLA1384134643', 'MLA1597677286', 'MLA916372672', 'MLA763380836', 'MLA1398755255', 'MLA1398845395', 'MLA930506223', 'MLA1400539531', 'MLA1785182142', 'MLA1597470910', 'MLA1110314122', 'MLA1597677282', 'MLA1110377590', 'MLA1448891827', 'MLA1683844336', 'MLA1398832615', 'MLA1597677284', 'MLA1400506527', 'MLA1452498123', 'MLA1597457958', 'MLA1452420859', 'MLA833417329', 'MLA1398845475', 'MLA912014012', 'MLA1456652579', 'MLA1928125454', 'MLA1443012353', 'MLA1930441108', 'MLA1432622907', 'MLA1364551668', 'MLA1456415339', 'MLA1361515563', 'MLA1432597373', 'MLA1361528507', 'MLA1422239063', 'MLA1437520249', 'MLA1892733826', 'MLA1416430677', 'MLA1820484428', 'MLA1436571213', 'MLA1930440916', 'MLA1807784940', 'MLA1450805011', 'MLA1452528853', 'MLA1569955706', 'MLA1939932266', 'MLA1933589706', 'MLA1448244479', 'MLA1447363539', 'MLA1916055982', 'MLA1412480803', 'MLA1447237225', 'MLA1854015610', 'MLA1618186704', 'MLA1934024052', 'MLA1366426083', 'MLA1449403463', 'MLA1594852796', 'MLA1399215546', 'MLA1936729268', 'MLA1719499042', 'MLA1618134776', 'MLA1378227377', 'MLA1426291701', 'MLA1806378888', 'MLA1377244881', 'MLA1449909446', 'MLA1924987444', 'MLA1457807717', 'MLA1905654296', 'MLA1457565557', 'MLA1400247011', 'MLA1904940598', 'MLA1925001440', 'MLA1877356464', 'MLA1942285402', 'MLA1911254292', 'MLA1781884668', 'MLA1938835060', 'MLA1399520644', 'MLA1933079400', 'MLA1447987851', 'MLA1933604596', 'MLA1436930383', 'MLA1946353708', 'MLA1433276905', 'MLA1913427140', 'MLA1931246390', 'MLA1454231967', 'MLA1443682603', 'MLA1799086010', 'MLA1837941502', 'MLA1414122791', 'MLA1925114644', 'MLA1794555584', 'MLA1445793563', 'MLA1913452572', 'MLA1408440613', 'MLA1133058175', 'MLA1443250893', 'MLA1844813002', 'MLA1903134622', 'MLA1111206110', 'MLA1436028141', 'MLA1822817324', 'MLA1111243533', 'MLA1189756455', 'MLA1451784141', 'MLA935560782', 'MLA1448835555', 'MLA1670324528', 'MLA1867521508', 'MLA1428080643', 'MLA1426077727', 'MLA1677887932', 'MLA1455795215', 'MLA1946508156', 'MLA1446598647', 'MLA1938425710', 'MLA1456872275', 'MLA1899194696', 'MLA1447521627', 'MLA1900086302', 'MLA1913825834', 'MLA1934617232', 'MLA1916581512', 'MLA1452952571', 'MLA1928185834', 'MLA1922572798', 'MLA1453212713', 'MLA1456277103', 'MLA1454761719', 'MLA1929076010', 'MLA1944219284', 'MLA1920529838', 'MLA1448806077', 'MLA1913923014', 'MLA1391230655', 'MLA1872960642', 'MLA1929064936', 'MLA1944238836', 'MLA1317267791', 'MLA1451719249', 'MLA1813667360', 'MLA1897081278', 'MLA1917664572', 'MLA1443460083', 'MLA1434538437', 'MLA1457976495', 'MLA1419331631', 'MLA1438665381', 'MLA1448716455', 'MLA879375937', 'MLA924796800', 'MLA1434473587', 'MLA1434551091', 'MLA1451465451', 'MLA1454896289', 'MLA1447771371', 'MLA1850845602', 'MLA1813226356', 'MLA1341381358', 'MLA1925824046', 'MLA1909575060', 'MLA1364216697', 'MLA1626492828', 'MLA1862240494', 'MLA1943089676', 'MLA1451611825', 'MLA1455405423', 'MLA1940780266', 'MLA1901602976', 'MLA1937931438', 'MLA1376700509', 'MLA1916062622', 'MLA1890341728', 'MLA1144084762', 'MLA1456925617', 'MLA1374336916', 'MLA1117800874', 'MLA1372865557', 'MLA1856299012', 'MLA1920570096', 'MLA1869562272', 'MLA1920505416', 'MLA1787834792', 'MLA1447682463', 'MLA1403888993', 'MLA1114934662', 'MLA1440621335', 'MLA1391355057', 'MLA1373073449', 'MLA1369051919', 'MLA1751007286', 'MLA1403353954', 'MLA1440239591', 'MLA1937833012', 'MLA1413017321', 'MLA1449794463', 'MLA1716970254', 'MLA1275869904', 'MLA1138176179', 'MLA1916498408', 'MLA1436049559', 'MLA1143409979', 'MLA1868644730', 'MLA1143429135', 'MLA1441306967', 'MLA1453203257', 'MLA1373149393', 'MLA1441654143', 'MLA1450338037', 'MLA1359581075', 'MLA1412833394', 'MLA1800170008', 'MLA1917670470', 'MLA1438372841', 'MLA1429044047', 'MLA1920492052', 'MLA1166920743', 'MLA1788560204', 'MLA1275677195', 'MLA1448063231', 'MLA1117755386', 'MLA1449931871', 'MLA1144078429', 'MLA1875994450', 'MLA1448851429', 'MLA1901997240', 'MLA1937768208', 'MLA1391504537', 'MLA1916511586', 'MLA1933602550', 'MLA1936830218', 'MLA1890305194', 'MLA1906907810', 'MLA1449919051', 'MLA759387281', 'MLA1451204361', 'MLA1913040380', 'MLA1449944953', 'MLA1940515494', 'MLA1444420275', 'MLA1457634563', 'MLA1449766059', 'MLA1143410892', 'MLA1451305263', 'MLA1452410449', 'MLA1451757853', 'MLA1142197777', 'MLA1439824889', 'MLA1916498696', 'MLA1916575524', 'MLA1937940182', 'MLA1718061952', 'MLA1935301882', 'MLA1417499719', 'MLA1439837937', 'MLA1286072659', 'MLA1943103482', 'MLA1404718091', 'MLA1214656893', 'MLA1442434039', 'MLA1440301179', 'MLA1143423103', 'MLA1214650470', 'MLA1403370075', 'MLA1875995546', 'MLA1458435638', 'MLA1413082105', 'MLA1919003788', 'MLA1454877931', 'MLA1134829983', 'MLA1429948205', 'MLA1913813546', 'MLA1440556697', 'MLA1341348681', 'MLA1437940615', 'MLA1440608919', 'MLA1439607369', 'MLA1174670102', 'MLA1122850533', 'MLA1457369511', 'MLA1149652512', 'MLA1403331045', 'MLA1138064125', 'MLA1114918626', 'MLA1454479419', 'MLA1440266209', 'MLA1451731391', 'MLA1441294233', 'MLA1394486515', 'MLA1451861395', 'MLA1788560300', 'MLA1441280211', 'MLA1944678926', 'MLA1445191887', 'MLA1894776226', 'MLA1453083943', 'MLA1916259828', 'MLA1446309787', 'MLA1473218924', 'MLA1942279552', 'MLA1454402185', 'MLA1456507343', 'MLA1890470052', 'MLA1894879970', 'MLA1936732176', 'MLA1441602455', 'MLA1876047202', 'MLA1876008746', 'MLA1414835553', 'MLA1876098748', 'MLA1450586715', 'MLA874503353', 'MLA1839169318', 'MLA1548431302', 'MLA1442744693', 'MLA1473649132', 'MLA1446432849', 'MLA1446722649', 'MLA1930417022', 'MLA1456177985', 'MLA1940892644', 'MLA1446646313', 'MLA1447463009', 'MLA1933961680']\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# Definir los términos de búsqueda\n",
    "search_terms = [\"Google Home\", \"Apple TV\", \"Amazon Fire TV\"]\n",
    "item_ids = []\n",
    "\n",
    "# Obtener los ítems para cada término de búsqueda\n",
    "for term in search_terms:\n",
    "    offset = 0\n",
    "    while True:\n",
    "        url = f\"https://api.mercadolibre.com/sites/MLA/search?q={term}&limit=50&offset={offset}\"\n",
    "        response = requests.get(url)\n",
    "        if response.status_code == 200:\n",
    "            data = response.json()\n",
    "            results = data['results']\n",
    "            if not results:  # Si no hay más resultados, salir del bucle\n",
    "                break\n",
    "            for item in results:\n",
    "                item_ids.append(item['id'])\n",
    "            offset += 50  # Aumentar el offset para la siguiente página\n",
    "        else:\n",
    "            print(f\"Error en la búsqueda para {term}: {response.status_code}\")\n",
    "            break\n",
    "\n",
    "# Mostrar la lista de Item_Id obtenidos\n",
    "print(f\"Total de Item_Id obtenidos: {len(item_ids)}\")\n",
    "print(item_ids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f7e29124",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total de ítems detallados obtenidos: 335\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "\n",
    "# Vamos a obtener los detalles de un ítem\n",
    "def obtener_detalles_item(item_id):\n",
    "    url = f\"https://api.mercadolibre.com/items/{item_id}\"\n",
    "    response = requests.get(url)\n",
    "    if response.status_code == 200:\n",
    "        return response.json()  # Retorna el JSON del ítem\n",
    "    else:\n",
    "        print(f\"Error al obtener el ítem {item_id}: {response.status_code}\")\n",
    "        return None\n",
    "\n",
    "# Obtener detalles de todos los ítems\n",
    "detalles_items = []\n",
    "for item_id in item_ids:\n",
    "    detalles = obtener_detalles_item(item_id)\n",
    "    if detalles:  # Solo agregar si se obtuvieron detalles\n",
    "        detalles_items.append(detalles)\n",
    "\n",
    "# Mostrar la cantidad de ítems obtenidos\n",
    "print(f\"Total de ítems detallados obtenidos: {len(detalles_items)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ab3bf81a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Columnas disponibles en el DataFrame:\n",
      "Index(['id', 'site_id', 'title', 'seller_id', 'category_id',\n",
      "       'official_store_id', 'price', 'base_price', 'original_price',\n",
      "       'currency_id', 'initial_quantity', 'sale_terms', 'buying_mode',\n",
      "       'listing_type_id', 'condition', 'permalink', 'thumbnail_id',\n",
      "       'thumbnail', 'pictures', 'video_id', 'descriptions',\n",
      "       'accepts_mercadopago', 'non_mercado_pago_payment_methods', 'shipping',\n",
      "       'international_delivery_mode', 'seller_address', 'seller_contact',\n",
      "       'location', 'coverage_areas', 'attributes', 'listing_source',\n",
      "       'variations', 'status', 'sub_status', 'tags', 'warranty',\n",
      "       'catalog_product_id', 'domain_id', 'parent_item_id', 'deal_ids',\n",
      "       'automatic_relist', 'date_created', 'last_updated', 'health',\n",
      "       'catalog_listing'],\n",
      "      dtype='object')\n",
      "Detalles de los ítems guardados en 'detalles_items.csv'.\n"
     ]
    }
   ],
   "source": [
    "# Crear un DataFrame a partir de los detalles obtenidos\n",
    "df_items = pd.DataFrame(detalles_items)\n",
    "\n",
    "# Imprimir las columnas disponibles\n",
    "print(\"Columnas disponibles en el DataFrame:\")\n",
    "print(df_items.columns)\n",
    "\n",
    "# Definir las columnas que queremos\n",
    "columnas_relevantes = ['id', 'title', 'price', 'condition', 'sold_quantity', 'category_id', 'available_quantity', 'currency_id']\n",
    "\n",
    "# Filtrar solo las columnas que están disponibles\n",
    "columnas_presentes = [col for col in columnas_relevantes if col in df_items.columns]\n",
    "\n",
    "# Seleccionar solo las columnas relevantes\n",
    "df_relevantes = df_items[columnas_presentes]\n",
    "\n",
    "# Escribir el DataFrame a un archivo CSV\n",
    "df_relevantes.to_csv('detalles_items.csv', index=False, encoding='utf-8')\n",
    "\n",
    "print(\"Detalles de los ítems guardados en 'detalles_items.csv'.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ac36f14",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
