# Program 3 — MNIST (LogReg, SVM, RF)

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("Train:", X_train.shape[0], "samples Test:", X_test.shape[0], "samples")

X_train = X_train.reshape(-1, 784) / 255.0
X_test = X_test.reshape(-1, 784) / 255.0

X_train_svm = X_train[:10000]
y_train_svm = y_train[:10000]

logreg = LogisticRegression(max_iter=1000)
svm = SVC(kernel='rbf')
rf = RandomForestClassifier()

logreg.fit(X_train, y_train)
svm.fit(X_train_svm, y_train_svm)
rf.fit(X_train, y_train)

models = {
    "Logistic Regression": logreg,
    "SVM (kernel=rbf)": svm,
    "Random Forest": rf
}

print("Classifier Accuracy F1-score")

accuracies = []

for name, model in models.items():
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')
    accuracies.append(acc)
    print(f"{name} {acc*100:.2f}% {f1:.3f}")

plt.bar(models.keys(), accuracies)
plt.xticks(rotation=30)
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison")
plt.savefig("program3_accuracy.png")
print("[Bar chart: Accuracy comparison saved]")