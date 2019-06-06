import gym
import numpy as np


class GraphEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.hasCargo = False
        self.hasFuel = False
        self.time = 0
        self.done = False

        # Observation Space:
        # [time, carryingCargo, caryingFueld]
        self.observation_space = spaces.MultiDiscrete([150, 1, 1])



    def step(self, action):
        ...

    def reset(self):
        self.hasCargo = False
        self.hasFuel = False
        self.time = 0
        self.done = False

    def render(self, mode='human'):
        ...

    def close(self):
        ...
