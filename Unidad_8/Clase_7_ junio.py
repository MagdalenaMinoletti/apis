#Crear APIs

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])



def person():

    rsp= {
        'id': 123,
        'name': 'Edgard',
        'is_alive': True,
        'favorite_sport': ['cycling','tennis','swimming'],
        'graduated': None
    }

    return rsp

person()