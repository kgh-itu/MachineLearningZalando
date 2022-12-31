from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

from src.get_train_test_split.fashion_mnist_data import FashionMnistData
from src.models.decision_tree.decision_tree_classifier import DecisionTreeClassifier

data = FashionMnistData()
x_train, y_train, x_test, y_test = data.get_train_test_split()
model = DecisionTreeClassifier(max_depth=9, min_samples_split=4, random_state=42)
model.fit(x_train, y_train)
preds = model.predict(x_test)
train_preds = model.predict(x_train)
print("Test ACCURACY", accuracy_score(y_test, preds))
print("Train ACCURACY", accuracy_score(y_train, train_preds))
print("F1", list(enumerate(f1_score(y_test, preds, average=None))))
print("RECALL", list(enumerate(recall_score(y_test, preds, average=None))))
print("PRECISION", list(enumerate(precision_score(y_test, preds, average=None))))
