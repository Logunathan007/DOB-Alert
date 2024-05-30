from flask import Flask,jsonify,request
from flask_cors import CORS
from db_connection import *;

app = Flask(__name__,)
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

@app.route('/addnew',methods=['POST'])
def add():
    d = request.get_json();
    print(d)
    name = ""
    dob = ""
    info = ""
    for k,v in d.items():
        if(k == 'name'):
            name = v;
        elif(k == 'dob'):
            ls = v.split('-');
            ls[0],ls[2] = ls[2],ls[0]
            dob = '-'.join(ls);
        else:
            info += k+": "+v+"_"
    insert_new_data(name,dob,info);
    return jsonify({'result':True})

if __name__ == '__main__':
    app.run(debug=True)
