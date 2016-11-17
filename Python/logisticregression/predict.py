from sklearn.datasets import load_iris
from sklearn.externals import joblib
import pandas as pd

iris = load_iris()
cls = joblib.load('model_storage/model.pkl')
test = pd.read_csv('test_data.csv')
features = test.columns[:4]
test['preds'] = iris.target_names[cls.predict(test[features])]
print test