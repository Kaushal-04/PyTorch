# Exapmle of Data Loader
from torch.utils.data import DataLoader

# create a toy dataset
class NumberProductDataset(DataLoader):
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
dataset = NumberProductDataset(
    data_range=(0,5)
)

# insatantiate the dataLoader
dataloader = DataLoader(dataset, batch_size=3, shuffle=True)

# Iterating over batches
for (num_pairs, products) in dataloader:
    print(num_pairs, products)

# product are in a batch together ([2, 12, 20])