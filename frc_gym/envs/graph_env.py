import gym
import numpy as np


class GraphEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        ...

    def step(self, action):
        ...

    def reset(self):
        ...

    def render(self, mode='human'):
        ...

    def close(self):
        ...
