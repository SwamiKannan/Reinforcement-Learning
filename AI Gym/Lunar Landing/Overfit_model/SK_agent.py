<<<<<<< HEAD:AI Gym/Lunar Landing/Overfit model/SK_agent.py
import gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import random
from collections import defaultdict ,namedtuple

class DQNAgent():
    def __init__(self,env,buffer,dnn_pred,dnn_target,gamma=0.99,replace=500,epsilon=1):
        self.buffer=buffer
        self.pred_net=dnn_pred
        self.target_net=dnn_target
        self.replace_count=replace
        self.epsilon=epsilon
        self.gamma=gamma
        self.losses=[]
        
    def choose_action(self,env,state):
        if random.random()>self.epsilon:
            with torch.no_grad():
                state=torch.FloatTensor(state)
                action=torch.argmax(self.pred_net.forward(state)).item()
        else:
            action=env.action_space.sample()
        return action
        
    def step(self):
        states, actions, rewards, next_states,dones=self.buffer.sample()
        dones=dones.reshape(-1,1)
        acts = actions.squeeze().type(torch.int64).view(-1,1)#Get updates from buffer
        preds=self.pred_net.forward(states).squeeze().gather(-1,acts)
        #Forward pass to get predicted values for the training network ---- (1)
        target_q=torch.max(self.target_net.forward(next_states.float()),dim=1)[0].reshape(-1,1) #get max(Q(next_states)) for the target_q as the reference values
        targets=rewards+(self.gamma*target_q*(1-dones[0])).detach() # get TD update for max(Q[next_state]) 1-dones implies there should no q(next_state) or q_next state for terminal state=0 ---- (2)
        loss=criterion(preds,targets.view(-1,1))#Calculate MSE loss between (2) and (1)
        optimizer.zero_grad() #Initiate backpropogation
        loss.backward()  #Get backpropogation gradients
        optimizer.step() #Update weights
        return loss
    
    def update_target_weights(self):
        for pred, targ in zip(self.pred_net.parameters(), self.target_net.parameters()):
=======
import gym
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import random
from collections import defaultdict ,namedtuple

class DQNAgent():
    def __init__(self,env,buffer,dnn_pred,dnn_target,gamma=0.99,replace=500,epsilon=1):
        self.buffer=buffer
        self.pred_net=dnn_pred
        self.target_net=dnn_target
        self.replace_count=replace
        self.epsilon=epsilon
        self.gamma=gamma
        self.losses=[]
        
    def choose_action(self,env,state):
        if random.random()>self.epsilon:
            with torch.no_grad():
                state=torch.FloatTensor(state)
                action=torch.argmax(self.pred_net.forward(state)).item()
        else:
            action=env.action_space.sample()
        return action
        
    def step(self):
        states, actions, rewards, next_states,dones=self.buffer.sample()
        dones=dones.reshape(-1,1)
        acts = actions.squeeze().type(torch.int64).view(-1,1)#Get updates from buffer
        preds=self.pred_net.forward(states).squeeze().gather(-1,acts)
        #Forward pass to get predicted values for the training network ---- (1)
        target_q=torch.max(self.target_net.forward(next_states.float()),dim=1)[0].reshape(-1,1) #get max(Q(next_states)) for the target_q as the reference values
        targets=rewards+(self.gamma*target_q*(1-dones[0])).detach() # get TD update for max(Q[next_state]) 1-dones implies there should no q(next_state) or q_next state for terminal state=0 ---- (2)
        loss=criterion(preds,targets.view(-1,1))#Calculate MSE loss between (2) and (1)
        optimizer.zero_grad() #Initiate backpropogation
        loss.backward()  #Get backpropogation gradients
        optimizer.step() #Update weights
        return loss
    
    def update_target_weights(self):
        for pred, targ in zip(self.pred_net.parameters(), self.target_net.parameters()):
>>>>>>> 7ea86d6b1b17a71ac00a43d9292f7957ebe6d69c:SK_agent.py
            targ.data.copy_(pred.data)