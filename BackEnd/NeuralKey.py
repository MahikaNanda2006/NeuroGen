import hashlib

def generate_neural_key(features):
    feature_bytes = features.tobytes()
    key = hashlib.sha256(feature_bytes).hexdigest()
    return key


