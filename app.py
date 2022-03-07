
from flask import Flask, jsonify, request

app = Flask()

@app.route('/imc', methods=['GET'])
def calcularIMC():
    peso = float(request.args.get('peso'))
    altura = float(request.args.get('altura'))
    resultado = peso/(altura*altura)
    return jsonify({"value",resultado})
    
@app.route('/igc', methods=['GET'])
def calcularIGC():
    cint = float(request.args.get('cint')) 
    altura = float(request.args.get('alt'))
    resultado = cint/(altura*(altura**(0.5)))
    return jsonify({"value",resultado})


@app.route('/calorias', methods=['GET'])
def calcularCalorias():
    peso = float(request.args.get('peso'))
    distancia = float(request.args.get('distancia'))
    resultado = 1.03*peso*distancia
    return jsonify({"value",resultado})


if __name__ == '__main__':
    app.run(debug=True)















