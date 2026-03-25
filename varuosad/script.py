from flask import Flask, jsonify, request
from io import StringIO
import csv
import requests

data = None #liht global var, hiljem vaja

def fetch_data():
    url = "https://github.com/timotr/harjutused/raw/refs/heads/main/hajusrakendused/LE.txt"

    response = requests.get(url)

    fake_file = StringIO(response.text) #Selleks, et see järgmine command töötaks
    fieldnames = [
        "id",
        "nimi",
        "midagi 1",
        "midagi 2",
        "midagi 3",
        "midagi 4",
        "midagi 5",
        "midagi 6",
        "midagi 7",
        "midagi 8",
        "midagi 9",
        "midagi 10",
        "midagi 11",
    ]
    _data = csv.DictReader(
        fake_file, 
        delimiter="\t",
        fieldnames=fieldnames
    ) #CSV formaadist ära objectiks ja delimiter selleks, et täpsustada kuda andmed eraldatud

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
    print(page)
    return jsonify(page)

app.run()   