import requests
from flask import jsonify

url = "http://localhost:80/addUser"


def unitTest(data):
    response = requests.post(url, json=data)
    user = response.json()
    return user


# Expecting to get: {'first_name': 'Ron', 'id_number': 120985678, 'last_name': 'Gamzu'}
print(unitTest({"firstName": "Ron",
                "lastName": "Gamzu",
                "idNumber": "120985678"}))

# Expecting to get: {'first_name': 'EITIEL', 'id_number': 101001010, 'last_name': 'Jobs'}
print(unitTest({"firstName": "EITIEL",
                "lastName": "Jobs",
                "idNumber": "101001010"}))
