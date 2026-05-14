# Program 4 — Wine (SVM, RF, MLP)

import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score

data = load_wine()
X, y = data.data, data.target

print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features, {len(np.unique(y))} classes")

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

models = {
    "SVM (rbf)": SVC(kernel='rbf'),
    "Random Forest": RandomForestClassifier(),
    "MLPClassifier": MLPClassifier(max_iter=2000)
}

print("Classifier Accuracy F1(macro) Time(s)")

accuracies = []
f1s = []
times = []

for name, model in models.items():
    start = time.time()
    model.fit(X_train, y_train)
    end = time.time()

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')
    t = end - start

    accuracies.append(acc)
    f1s.append(f1)
    times.append(t)

    print(f"{name} {acc*100:.2f}% {f1:.3f} {t:.2f}")

x = np.arange(len(models))
width = 0.25

plt.bar(x - width, accuracies, width, label='Accuracy')
plt.bar(x, f1s, width, label='F1')
plt.bar(x + width, times, width, label='Time')

plt.xticks(x, models.keys(), rotation=30)
plt.legend()
plt.title("Classifier Comparison")
plt.savefig("program4_comparison.png")
print("[Comparison bar chart saved]")