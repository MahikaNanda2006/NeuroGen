import numpy as np
def extract_features(eeg):
    # Statistical features per channel
    mean = np.mean(eeg, axis=0)
    std = np.std(eeg, axis=0)
    var = np.var(eeg, axis=0)
    # Flatten features
    features = np.concatenate([mean, std, var])
    return features
#Add to main when it is necessary

