from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
import time
# source venv/bin/activate
# sudo fuser -k 5000/tcp

app = Flask(__name__)
CORS(app)

data_bichinho = {
    "nome": "BoB",
    "saude": 100,
    "comida": 100,
    "felicidade": 100,
    "energia": 100,
    "idade": 0
}


def isnumber(value):
    try:
        float(value)
    except:
        return False
    return True

def verifica_valores():
    for i, j in data_bichinho.items():
        if isnumber(j):
            if j>100:
                data_bichinho[i] = 100
            if j<0:
                data_bichinho[i] = 0
        


@app.route('/status', methods=['GET'])
def obter_dados():
        return jsonify(data_bichinho)

@app.route('/food', methods=['PUT'])
def food():
    data_bichinho["comida"] = data_bichinho["comida"] + 20
    data_bichinho["energia"] = data_bichinho["energia"] + 15
    data_bichinho["felicidade"] = data_bichinho["felicidade"] + 7
    verifica_valores()
    return jsonify(data_bichinho);

@app.route('/play', methods=['PUT'])
def play():
    data_bichinho["energia"] = data_bichinho["energia"] - 20
    data_bichinho["felicidade"] = data_bichinho["felicidade"] + 20
    data_bichinho["comida"] = data_bichinho["comida"] - 15
    verifica_valores()
    return jsonify(data_bichinho);

@app.route('/sleep', methods=['PUT'])
def sleep():
    data_bichinho["energia"] = 100
    data_bichinho["comida"] = data_bichinho["comida"] - 20
    data_bichinho["saude"] = data_bichinho["saude"] + 30
    verifica_valores()
    return jsonify(data_bichinho);

@app.route('/medicine', methods=['PUT'])
def medicine():
    data_bichinho["saude"] = data_bichinho["saude"] + 40
    verifica_valores()
    return jsonify(data_bichinho);


def tempo_atributos():
    segundos=0
    while True:
        if data_bichinho["saude"] == 0:
            return
        time.sleep(1)
        segundos+=1
        if segundos%15 == 0:
            data_bichinho["felicidade"] -= 1
            data_bichinho["comida"] -= 2
        if segundos%30 == 0:
            data_bichinho["energia"] -= 1
            data_bichinho["saude"] -= 2
        if(segundos%60 == 0):
            data_bichinho["idade"] += 1


if __name__ == "__main__":
    tread_tempo = threading.Thread(target=tempo_atributos)
    tread_tempo.start()
    app.run(debug=True)

