# Mountain-Car v0
[![Watch the video](https://j.gifs.com/LZPV6v.gif)](https://gym.openai.com/videos/2019-10-21--mqt8Qj1mwo/MountainCar-v0/original.mp4)

## Environment:
A car is on a one-dimensional track, positioned between two "mountains". The goal is to drive up the mountain on the right; however, the car's engine is not strong enough to scale the mountain in a single pass. Therefore, the only way to succeed is to drive back and forth to build up momentum. Here, the reward is greater if you spend less energy to reach the goal

## State space:
The agent (a car) is started at the bottom of a valley. For any given state the agent may choose to accelerate to the left, right or cease any acceleration.
<table>
  <tr>
    <td>Num</td>
    <td>Observation</td>
    <td>Min</td>
    <td>Max</td>
  </tr>
  <tr>
    <td>0</td>
    <td>Car Position</td>
    <td>-1.2</td>
    <td>0.6</td>
  </tr>
    <tr>
    <td>1</td>
    <td>Car Velocity</td>
    <td>-0.07</td>
    <td>0.07</td>
  </tr>
</table>

## Action space:
The agent (a car) is started at the bottom of a valley. For any given state the agent may choose to accelerate to the left, right or cease any acceleration.
<table>
  <tr>
    <td>Num</td>
    <td>Observation</td>
    <td>Min</td>
    <td>Max</td>
  </tr>
  <tr>
    <td>0</td>
    <td>The Power coeffecient</td>
    <td>-1.0</td>
    <td>1.0</td>
  </tr>
</table>

## Rewards:
Reward of 100 is awarded if the agent reached the flag (position = 0.45) on top of the mountain. Reward is decreased based on amount of energy consumed each step.
## Starting State:
The position of the car is assigned a uniform random value in [-0.6 , -0.4]. The starting velocity of the car is always assigned to 0.
## Episode Termination:
The car position is more than 0.45. Episode length is greater than 200
