from flask import Flask, jsonify, request
from io import StringIO
import csv
import requests

data = None #liht global var, hiljem vaja

def fetch_data():
    url = "https://github.com/timotr/harjutused/raw/refs/heads/main/hajusrakendused/LE.txt"

    response = requests.get(url)

    fake_file = StringIO(response.text) #Selleks, et see järgmine command töötaks
    _data = csv.DictReader(fake_file, delimiter="\t") #CSV formaadist ära objectiks ja delimiter selleks, et täpsustada kuda andmed eraldatud

    return list(_data)

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    global data #See vajalik, et see mälus oleks
    data = fetch_data()
    return "Data olemas" #Flask kahtlane ja vajab, et see returniks midagi
    

@app.route('/', methods = ["GET", "POST"])
def home():
    page = []
    for row in range(30):
        page.append(data[row])
    return jsonify(page)

app.run()   