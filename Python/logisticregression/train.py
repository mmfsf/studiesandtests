from sklearn.datasets import load_iris
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print '### Features ###'
print iris.feature_names
print '...\n\n'

features_train, features_test, target_train, target_test = train_test_split(df[iris.feature_names], iris.target, train_size = .8)

cls = LogisticRegression(n_jobs=20)

cls.fit(features_train, target_train)
predictions = cls.predict(features_test)
print '### confusion matrix ###'
print confusion_matrix(predictions, target_test)
print "...\n\n"

preds_names = iris.target_names[cls.predict(features_test)]
test_names = iris.target_names[target_test]
print "### Result of the classifier (Predicted type of iris plant vs the actual plant type) ###\n"
print pd.crosstab(test_names, preds_names, rownames=['actual'], colnames=['preds'])

print "\n\nSave model to the directory model_storage..."
joblib.dump(cls, 'model_storage/model.pkl')
print "Save test data to the file test_data.csv..."
features_test['target'] = test_names
features_test.to_csv('test_data.csv', index = False)