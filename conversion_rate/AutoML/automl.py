import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML

df = pd.read_csv(
    "conversion_data_train.csv",
    # skipinitialspace=True,
)
target_variable = 'converted'
Y = df.loc[:, target_variable]
X = df.drop(target_variable, axis=1)


X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2
)

automl = AutoML()
automl.fit(X_train, y_train)

predictions = automl.predict(X_test)