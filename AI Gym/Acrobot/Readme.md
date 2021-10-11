# Acrobot-v1
[![Watch the video](https://j.gifs.com/QkOG3Z.gif)](https://gym.openai.com/videos/2019-10-21--mqt8Qj1mwo/Acrobot-v1/original.mp4)
## Environment:
The acrobot system includes two joints and two links, where the joint between the two links is actuated. Initially, the links are hanging downwards, and the goal is to swing the end of the lower link up to a given height.
The acrobot was first described by Sutton [Sutton96]. We are using the version from RLPy [Geramiford15], which uses Runge-Kutta integration for better accuracy.
Acrobot is a 2-link pendulum with only the second joint actuated. Initially, both links point downwards. The goal is to swing the end-effector at a height at least the length of one link above the base. Both links can swing freely and can pass by each other, i.e., they don't collide when they have the same angle.
## State Space:
The state consists of the sin() and cos() of the two rotational joint angles and the joint angular velocities : [cos(theta1) sin(theta1) cos(theta2) sin(theta2) thetaDot1 thetaDot2].
For the first link, an angle of 0 corresponds to the link pointing downwards. The angle of the second link is relative to the angle of the first link. An angle of 0 corresponds to having the same angle between the two links.
A state of [1, 0, 1, 0, ..., ...] means that both links point downwards.
## Action Space:
The action is either applying +1, 0 or -1 torque on the joint between the two pendulum links.
Note: The dynamics equations were missing some terms in the NIPS paper which  are present in the book. R. Sutton confirmed in personal correspondence that the experimental results shown in the paper and the book were generated with the equations shown in the book. 
However, there is the option to run the domain with the paper equations by setting book_or_nips = 'nips'
## Reference:
R. Sutton: Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding (NIPS 1996)
R. Sutton and A. G. Barto: Reinforcement learning: An introduction. Cambridge: MIT press, 1998.
## Citation:
```
[Sutton96]R Sutton, "Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding", NIPS 1996.
[Geramiford15]	A Geramifard, C Dann, RH Klein, W Dabney, J How, "RLPy: A Value-Function-Based Reinforcement Learning Framework for Education and Research." JMLR, 2015.
```
## Source code for environment:
https://github.com/openai/gym/blob/master/gym/envs/classic_control/acrobot.py
