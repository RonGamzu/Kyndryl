from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)


try:
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb+srv://RonGamzu:1234@cluster0.ajspk.mongodb.net/Kyndryl?retryWrites=true&w=majority'
    }
    db = MongoEngine(app)
except:
    print('ERROR - Cannot connect to db')


class Users(db.Document):
    id = db.SequenceField(primary_key=True)
    first_name = db.StringField(required=True, min_length=2, max_length=30)
    last_name = db.StringField(required=True, min_length=2, max_length=30)
    id_number = db.IntField(required=True, min_value=1000, unique=True)


@app.route('/addUser', methods=["POST"])
def add_user():
    userDetails = request.get_json()
    if userDetails['firstName'].strip() == "" or userDetails['lastName'].strip() == "":
        return 'Please enter a valid full name', 505
    if int(userDetails['idNumber']) < 1000:
        return 'Please enter a valid id number', 505
    try:
        user = Users(first_name=userDetails['firstName'],
                     last_name=userDetails['lastName'], id_number=userDetails['idNumber']).save()
        return jsonify(user), 201
    except:
        return 'ERROR - something got wrong', 404


@app.route('/users', methods=['GET'])
def getAllUsers():
    try:
        users = Users.objects()
        return jsonify(users), 201
    except:
        return 'Something got wrong', 404

##################################
if __name__ == "__main__":
    app.run(port=80, debug=False)


