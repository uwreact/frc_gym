import gym
import numpy as np
from gym import spaces, logger
from gym.utils import seeding
import networkx as nx
import matplotlib.pyplot as plt


class ProtoEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # Prototype environment for the 2019 FRC DeepSpace Game
        # - Consists of only a HAB, Player Station, Rocket and Cago Ship
        # - Agent begins at HAB, can pick up cargo at Player Station and then score
        #   on either the Rocket or Cago Ship
        # - Rocket awards 3 points, cargo ship awards 2 points
        # - Epsiode ends once time runs out

        # Timing:
        # HAB -> Player Station = 10
        # HAB -> Rocket = 20
        # HAB -> Cargo Ship = 15
        # HAB -> HAB = 0
        # PlayerStation -> Player Station = 0
        # PlayerStation -> Rocket = 15
        # PlayerStation -> Cargo Ship = 20
        # PlayerStation -> HAB = 10
        # Rocket -> Player Station = 15
        # Rocket -> Rocket = 0
        # Rocket -> Cargo Ship = 5
        # Rocket -> HAB = 20
        # Cargo Ship -> Player Station = 20
        # Cargo Ship -> Rocket = 5
        # Cargo Ship -> Cargo Ship = 0
        # Cargo Ship -> HAB = 15

        # Action Space: locations on field where agent can move:
        #   0 = HAB
        #   1 = Player Station
        #   2 = Rocket
        #   3 = Cargo Ship
        self.action_space = spaces.Discrete(4)

        # Observation Space:
        # [time, carryingCargo]
        self.observation_space = spaces.MultiDiscrete([150, 1])

        #Amount of time to get from one location to another
        self.times = {
            0: {
                1: 10,
                2: 20,
                3: 15,
                0: 0
            },
            1: {
                1: 0,
                2: 15,
                3: 20,
                0: 10
            },
            2: {
                1: 15,
                2: 0,
                3: 5,
                0: 20
            },
            3: {
                1: 20,
                2: 5,
                3: 0,
                0: 15
            }
        }

        self.time = 0
        self.currentSate = 0
        self.hasCargo = 0
        self.done = False

    def step(self, action):
        reward = 0

        self.time += self.times[self.currentSate][action]
        self.currentSate = action

        if (self.time >= 150):
            #Episode over
            self.done = True

            self.time = 150

        if not self.done:

            if action == 0:
                reward = 0
            if action == 1:
                self.hasCargo = True
            if action == 2:
                if self.hasCargo:
                    reward = 3
                    self.hasCargo = False
                else:
                    reward = 0
            if action == 3:
                if self.hasCargo:
                    reward = 2
                    self.hasCargo = False
                else:
                    reward = 0

        self.observation_space = [self.time, self.hasCargo]
        return self.observation_space, reward, self.done

    def reset(self):
        self.time = 0
        self.currentSate = 0
        self.hasCargo = False
        self.done = False

    def render(self, mode='human'):
        # Implement a simple graph like using networkx
        graph = nx.Graph()
        graph.add_nodes_from([0, 1, 2, 3])

        nx.draw_circular(graph, with_labels=True, font_weight='bold')
        plt.show()

    def close(self):
        ...
