from flask import Flask, jsonify, request
from io import StringIO
import csv
import requests

data = None #liht global var, hiljem vaja
page_count = 30 #Mitu asja 1 lehel

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
        "hind",
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
    current_page = request.args.get("page")
    name = request.args.get("name")
    id = request.args.get("id")
    page = []
    if name and id:
        for i in range(len(data)):
            if data[i]["nimi"] == name and data[i]["id"] == id:
                page.append(data[i])
            if i >= page_count:
                break
    elif name:
        for i in range(len(data)):
            if data[i]["nimi"] == name:
                page.append(data[i])
            if i >= page_count:
                break
    elif id: 
        for i in range(len(data)):
            if data[i]["id"] == id:
                page.append(data[i])
            if i >= page_count:
                break
    elif current_page and not id and not name:
        for row in range(page_count):
            page.append(data[row + int(current_page) * page_count])
    else:
        for row in range(page_count):
            page.append(data[row])
    
    page.sort(key=lambda x: x["hind"])
    return jsonify(page)

app.run()   