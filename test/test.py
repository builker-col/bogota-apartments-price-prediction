import requests
import humanize

# URL de tu API local
url = 'http://localhost:5501/chapinero/predict'  # Asegúrate de que esta URL coincida con la dirección de tu API

# Datos de ejemplo para la solicitud POST
data = {
    'area': 63.92,
    'habitaciones': 2,
    'banos': 2,
    'parqueaderos': 1,
    'estrato': 4,
    'antiguedad': 'ENTRE 10 Y 20 ANOS', 
    'gimnasio': 0,
    'direccion': 'Carrera 7 # 39 - 19',
    'estacion_tm_cercana': 'MARLY'
}

# Realizar la solicitud POST a la API
response = requests.post(url, json=data)

# Verificar la respuesta de la API
if response.status_code == 200:
    prediction = response.json()['prediction']
    # print(f'La predicción de precio para el apartamento es: {prediction}')
    print(f'La predicción de precio para el apartamento es: {humanize.intcomma(int(prediction))}')
else:
    print(f'Error al hacer la solicitud: {response.status_code}, {response.json()}')
