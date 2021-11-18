from collections import namedtuple
import numpy

class Buffer():
    def __init__(self, batch_size=128,buffer_size=5e4):
        self.batch_size=batch_size
        self.buffer=buffer_size
        self.relay=[]
        self.timestep=namedtuple('experience',field_names=('state','action','reward','next_state','done'))
        self.count=0
    
    def append_timestep(self,state,action, reward,next_state,done):
        tp=self.timestep(state,action, reward,next_state,done)
        if self.count<self.buffer:
            self.relay.append(tp)
        else:
            self.relay[int((self.count+1)%self.buffer)]=tp
        self.count+=1
            
    def get_samples(self):
        np.random.seed(42)
        samples=random.sample(self.relay,self.batch_size)
        states=torch.from_numpy(np.vstack([e.state for e in samples])).float().cuda()
        actions=torch.from_numpy(np.vstack([e.action for e in samples])).long().cuda()
        rewards=torch.from_numpy(np.vstack([e.reward for e in samples])).float().cuda()
        next_states=torch.from_numpy(np.vstack([e.next_state for e in samples])).float().cuda()
        dones=torch.from_numpy(np.vstack([e.done for e in samples]).astype(np.uint8)).long().cuda()
        return states,actions, rewards,next_states,dones