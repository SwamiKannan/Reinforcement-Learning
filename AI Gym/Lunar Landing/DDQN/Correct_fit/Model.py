import torch.nn as nn
class DDQN(nn.Module):
    def __init__(self, input_size, hidden_layer1=800, hidden_layer2=200,out=4):
        super().__init__()
        self.lin1=nn.Linear(input_size,hidden_layer1)
        self.lin2=nn.Linear(hidden_layer1,hidden_layer2)
        self.lin3=nn.Linear(hidden_layer2,out)
        
        
    def forward(self,X):
        X=F.relu(self.lin1(X))
        X=F.relu(self.lin2(X))
        X=self.lin3(X)
        return X