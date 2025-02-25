# Predict Logic Depth
import joblib
import numpy as np

# Load model
model = joblib.load("models/logic_depth_model.pkl")

# Example feature vector for prediction
example_features = np.array([[5, 10, 3, 20]])

# Predict depth
predicted_depth = model.predict(example_features)
print(f"Predicted Logic Depth: {predicted_depth[0]}")
