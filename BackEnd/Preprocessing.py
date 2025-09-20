#Do this later from Data import Data
from scipy.signal import butter, filtfilt

def bandpass_filter(eeg, low=1, high=50, fs=256):
    b, a = butter(4, [low/(fs/2), high/(fs/2)], btype='band')
    return filtfilt(b, a, eeg, axis=0)


