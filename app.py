from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
import base64
import os
import numpy as np
import subprocess
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime


app = Flask(__name__)
CORS(app) 

@app.route('/upload/<prod>', methods=['POST']) 
def Upload(prod):  
    try:
        img = request.files.get('image')

        if not os.path.exists('data'):
            os.makedirs('data')
        
        img.save(os.path.join('data', prod+'.last'))
        
        val = open(os.path.join('data', prod+'.val'), 'w')
        val.write(request.form.get('value'))
        val.close()
        
        # arquivo = open('arquivo.txt', 'w')
        # arquivo.write(valor_do_input)
        # arquivo.close()

        return jsonify('true')
    except:
        return jsonify('false')


@app.route('/GetData', methods=['GET']) 
def getData():  
    resp = ''  
    try:
        file = open('./data/cp.last', 'rb')
        imgCP = file.read()
        file = open('./data/ki.last', 'rb')
        imgKI = file.read()
        file = open('./data/li.last', 'rb')
        imgLI = file.read()
        file = open('./data/tt.last', 'rb')
        imgTT = file.read()
        file = open('./data/si.last', 'rb')
        imgSI = file.read()
        file = open('./data/cp.val', 'r')
        valCP = file.read()
        file = open('./data/ki.val', 'r')
        valKI = file.read()
        file = open('./data/li.val', 'r')
        valLI = file.read()
        file = open('./data/tt.val', 'r')
        valTT = file.read()
        file = open('./data/si.val', 'r')
        valSI = file.read()
        resp = {
            'time': datetime.now().time().strftime('%H:%M'),
            'cp':{ 'img': base64.b64encode(imgCP).decode('utf-8'), 'val': valCP },
            'ki':{ 'img': base64.b64encode(imgKI).decode('utf-8'), 'val': valKI },
            'li':{ 'img': base64.b64encode(imgLI).decode('utf-8'), 'val': valLI },
            'tt':{ 'img': base64.b64encode(imgTT).decode('utf-8'), 'val': valTT },
            'si':{ 'img': base64.b64encode(imgSI).decode('utf-8'), 'val': valSI }    
        }
    except Exception as e:
         print(e)
    
    finally:
        return jsonify(resp)



if __name__ == '__main__':
    app.run(debug=True)
