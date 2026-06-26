import torch

layer_outputs = torch.tensor([
    [-2.5, 1.2, 0.0, 3.4],
    [0.5, -4.2, 2.1, -0.1],
    [1.1, 0.8, -1.5, 5.0]
])

relu_tensor = torch.clamp(layer_outputs, min=0.0)
print("--- Manual ReLU Activation Pass ---")
print(relu_tensor)

anomaly_mask = relu_tensor > 2.0
filtered_activations = relu_tensor * anomaly_mask.float()
print("\n--- High-Intensity Anomaly Feature Regions ---")
print(filtered_activations)
