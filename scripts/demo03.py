from sklearn import svm

training_data = [[0, 0], [1, 1]]
labels = [0, 1]
clf = svm.SVC()
clf.fit(training_data, labels)
print(clf)


new_datapoint = [2, 4]

print(clf.predict([new_datapoint]))

new_datapoint = [-2, -1]
print(clf.predict([new_datapoint]))

import matplotlib.pyplot as plt

from sklearn import svm
from sklearn.datasets import make_blobs
from sklearn.inspection import DecisionBoundaryDisplay

# we create 40 separable points
X, y = make_blobs(n_samples=10, centers=2, random_state=6)

i=0
while i<len(X):
    print("POINT:", X[i])
    print("Label:", y[i])
    print()
    i = i+1


plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
plt.show()


# fit the model, don't regularize for illustration purposes
clf = svm.SVC(kernel="linear")
clf.fit(X, y)

plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)

# plot the decision function
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
# plot support vectors
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()