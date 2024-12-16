import torch
import torch.nn as nn
loss_function = nn.MSELoss() # define the loss function

#define the actual and predicted values as tensor
predicted_tensor = torch.tensor([320000.0])
actual_tensor = torch.tensor([300000.0])

# compute the loss
loss_value = loss_function(predicted_tensor, actual_tensor)
print(loss_value.item())
# provide the square difference