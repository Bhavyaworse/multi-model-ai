import numpy as np

training_features = np.array([[2, 0.5], [5, 2.1], [0, 0.8], [9, 3.8], [1, 0.4]])
training_labels = np.array()

class CustomBoundaryClassifier:
    def __init__(self, threshold_val=4):
        self.threshold_val = threshold_val
        
    def predict(self, matrix):
        return [1 if row[0] < self.threshold_val else 0 for row in matrix]

model = CustomBoundaryClassifier(threshold_val=5)
guesses = model.predict(training_features)

matching_scores = sum(1 for p, actual in zip(guesses, training_labels) if p == actual)
print(f"Computed Metrics: {(matching_scores / len(training_labels)) * 100:.1f}%")
