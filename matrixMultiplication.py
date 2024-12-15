import torch
a = torch.tensor([[1,1],[1,0]])
print(a)
print(torch.matrix_power(a,2))
print(torch.matrix_power(a,4))