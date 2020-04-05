from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
respuesta = {"code": 200, "desc": "OK"}

@app.route('/ping')
def  ping():
	return 'Pong'


@app.route('/sumar', methods=['POST'])
def  sumar():
	new_operacion = {
		"numeroUno": request.json['numeroUno'],
		"numeroDos": request.json['numeroDos'],
		"resultado": request.json['numeroUno'] + request.json['numeroDos']
	}
	return jsonify({"Status": respuesta,"Resultado": new_operacion})

@app.route('/restar', methods=['POST'])
def  restar():
	new_operacion = {
		"numeroUno": request.json['numeroUno'],
		"numeroDos": request.json['numeroDos'],
		"resultado": request.json['numeroUno'] - request.json['numeroDos']
	}
	return jsonify({"Status": respuesta,"Resultado": new_operacion})

@app.route('/multiplicar', methods=['POST'])
def  multiplicar():
	new_operacion = {
		"numeroUno": request.json['numeroUno'],
		"numeroDos": request.json['numeroDos'],
		"resultado": request.json['numeroUno'] * request.json['numeroDos']
	}
	return jsonify({"Status": respuesta,"Resultado": new_operacion})

@app.route('/dividir', methods=['POST'])
def  dividir():
	new_operacion = {
		"numeroUno": request.json['numeroUno'],
		"numeroDos": request.json['numeroDos'],
		"resultado": request.json['numeroUno'] / request.json['numeroDos']
	}
	return jsonify({"Status": respuesta,"Resultado": new_operacion})


if __name__ == '__main__':
	app.run(debug=True, port = 4000)