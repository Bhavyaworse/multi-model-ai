import torch
import torch.nn as nn

class ScannerNetworkCNN(nn.Module):
    def __init__(self):
        super(ScannerNetworkCNN, self).__init__()
        self.convolution_block = nn.Conv2d(in_channels=1, out_channels=2, kernel_size=3, padding=1)
        self.pooling_block = nn.MaxPool2d(kernel_size=2, stride=2)
        self.dense_layer = nn.Linear(2 * 2 * 2, 2)

    def forward(self, tensor_stream):
        x = self.pooling_block(torch.relu(self.convolution_block(tensor_stream)))
        x = x.view(-1, 2 * 2 * 2)
        x = self.dense_layer(x)
        return x

neural_classifier = ScannerNetworkCNN()
synthetic_batch = torch.randn(1, 1, 4, 4)
raw_predictions = neural_classifier(synthetic_batch)

print(raw_predictions.detach().numpy())
