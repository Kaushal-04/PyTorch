from mlp import model
# Adam Optimizer
import torch.optim as optim

optimizer = optim.Adam(model.parameters(), lr=0.01)