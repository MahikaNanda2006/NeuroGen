import numpy as np

channels = 8
samples = 256*10
def get_simulated_eeg():
    simulated_eeg = np.random.randn(samples, channels)
    return simulated_eeg
