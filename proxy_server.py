from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Ruta para obtener el JSON de la API de www.dolarsi.com
@app.route('/dolar', methods=['GET'])
def get_dolar():
    # URL de la API de www.dolarsi.com
    url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    try:
        # Hacer una petición GET a la URL de la API
        response = requests.get(url)
        # Obtener el JSON de la respuesta
        data = response.json()
        # Devolver el JSON obtenido
        return jsonify(data)
    except Exception as e:
        # Si ocurre algún error, devolver un JSON con el mensaje de error y un código de estado 500
        return jsonify({'error': str(e)}), 500

# Ruta para obtener un tipo específico de dolar
@app.route('/dolar/<string:dolar_type>', methods=['GET'])
def get_specific_dolar(dolar_type):
    # URL de la API de www.dolarsi.com
    url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    try:
        # Hacer una petición GET a la URL de la API
        response = requests.get(url)
        # Obtener el JSON de la respuesta
        data = response.json()
        # Buscar en el JSON el tipo de dólar especificado
        for casa in data:
            if casa.get('casa', {}).get('nombre', '').lower() == dolar_type.lower():
                # Si se encuentra el tipo de dólar especificado, devolverlo
                return jsonify(casa)
        # Si no se encuentra el tipo de dólar especificado, devolver un JSON con un mensaje indicando que no se encontró y un código de estado 404
        return jsonify({'message': 'Dolar type not found'}), 404
    except Exception as e:
        # Si ocurre algún error, devolver un JSON con el mensaje de error y un código de estado 500
        return jsonify({'error': str(e)}), 500

# Si el archivo se ejecuta como script principal (es decir, si __name__ == '__main__')
if __name__ == '__main__':
    # Iniciar la aplicación Flask en el host '0.0.0.0' y en el puerto 5000
    app.run(host='0.0.0.0', port=5000)