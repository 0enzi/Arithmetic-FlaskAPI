import re
from flask import request, Flask, jsonify


app = Flask(__name__)

@app.route('/add', methods=["POST"])
def add():
    #GET RESOURCE
    data = request.get_json()

    #GET x and y
    x = data['x']
    y = data['y']

    #VALIDATE ENTERED INFO
    if not data["x"]:
        return "Error: Please enter both values"

    if not data['y']:
        return "Error: Please enter yboth values"

    #PERFOM TASK
    z  = {"added_result": x+y}

    #RETURN RESPONSE 
    return jsonify(z)


@app.route('/sub', methods=["POST"])
def sub():
    #GET RESOURCE
    data = request.get_json()

    #GET x and y
    x = data['x']
    y = data['y']

    
    #VALIDATE ENTERED INFO
    if not data["x"]:
        return "Error: Please enter both values"

    if not data['y']:
        return "Error: Please enter yboth values"


    #PERFOM TASK
    z  = {"subtracted_result": x-y}

    #RETURN RESPONSE 
    return jsonify(z)


@app.route('/div', methods=["POST"])
def div():
    #GET RESOURCE
    data = request.get_json()

    #GET x and y
    x = data['x']
    y = data['y']

    
    #VALIDATE ENTERED INFO
    if data['y'] == 0:
        return "Denominator cannot be equal to zero!", 302

    if not data["x"]:
        return "Error: Please enter both values"

    if not data['y']:
        return "Error: Please enter both values"

    #PERFOM TASK
    z  = {"divided_result": x/y}

    #RETURN RESPONSE 
    return jsonify(z)


@app.route('/mul', methods=["POST"])
def mul():
    #GET RESOURCE
    data = request.get_json()

    #GET x and y
    x = data['x']
    y = data['y']

    
    #VALIDATE ENTERED INFO
    if data['y'] == 0:
        return "0 Obviously", 302


    if not data["x"]:
        return "Error: Please enter both values",301

    if not data['y']:
        return "Error: Please enter yboth values",301

    #PERFOM TASK
    z  = {"multiplied_result": x*y}

    #RETURN RESPONSE 
    return jsonify(z)


app.run(host="0.0.0.0", port=4500, debug=True)