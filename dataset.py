# create a custom dataset
# Example of dataset class
from torch.utils.data import Dataset

# create a toy dataset
class NumberProductDataset(Dataset):
    def __init__(self, data_range=(0,10)):
        self.numbers = list(range(data_range[0], data_range[1]))
        # consecutive nos and their products
    
    def __getitem__(self, index):
        # cprovide access
        number1 = self.numbers[index]
        number2 = self.numbers[index] + 1
        return (number1, number2), number1 * number2
    
    def __len__(self):
        # return total no. of pairs
        return len(self.numbers)
    
# Instantiate the dataset
Dataset = NumberProductDataset(
    data_range=(0,11)
)

# Access a sample
data_sample = Dataset[3]
print(data_sample)

# ((3, 4), 12) Product of 3 & 4 is 12