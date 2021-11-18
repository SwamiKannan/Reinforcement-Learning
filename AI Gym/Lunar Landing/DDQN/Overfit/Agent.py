import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import namedtuple
import random
import gym

class Agent():
    def __init__(self, buffer, pred_net, tgt_net,seed,reset,gamma=0.99, epsilon=1.0, decay=0.995,epsilon_min=0.01):
        self.pred_net=pred_net
        self.tgt_net=tgt_net
        self.gamma=gamma
        self.epsilon=epsilon
        self.decay=decay
        self.epsilon_min=epsilon_min
        self.seed=seed
        self.count=0
        self.reset=reset
        self.buffer=buffer
        
    def reset_epsilon(self):
        self.epsilon=min(self.epsilon*self.decay,self.epsilon_min)
    def get_action(self,env,state):
        if random.random()>self.epsilon:
            with torch.no_grad():
                state=torch.Tensor(state).float().cuda()
                action=torch.argmax(self.pred_net.forward(state)).item()
        else:
            action = env.action_space.sample()
        return action
    
    def learn_agent(self):
        states,actions, rewards,next_states,dones=self.buffer.get_samples()
        check=self.pred_net(states)
        y_pred=self.pred_net.forward(states).gather(1,actions)
        pred_action=torch.argmax(self.pred_net(next_states),dim=1)
        y_tgt=rewards+self.gamma*((self.tgt_net(next_states).gather(1,pred_action.reshape(-1,1)))*(1-dones).detach())
        loss=criterion(y_pred,y_tgt)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        self.count+=1
        return loss
        
    def refresh(self):
        if self.count==self.reset:
            for pred, targ in zip(self.pred_net.parameters(), self.tgt_net.parameters()):
                targ.data.copy_(pred.data)
            self.count=0