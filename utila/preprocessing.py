import numpy as np

def preprocess_vitals(vitals):
    # Normalize vitals for model input
    hr = vitals['heart_rate'] / 200
    temp = vitals['temperature'] / 50
    bp = vitals['blood_pressure'] / 200
    return np.array([hr, temp, bp])
