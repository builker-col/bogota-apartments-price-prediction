from dotenv import load_dotenv
import pandas as pd
import requests
import re
import os

load_dotenv()

def search_estation_by_name(name):
    """
    Searches for a station by name in the TransMilenio system.

    Args:
        name (str): The name of the station to search for.

    Returns:
        dict: A dictionary containing the name of the station and its coordinates if found, or a message if not found.
    """
    response = requests.get('https://gis.transmilenio.gov.co/arcgis/rest/services/Troncal/consulta_estaciones_troncales/FeatureServer/1/query?where=1%3D1&outFields=*&f=json').json()
    troncal_transmilenio = pd.DataFrame(response['features'])
    troncal_transmilenio = pd.json_normalize(troncal_transmilenio['attributes'])
    
    name = name.upper()
    name = name.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U').replace('Ñ', 'N').replace('AVENIDA', 'AV.')

    troncal_transmilenio['nombre_estacion'] = troncal_transmilenio['nombre_estacion'].apply(lambda x: x.upper())
    troncal_transmilenio['nombre_estacion'] = troncal_transmilenio['nombre_estacion'].astype(str).apply(lambda x: x.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U').replace('Ñ', 'N') if pd.notnull(x) else x)

    regex = re.compile(f'.*{name}.*')
    for i in troncal_transmilenio['nombre_estacion']:
        if re.match(regex, i):
            return {'name': i, 'coordinates': (troncal_transmilenio[troncal_transmilenio['nombre_estacion'] == i]['latitud_estacion'].values.tolist()[0], troncal_transmilenio[troncal_transmilenio['nombre_estacion'] == i]['latitud_estacion'].values.tolist()[0])}
    return {'message': 'Estación no encontrada'}

def havesine_distance(origin, destination):
    """
    Calculate the Haversine distance between two points on the Earth's surface.

    Parameters:
    origin (tuple): A tuple containing the latitude and longitude of the origin point.
    destination (tuple): A tuple containing the latitude and longitude of the destination point.

    Returns:
    float: The distance between the origin and destination points in meters.
    """
    import math

    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371000 # meters

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

def get_coordinates(address: str):
    """
    Retrieves the latitude and longitude coordinates for a given address using the Google Geocoding API.

    Args:
        address (str): The address to geocode.

    Returns:
        tuple: A tuple containing the latitude and longitude coordinates of the address.

    Raises:
        None

    """
    # URL base de la API de Geocodificación de Google
    url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Parámetros de la solicitud
    params = {
        'address': address,
        'key': os.getenv('GOOGLE_MAPS_TOKEN')
    }

    # Realizar la solicitud GET a la API
    response = requests.get(url, params=params)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        data = response.json()
        
        # Verificar si se encontró una ubicación
        if data['status'] == 'OK':
            # Obtener las coordenadas de la primera ubicación encontrada
            latitud = data['results'][0]['geometry']['location']['lat']
            longitud = data['results'][0]['geometry']['location']['lng']
            
            return latitud, longitud
        else:
            print('No se encontró la ubicación.')
    else:
        print('Error en la solicitud:', response.status_code)

def get_distance_station(station_name: str, address: str) -> float:
    """
    Calculates the distance between a given address and a given station.

    Args:
        station_name (str): The name of the station to calculate the distance to.
        address (str): The address to calculate the distance from.

    Returns:
        float: The distance between the address and the station in meters.

    Raises:
        None

    """
    station = search_estation_by_name(station_name)
    if 'message' in station:
        return station['message']
    else:
        station_coordinates = station['coordinates']
        address_coordinates = get_coordinates(address)
        distance = havesine_distance(station_coordinates, address_coordinates)
        return distance