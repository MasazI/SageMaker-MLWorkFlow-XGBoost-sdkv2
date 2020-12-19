import os
import tarfile
import pickle
import numpy as np
import xgboost
import pandas as pd
from sklearn import metrics

if __name__ == "__main__":
    model_path = os.path.join("/opt/ml/processing/model", "model.tar.gz")
    test_path = os.path.join("/opt/ml/processing/input", "test.csv")
    output_path = os.path.join("/opt/ml/processing/evaluation", "result.txt")
    print("Extracting model from path: {}".format(model_path))
    with tarfile.open(model_path) as tar:
        tar.extractall(path=".")
    print("Loading model")
    model = pickle.load(open('xgboost-model', 'rb'))

    print("Loading test input data")
    test_data = pd.read_csv(test_path)
    dtest = test_data.values
    
    print("Evaluating")
    test_dm = xgboost.DMatrix(test_data.values[:, 1:])
    predictions_xgb = model.predict(test_dm)
    
    score = metrics.accuracy_score(test_data.iloc[:, 0].values, np.round(predictions_xgb))
    print(score)
    
    with open(output_path, 'w') as f:
        f.write(score)
        f.write('\n')