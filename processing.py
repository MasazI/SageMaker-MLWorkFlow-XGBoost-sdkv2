input_file = '/opt/ml/processing/input/churn.txt';
train_file = '/opt/ml/processing/output/data/train.csv'
validation_file = '/opt/ml/processing/output/data/validation.csv'
test_file = '/opt/ml/processing/output/data/test.csv'

import pandas as pd
import numpy as np
churn = pd.read_csv(input_file)
churn = churn.drop('Phone', axis=1)
churn['Area Code'] = churn['Area Code'].astype(object)
churn = churn.drop(['Day Charge', 'Eve Charge', 'Night Charge', 'Intl Charge'], axis=1)
model_data = pd.get_dummies(churn)
model_data = pd.concat([model_data['Churn?_True.'], model_data.drop(['Churn?_False.', 'Churn?_True.'], axis=1)], axis=1)

train_data, validation_data, test_data = np.split(model_data.sample(frac=1, random_state=1729), [int(0.7 * len(model_data)), int(0.9 * len(model_data))])
train_data.to_csv(train_file, header=False, index=False)
validation_data.to_csv(validation_file, header=False, index=False)
test_data.to_csv(test_file, header=False, index=False)