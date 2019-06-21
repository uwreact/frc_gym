import numpy as np
import matplotlib.pyplot as plt
import gym


class GridWorldEnv(gym.Env):
    def __init__(self, rows, columns, magicSquares):
        self.grid = np.zeros((rows, columns))
        self.rows = rows
        self.columns = columns

        # Initialize State Space and remove terminal state (bottom right square)
        self.stateSpace = [i for i in range(self.rows * self.columns)]
        self.stateSpace.remove(self.rows * self.columns - 1)

        # State space plus contains the terminal spacae
        self.stateSpacePlus = [i for i in range(self.rows * self.columns)]

        # State space is a 1d array, thus moves up and down are multiples of rows
        self.actionSpace = {'U': -self.rows, 'D': self.rows, 'L': -1, 'R': 1}

        self.possibleActions = ['U', 'D', 'L', 'R']

        self.addMagicSquares(magicSquares)

        self.agentPosition = 0

    def addMagicSquares(self, magicSquares):
        self.magicSquares = magicSquares
        i = 2

        for square in self.magicSquares:
            x = square // self.rows
            y = square % self.columns
            self.grid[x][y] = i
            i += 1
            x = magicSquares[square] // self.rows
            y = magicSquares[square] % self.columns
            self.grid[x][y] = i
            i += 1

    def isTerminalState(self, state):
        return state in self.stateSpacePlus and state not in self.stateSpace

    def getAgentPosition(self):
        x = self.agentPosition // self.rows
        y = self.agentPosition % self.columns
        return x, y

    def setState(self, state):
        x, y = self.getAgentPosition()
        self.grid[x][y] = 0
        self.agentPosition = state
        x, y = self.getAgentPosition()
        self.grid[x][y] = 1

    def offGrid(self, newState, oldState):
        if newState not in self.stateSpacePlus:
            return True
        elif oldState % self.rows == 0 and newState % self.rows == self.rows - 1:
            # Prevents off grid move in horizontal direction
            return True
        elif oldState % self.rows == self.rows - 1 and newState % self.rows == 0:
            return True
        else:
            return False

    def actionSpaceSample(self):
        return np.random.choice(self.possibleActions)

    def step(self, action):
        resultingState = self.agentPosition + self.actionSpace[action]
        if resultingState in self.magicSquares.keys():
            resultingState = self.magicSquares[resultingState]

        reward = -1 if not self.isTerminalState(resultingState) else 0

        if not self.offGrid(resultingState, self.agentPosition):
            self.setState(resultingState)
            return resultingState, reward, self.isTerminalState(
                self.agentPosition)
        else:
            return self.agentPosition, reward, self.isTerminalState(
                self.agentPosition)

    def reset(self):
        self.agentPosition = 0
        self.grid = np.zeros((self.rows, self.columns))
        self.addMagicSquares({18: 54, 63: 14})
        return self.agentPosition

    def render(self):
        print('------------------------------------------')
        for row in self.grid:
            for col in row:
                if col == 0:
                    print('-', end='\t')
                elif col == 1:
                    print('X', end='\t')
                elif col == 2:
                    print('Ain', end='\t')
                elif col == 3:
                    print('Aout', end='\t')
                elif col == 4:
                    print('Bin', end='\t')
                elif col == 5:
                    print('Bout', end='\t')
            print('\n')
        print('------------------------------------------')
