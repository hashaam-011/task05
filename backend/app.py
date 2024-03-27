from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('database', 27017)  # Connect to MongoDB using the service name 'database'

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form
    db = client.mydatabase  # Change 'mydatabase' to your desired database name
    collection = db.forms   # Collection name where data will be stored
    result = collection.insert_one(data)
    return jsonify({"message": "Form submitted successfully", "id": str(result.inserted_id)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)