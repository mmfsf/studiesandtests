# http://jvns.ca/blog/2014/11/17/fun-with-machine-learning-logistic-regression/
import pandas as pd
import numpy as np
# Generate 100,000 data points normally distributed 
# with mean 0 and variance 1
# Our features are called 'panda' and 'elephant'.
dataset = pd.DataFrame({
    'panda': np.random.normal(0, 1, 100000),
    'elephant': np.random.normal(0, 1, 100000)
})
# The coefficients we're using are -1/3 * panda - 1/3 * elephant
x = - 1/3 * (dataset['panda'] +  dataset['elephant'])
# Put everything through the logistic function
probabilities = 1 / (1 + np.exp(-1 * x))
print probabilities
# A trick! np.random.uniform(0,1) < 0.7 is 1 with 
# probability 70% and 0 with probability 30%
dataset['target'] = np.random.uniform(0,1, 100000) < probabilities
print dataset.target.value_counts()
# Check that the target values are roughly evenly distributed
# True     50032
# False    49968

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
cls = LogisticRegression()
features = dataset[['elephant', 'panda']]
target = dataset['target']
features_train, features_test, target_train, target_test = train_test_split(features, target)
cls.fit(features_train, target_train)
predictions = cls.predict(features_test)
print confusion_matrix(predictions, target_test)

import matplotlib.pyplot as plt
# Plot outputs
# trues = dataset[['elephant', 'panda']][target][:500]
# falses = dataset[['elephant', 'panda']][~target][:500]
# ax = plt.axes()
# trues.plot(x='elephant', y='panda', kind='scatter', ax=ax, alpha=0.6, label='True')
# falses.plot(x='elephant', y='panda', kind='scatter', color='orange', ax=ax, alpha=0.6, label='False')
# plt.legend()

# plt.show()

# trues['elephant'] -= 1
# trues['panda'] -= 1
# ax = plt.axes()
# trues.plot(x='elephant', y='panda', kind='scatter', ax=ax, alpha=0.6, label='True')
# falses.plot(x='elephant', y='panda', kind='scatter', color='orange', ax=ax, alpha=0.6, label='False')
# plt.legend()

# plt.show()

test_df = pd.DataFrame(features_test, columns=['panda', 'elephant'])
trues = test_df[['elephant', 'panda']][predictions][:500]
falses = test_df[['elephant', 'panda']][~predictions][:500]
ax = plt.axes()
trues.plot(x='elephant', y='panda', kind='scatter', ax=ax, alpha=0.6, label='True')
falses.plot(x='elephant', y='panda', kind='scatter', color='orange', ax=ax, alpha=0.6, label='False')
plt.legend()

plt.show()