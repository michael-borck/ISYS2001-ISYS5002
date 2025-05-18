# A simple machine learning example using scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Prepare data
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2)

# 2. Create and train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 3. Make predictions
predictions = model.predict(X_test)

# 4. Evaluate performance
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2f}")
