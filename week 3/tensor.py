import torch

thermal_frame = torch.tensor([[
    [10.0, 12.0, 15.0, 11.0],
    [14.0, 180.0, 195.0, 12.0],
    [11.0, 190.0, 210.0, 15.0],
    [13.0, 16.0, 12.0, 14.0]
]])

print(f"Dimensions: {thermal_frame.shape} | Datatype: {thermal_frame.dtype}")

normalized_matrix = thermal_frame / 255.0
print(normalized_matrix)
