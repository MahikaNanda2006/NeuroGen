# simple in-memory storage for demo
demo_storage = {}

def create_table():
    pass  # not needed in demo

def save_neural_key(user_id, features):
    demo_storage[user_id] = features.tolist()  # store in memory

def verify_neural_key(user_id, features_new):
    features_stored = demo_storage.get(user_id, None)  # check if user exists
    if features_stored is None:
        return -1  # User Not Found ⚠️

    # Compare features (cosine similarity)
    import numpy as np
    from BackEnd import Comparison

    features_stored = np.array(features_stored)
    return Comparison.is_match(features_new, features_stored, 0.85)
