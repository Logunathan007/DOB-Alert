from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/verify',methods=['POST'])
def verify():
    data = [{
        'name':'logu',
        'password':'logu'
    }]
    name = request.get_json()['name']
    password = request.get_json()['password'];
    for i in data:
        if(i['name'] == name and i['password'] == password):
            return jsonify({'result':True})
    return jsonify({'result':False})

if __name__ == '__main__':
    app.run(debug=True)
