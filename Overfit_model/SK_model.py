import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import random

class DNN(nn.Module):
    def __init__(self,input_size, output_size,hidden_size1=64, hidden_size2=64):
        super().__init__()
        self.Lin1=nn.Linear(input_size,hidden_size1)
        self.Lin2=nn.Linear(hidden_size1,hidden_size2)
        self.Lin3=nn.Linear(hidden_size2,output_size)
        
    def forward(self,X):
        X=F.relu(self.Lin1(X))
        X=F.relu(self.Lin2(X))
        X=self.Lin3(X)
        return X