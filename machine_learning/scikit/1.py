# https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

# ['target', 'DESCR', 'feature_names', 'target_filename', 'data', 'data_filename']
# print(diabetes.keys())
# print(diabetes.data)

diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X_train = diabetes_X[:-30]
diabetes_X_test  = diabetes_X[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_predicted = model.predict(diabetes_X_test)

print("Mean Squared Error", mean_squared_error(diabetes_y_test, diabetes_y_predicted))
print("Weights ", model.coef_)
print("Intercepts", model.intercept_)

plt.scatter(diabetes_X_test, diabetes_y_test)
plt.plot(diabetes_X_test, diabetes_y_predicted)
plt.show()