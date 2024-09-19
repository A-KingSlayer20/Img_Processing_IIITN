# Following code implements knn algorithm using sklearn library

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load dataset (Iris dataset)
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Initialize and train the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)  # K = 5
knn.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = knn.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)
