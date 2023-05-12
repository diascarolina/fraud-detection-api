import pickle
import math
import os
import pandas as pd
import pytest

model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'app/modelo/modelo.pkl')
model = pickle.load(open(model_path, 'rb'))



def test_predictions():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/test_data.csv')
    df = pd.read_csv(path)
    expected_result = df["Class"]

    df["preds"] = model.predict(df.drop("Class", axis=1))

    for i, predict_value in enumerate(df["preds"]):
            assert math.isclose(predict_value,
                float(expected_result[i]),
                rel_tol=0.01), f"A predição {i} tem valor esperado {expected_result[i]}, mas retornou {predict_value}"
