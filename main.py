from flask import Flask, json, jsonify
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://contact-me-api-python:MongoContact-me-api-python@localhost:27017/?authSource=contact-me")
db = cluster['contact-me']
collection = db['people']

app = Flask(__name__)

def validateKey(key):
    if key == '225338242':
        return True
    else:
        return False

@app.route('/<string:key>/find')
def find(key):
    result = validateKey(key)
    if result:
        arrayResult = {}
        results = collection.find({})
        temp = 0
        for result in results:
            result.pop("_id")
            arrayResult[temp]=result
            temp += 1
        return jsonify(arrayResult)
    else:
        return "Key Error"

@app.route('/<string:key>/create/<string:email>/<string:subject>')
def create(key, email, subject):
    result = validateKey(key)
    if result:
        post = {
            'email' : email,
            'subject' : subject
        }
        collection.insert_one(post)
        return "Done"
    else:
        return "Key Error"

@app.route('/<string:key>/delete/<string:email>')
def delete(key, email):
    result = validateKey(key)
    if result:
        collection.delete_one({'email' : email})
        return "Done"
    else:
        return "Key Error"

if __name__ == "__main__":
    app.run(debug=True)
