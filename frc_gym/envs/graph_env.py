import gym
import numpy as np
import networkx as nx

# TODO: Cut dictionary down in half
# TODO: Better scoring
# TODO: Check if rocket complete
# TODO: Ranking points
# TODO: General Refactor
# TODO: Basic Visualization
# TODO: Update Read Me


class GraphEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.hasCargo = False
        self.hasHatch = False
        self.time = 0
        self.done = False
        self.currentState = 0

        # Observation Space:
        # [time, caryingHatch, caryingCargo]
        self.observation_space = [0, 0, 0]
        self.action_space = [0, 0, 0, 0]

        self.graph = nx.Graph()

        self.graph.add_edge('habMiddle', 'habMiddle', weight=0)
        self.graph.add_edge('habMiddle', 'habLevel2NearSide', weight=0)
        self.graph.add_edge('habMiddle', 'habLevel2FarSide', weight=0)
        self.graph.add_edge('habMiddle', 'habLevel3', weight=0)
        self.graph.add_edge('habMiddle', 'playerStationNearSideGetHatch', weight=0)
        self.graph.add_edge('habMiddle', 'playerStationNearSideGetCargo', weight=0)
        self.graph.add_edge('habMiddle', 'playerStationFarSideGetHatch', weight=0)
        self.graph.add_edge('habMiddle', 'playerStationFarSideGetCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition0FarSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition0FarSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition1FarSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition1FarSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition2FarSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition2FarSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition3FarSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition3FarSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition4FarSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition4FarSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition5FarSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition5FarSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition0NearSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition0NearSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition1NearSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition1NearSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition2NearSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition2NearSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition3NearSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition3NearSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition4NearSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition4NearSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition5NearSideScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'rocketPosition5NearSideScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip0ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip0ScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip1ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip1ScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip2ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip2ScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip3ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip3ScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip4ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip4ScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip5ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip5ScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip6ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip6ScoreCargo', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip7ScoreHatch', weight=0)
        self.graph.add_edge('habMiddle', 'cargoShip7ScoreCargo', weight=0)


    def step(self, action):
        reward = 0

        self.time += self.graph.get_edge_data(self.currentState, action)

        if action <= 4:
            reward = self.calculateHabRewards(action, self.time)
        elif action <= 7:
            #We are at the player station:
            if (action % 2):
                self.hasCargo = True
            else:
                self.hasHatch = True
        elif action <= 16:
            reward = self.calculateRocketRewards(action)
        elif action >= 26:
            reward = self.calculateCargoShipRewards(action)

        if (self.time >= 150):
            self.done = True
            self.time = 150

        self.observation_space = [self.time, self.hasHatch, self.hasCargo]
        return self.observation_space, reward, self.done

    def reset(self):
        self.hasCargo = False
        self.hasFuel = False
        self.time = 0
        self.done = False
        self.currentState = 0

    def render(self, mode='human'):
        ...

    def close(self):
        ...

    def calculateHabRewards(self, state, time):
        if time < 20:
            if state == 0:
                return 3
            elif state == 1:
                return 6
            else:
                return 12
        return 0

    def calculateCargoShipRewards(self, state):
        #We are at the cargo ship
        if (state % 2):
            # We are scoring cargo
            return 3
        else:
            #We are scoring a hatch panel
            return 2

    def calculateRocketRewards(self, state):
        if ((state - 10) % 3):
            #We are scoring a hatch:
            return 2
        return 3
