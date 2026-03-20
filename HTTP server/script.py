from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def home():
    query_params = request.args
    body_type = request.content_type
    body = request.get_data()
    print(str(query_params) + "\n" + str(body_type) + "\n" + str(body.decode()))
    return query_params

app.run()   