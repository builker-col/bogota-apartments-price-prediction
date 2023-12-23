from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from joblib import load
import pandas as pd
import json

from src import auxiliar_functions as aux

app = Flask(__name__)
api = Api(app)
CORS(app)
            
class ChapineroRegression(Resource):
    def get(self):
        with open('models/chapinero/info.json') as json_file:
            data = json.load(json_file)

        return data, 200
    
    def post(self, model_type = 'rf'):
        if model_type == 'rf':
            model = load('models/chapinero/rf.joblib')
            model_without_coord = load('models/chapinero/rf_without_coords.joblib')
        elif model_type == 'ln':
            model = load('models/chapinero/ln.joblib')
            model_without_coord = load('models/chapinero/ln_without_coords.joblib')
        elif model_type == 'knn':
            model = load('models/chapinero/knn.joblib')
            model_without_coord = load('models/chapinero/knn_without_coords.joblib')
        
        data = request.get_json()
        if 'latitud' in data and 'longitud' in data:
            pass
        else:
            if type(data['antiguedad']) == str:
                if data['antiguedad'] not in ['ENTRE 0 Y 5 ANOS', 'ENTRE 10 Y 20 ANOS', 'ENTRE 5 Y 10 ANOS', 'MAS DE 20 ANOS', 'REMODELADO']:
                    return {'message': 'La antigüedad ingresada por el usuario no se encuentra en ningún rango conocido.'}, 400
                else:
                    antiguedad_categoria = data['antiguedad']
                    antiguedad_categoria = aux.get_antiguedad_class(antiguedad_categoria)
            else:
                usuario_antiguedad_anos = int(data['antiguedad'])
                antiguedad_categoria = aux.get_antiguedad_categoria(usuario_antiguedad_anos)
                antiguedad_categoria = aux.get_antiguedad_class(antiguedad_categoria)

            if antiguedad_categoria is not None:
                # Realizar la predicción y convertir el resultado a una lista
                prediction = model_without_coord.predict(pd.DataFrame({'area': [data['area']], 'habitaciones': [data['habitaciones']], 'banos': [data['banos']], 'parqueaderos': [data['parqueaderos']], 'estrato': [data['estrato']], 'antiguedad': [antiguedad_categoria], 'gimnasio': [data['gimnasio']]}))
                prediction_list = prediction.tolist()

                return {'prediction': prediction_list[0]}, 200
            else:
                return {'message': 'La antigüedad ingresada por el usuario no se encuentra en ningún rango conocido.'}, 400
    
api.add_resource(ChapineroRegression, '/chapinero/predict', '/chapinero/<string:model_type>/predict')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5501)