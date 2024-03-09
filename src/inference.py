from joblib import dump, load
import pandas as pd
import numpy as np
from .data_processor import log_txf

def get_prediction(**kwargs):
    clf = load('models/mdl.joblib')
    features = load('models/raw_features.joblib')
    pred_df = pd.DataFrame(kwargs, index=[0])
    pred_df = log_txf(pred_df, ['yearly_income'])
    pred = clf.predict(pred_df[features])
    return pred[0]
