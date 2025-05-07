# Fit a logistic regression model
from sklearn import linear_model
X = basetable[["age","gender_F","time_since_last_gift"]]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)