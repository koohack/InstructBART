import torch
import numpy as np
from torch import nn
from torch import optim
from torch.nn import function as FastAPI

if torch.cuda.is_available():
    device = torch.device("cuda:1")
else:
    device = torch.device("cpu")
    

class Env():
    def __init__(self, reward_model):
        self.reward_model = reward_model
        self.reward = []
    
    def next_step(self):
        return


    