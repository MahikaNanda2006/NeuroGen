# main.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import time
from BackEnd import Preprocessing, FeatureExtraction, NeuralKey, Comparison
from Data import Datass
from Storage_demo import db_handler


def main():
    def create_a_neural_key(i):
        # Step 0: Load simulated EEG
        print("[INFO] Loading simulated EEG...")
        eeg = Datass.get_simulated_eeg()
        time.sleep(1)
        print(f"[INFO] EEG shape: {eeg.shape}\n")

        # Step 1: Preprocessing
        print("[STEP 1] Preprocessing EEG...")
        eeg_pre = Preprocessing.bandpass_filter(eeg)
        time.sleep(0.5)
        print("[INFO] Preprocessing complete.\n")

        # Step 2: Feature Extraction
        print("[STEP 2] Extracting Features...")
        features = FeatureExtraction.extract_features(eeg_pre)
        print(f"[INFO] Features shape: {features.shape}\n")
        time.sleep(0.5)
        return features

            # Step 3: Generate Neural Key
            #print("[STEP 3] Generating Neural Key...")
            #key = NeuralKey.generate_neural_key(features)
            
            
            #print(f"[INFO] Neural Key: {key[:10]}... (truncated)\n")

            #time.sleep(0.5)
    def authenticate(user_id, neural_key_input):
        print("[STEP 4] Authenticating...")

        result = db_handler.verify_neural_key(user_id, neural_key_input)
        print (result)

        if result == -1:
            print("[ACCESS DENIED ❌] User does not exist")
        elif result == 0:
            print("[ACCESS DENIED ❌] Neural key does not match")
        elif result == 1:
            print("[ACCESS GRANTED ✅]")
    print("=== NeuroShield Prototype Demo ===\n")
    flag = int(input("Do you wish to save keys or check authentication?"))
    if flag == 1:
        x = int(input("Enter how many neural keys you would like to save"))
        db_handler.create_table()
        for i in range(x):
            features = create_a_neural_key(i)
            print("User ", i, "Was stored")
            db_handler.save_neural_key(i+1, features)
    elif flag == 2:
        z = int(input("Would you like to check the key?"))
        if z == 1:
            id = int(input("Enter the user ID"))
            key = create_a_neural_key(1)
            authenticate(id, key)
        else:
            exit()


if __name__ == "__main__":
    main()
