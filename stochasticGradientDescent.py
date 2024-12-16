from mlp import model
# PyTorch Optimizer Stochastic Gradient Descent (SGD)

import torch.optim as optim

# assume to define neural network model
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
# 0.01 is the learning rate
# momentum 0.9 smooths out updates & can help training