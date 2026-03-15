import os
import joblib
import numpy as np

def model_pred(amb_temp, mod_temp, time_enc, irr):

    # Load the trained model
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'finalized_model.pkl')
    model = joblib.load(model_path)

    # Extract input data from the form
    new_data = np.array([int(amb_temp) , int(mod_temp), int(time_enc) , float(irr)]).reshape(1, -1)
    print(new_data)

    # Perform prediction
    predicted_yield = model.predict(new_data)[0]

    return predicted_yield