




import json
from flask import Flask, request, jsonify
from data import Deployment
import os


app = Flask(__name__)





@app.route('/',methods=['get'])
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})


@app.route('/send', methods=['post'])
def process_request():
    data = request.json
    
    prossData = Deployment()
    fianldata = prossData.request(data)
    print(data)

    return jsonify(fianldata)








if __name__ == "__main__":
    app.run(debug=False)
