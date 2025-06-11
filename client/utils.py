import joblib
import numpy as np

def load_model(filename):
    return joblib.load(filename)

def preprocess_inputs(inputs, scaler=None):
    array = np.array(inputs).reshape(1, -1)
    if scaler:
        array = scaler.transform(array)
    return array
