# https://xavierbourretsicotte.github.io/LDA_QDA.html


from sklearn.inspection import PartialDependenceDisplay
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB


X,y = load_iris(return_X_y=True, as_frame=True)

clf_boost = HistGradientBoostingClassifier().fit(X,y)
clf_qda = QuadraticDiscriminantAnalysis().fit(X, y)
clf_logit = LogisticRegression().fit(X, y)
clf_lda = LinearDiscriminantAnalysis().fit(X, y)
clf_nb = GaussianNB().fit(X, y)


from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(2).fit_transform(X)
clf_ldaq = LinearDiscriminantAnalysis().fit(poly, y)
clf_logitq = LogisticRegression().fit(poly, y)

features = [0,1,2,3]

plt.clf()
PartialDependenceDisplay.from_estimator(clf_boost, X, features, target=2)
plt.title("Boosting")
plt.show()

plt.clf()
PartialDependenceDisplay.from_estimator(clf_qda, X, features, target=2)
plt.title("QDA")
plt.show()

plt.clf()
PartialDependenceDisplay.from_estimator(clf_ldaq, poly, features, target=2)
plt.title("LDAq")
plt.show()


plt.clf()
PartialDependenceDisplay.from_estimator(clf_lda, X, features, target=2)
plt.title("LDA")
plt.show()

plt.clf()
PartialDependenceDisplay.from_estimator(clf_logit, X, features, target=2)
plt.title("Logit")
plt.show()

plt.clf()
PartialDependenceDisplay.from_estimator(clf_nb, X, features, target=2)
plt.title("NB")
plt.show()


import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
iris = load_iris()
X = iris.data[:, :2]
classifier = QuadraticDiscriminantAnalysis().fit(X, iris.target)
disp = DecisionBoundaryDisplay.from_estimator(
    classifier, X, response_method="predict",
    xlabel=iris.feature_names[0], ylabel=iris.feature_names[1],
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=iris.target, edgecolor="k")
plt.show()

