from flask import Flask, json, jsonify
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://abled:MongoRoot3241@cluster0.fcmer.mongodb.net/person?retryWrites=true&w=majority")
db = cluster['person']
collection = db['content']

app = Flask(__name__)

@app.route('/find')
def find():
    arrayResult = []
    results = collection.find({})
    for result in results:
        result.pop("_id")
        arrayResult.append(result)
    return jsonify(arrayResult)

@app.route('/create/<string:email>/<string:subject>')
def create(email, subject):
    post = {
        'email' : email,
        'subject' : subject
    }
    collection.insert_one(post)
    return "Done"

@app.route('/delete/<string:email>')
def delete(email):
    collection.delete_one({'email' : email})
    return "Done"

if __name__ == "__main__":
    app.run(debug=True)