from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def is_match(features_new, features_stored, threshold=0.85):
    if features_stored is None or features_new is None:
        return -1

    if np.isnan(features_stored).any() or np.isnan(features_new).any():
        return 0  # treat NaNs as mismatch

    sim = cosine_similarity(features_new.reshape(1, -1), features_stored.reshape(1, -1))[0][0]

    return 1 if sim >= threshold else 0



