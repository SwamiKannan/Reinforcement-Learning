import numpy as np
import torch
import random
from collections import defaultdict ,namedtuple

class ReplayBuffer():
    def __init__(self,batch_size=64,size=int(1e4)):
        self.buffer_size=size
        self.batch_size=batch_size
        self.buffer=[]
        self.step=namedtuple('step',field_names=['state', 'action', 'reward', 'next_state', 'done']) #from https://stackoverflow.com/a/43404344 to reduce memory size
        self.states=[]
        self.actions=[]
        self.rewards=[]
        self.next_states=[]
        self.terminal=0
        self.counter=0 #count total number of items in the buffer
    
    def add_item(self, state, action, reward,next_state,done):
        st=self.step(state,action,reward,next_state, done)
        if self.counter<self.buffer_size:
            self.buffer.append(st)
        else:
            i=(self.counter+1)%self.buffer_size
            self.buffer[i]=st
        self.counter+=1

    def sample(self):
        np.random.seed(42)
        if len(self.buffer)<self.batch_size:
            print(f'Still needs to be populated: {len(self.buffer)} populated out of {self.batch_size}: {len(self.buffer)*100/self.batch_size}% complete')
        else:
            sample_idx=random.sample(self.buffer,self.batch_size)
            states_=torch.from_numpy(np.vstack([e.state for e in sample_idx if e is not None])).float().cuda()
            actions_=torch.from_numpy(np.vstack([e.action for e in sample_idx if e is not None])).long().cuda()
            rewards_=torch.from_numpy(np.vstack([e.reward for e in sample_idx if e is not None])).float().cuda()
            next_states_=torch.from_numpy(np.vstack([e.next_state for e in sample_idx if e is not None])).float().cuda()
            dones_=torch.from_numpy(np.vstack([e.done for e in sample_idx if e is not None]).astype(np.uint8)).float().squeeze().cuda()
        return (states_, actions_, rewards_, next_states_,dones_)