import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, request, jsonify
from BackEnd import Preprocessing, FeatureExtraction, Comparison
from flask_cors import CORS  
from Storage_demo import db_handler
import numpy as np

app = Flask(__name__)
CORS(app) 

@app.route("/api/save", methods=["POST"])
def save_key():
    data = request.get_json()
    user_id = data["user_id"]
    eeg = np.array(data["eeg"])
    eeg_pre = Preprocessing.bandpass_filter(eeg)
    features = FeatureExtraction.extract_features(eeg_pre)
    db_handler.create_table()
    db_handler.save_neural_key(user_id, features)
    return jsonify({"status": "saved"})

@app.route("/api/verify", methods=["POST"])
def verify_key():
    data = request.get_json()
    user_id = data["user_id"]
    eeg = np.array(data["eeg"])
    eeg_pre = Preprocessing.bandpass_filter(eeg)
    features = FeatureExtraction.extract_features(eeg_pre)
    match = db_handler.verify_neural_key(user_id, features)
    return jsonify({"match": match})

if __name__ == "__main__":
    app.run(port=5000)
