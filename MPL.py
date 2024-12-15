import torch.nn as nn
import torch

class MLP(nn.Module):
    def __init__(self, input_size): # class initialization by user input size
        super(MLP,self).__init__()
        self.hidden_layer = nn.Linear(input_size,64) # neural network layer create
        self.output_layer = nn.Linear(64,2) # first is sisze of input layer and second is Number of nodes
        self.activation = nn.ReLU() # Activation function
    def forward(self , x):
        x = self.activation(self.hidden_layer(x))
        return self.output_layer(x)
        
model = MLP(input_size=10) # instantiating or object
print(model)

output=model(torch.rand(10))# Testing the model
print(output) # output vector of length 2