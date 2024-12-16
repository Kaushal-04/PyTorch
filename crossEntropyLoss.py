import torch
import torch.nn as nn

# PyTorch Cross Entropy Loss model located in torch.nn module
loss_function = nn.CrossEntropyLoss() 

# cat = 0 & dog = 1 (corresponding to index 0 and 1)
target_tensor = torch.tensor([1]) # single image of dog
print(target_tensor)

# Predicton most likely to dog as index 1 is higher
predicted_tensor = torch.tensor([[2.0, 5.0]])
loss_value = loss_function(predicted_tensor, target_tensor)
print(loss_value)

# Predicton most likely to cat as index 0 is higher
predicted_tensor = torch.tensor([[1.5, 1.1]])
loss_value = loss_function(predicted_tensor, target_tensor)
print(loss_value)